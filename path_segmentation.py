import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import splprep, splev
from geometry_msgs.msg import Point
from scipy.ndimage import gaussian_filter1d
import config

from utils import convert_to_enu

# 1 - reading and parsing file with waypoints
waypoints = []
enu_coords = []
origin = None

def load_waypoints(file_path):
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            lat, lon = map(float, line.strip().split(','))
            if i == 0:
                origin = (lat, lon)
            enu_x, enu_y = convert_to_enu(lat, lon)
            point = Point()
            point.x, point.y = enu_x, enu_y
            waypoints.append(point)
            enu_coords.append([enu_x, enu_y])

    return np.array(enu_coords), origin

# 2 - fitting a spline to the ENU coordinates
def fit_spline(enu_coords):
    tck, u = splprep([enu_coords[:, 0], enu_coords[:, 1]], s=0)
    x_spline, y_spline = splev(u, tck)
    return x_spline, y_spline

# 3 - calculating curvature using the second derivative method
def calculate_curvature(x_spline, y_spline):
    dx = np.gradient(x_spline)
    dy = np.gradient(y_spline)
    ddx = np.gradient(dx)
    ddy = np.gradient(dy)
    curvature = np.abs(ddx * dy - dx * ddy) / np.power(dx**2 + dy**2, 1.5)
    return gaussian_filter1d(curvature, sigma=config.CURVATURE_SMOOTHING_SIGMA)
    

# calculating max curvature based on max deviation
def calculate_max_curvature(max_deviation):
    # formula for the turning radius based on lateral deviation
    return 1 / max_deviation  # max allowable curvature

# 4 - segmenting the path based on curvature behavior
def classify_segments(x, y, curvature, curvature_threshold, curvature_variation_threshold):
    straight_segments = []
    arc_segments = []
    clothoid_segments = []
    spline_segments = []
    current_segment = []
    last_type = None
    window_size = config.WINDOW_SIZE

    for i in range(len(x)):
        segment_type = None
        curvature_window = curvature[max(0, i-window_size):i+window_size]

        # straight line: near-zero curvature
        if abs(curvature[i]) < curvature_threshold:
            segment_type = 'Straight Line'
        # circular arc: constant curvature with low variance
        elif np.std(curvature_window) < curvature_variation_threshold:
            segment_type = 'Circular Arc'
        # clothoid: gradually changing curvature over a window
        elif np.all(np.diff(curvature_window) > 0) or \
             np.all(np.diff(curvature_window) < 0):
            segment_type = 'Clothoid Curve'
        # spline or other curve: complex or inconsistent curvature
        else:
            segment_type = 'Spline'

        # adding point to the current segment
        current_segment.append((x[i], y[i]))

        # if segment type changes and the current segment is long enough, finalize the segment
        if segment_type != last_type and len(current_segment) > 2:
            if last_type == 'Straight Line':
                straight_segments.append(current_segment)
            elif last_type == 'Circular Arc':
                arc_segments.append(current_segment)
            elif last_type == 'Clothoid Curve':
                clothoid_segments.append(current_segment)
            elif last_type == 'Spline':
                spline_segments.append(current_segment)
            
            # create a smooth transition by keeping the last point in the new segment
            current_segment = [(x[i], y[i])]  # keep the last point to avoid gaps

        last_type = segment_type

    # appending the final segment
    if len(current_segment) > 2:
        if last_type == 'Straight Line':
            straight_segments.append(current_segment)
        elif last_type == 'Circular Arc':
            arc_segments.append(current_segment)
        elif last_type == 'Clothoid Curve':
            clothoid_segments.append(current_segment)
        elif last_type == 'Spline':
            spline_segments.append(current_segment)

    return straight_segments, arc_segments, clothoid_segments, spline_segments

# plotting function to show segment start/end points
def plot_segments_with_markers(x_spline, y_spline, straight_segments, arc_segments, clothoid_segments, spline_segments):
    # combining all segments
    segments = straight_segments + arc_segments + clothoid_segments + spline_segments
    segment_types = ['Straight Line'] * len(straight_segments) + \
                    ['Circular Arc'] * len(arc_segments) + \
                    ['Clothoid Curve'] * len(clothoid_segments) + \
                    ['Spline'] * len(spline_segments)

    # defining colors for each segment type
    colors = {'Straight Line': 'blue', 'Circular Arc': 'green', 'Clothoid Curve': 'orange', 'Spline': 'red'}

    # plotting the full path
    plt.plot(x_spline, y_spline, label='Full Path', color='gray', linestyle='--')

    # plotting each segment and marking start/end points
    for i, segment in enumerate(segments):
        segment_x, segment_y = zip(*segment)
        plt.plot(segment_x, segment_y, color=colors[segment_types[i]], label=f'{segment_types[i]} {i}')
        
        # marking start and end points
        plt.scatter(segment_x[0], segment_y[0], color=colors[segment_types[i]], marker='o', s=100, edgecolor='black')  # Start point
        plt.scatter(segment_x[-1], segment_y[-1], color=colors[segment_types[i]], marker='s', s=100, edgecolor='black')  # End point

    # legend
    plt.legend(handles=[plt.Line2D([0], [0], color=color, lw=2, label=type_name) for type_name, color in colors.items()], title="Segment Types")
    plt.title('Path Segmentation with Start/End Points')
    plt.xlabel('X (ENU)')
    plt.ylabel('Y (ENU)')
    plt.grid(True)
    plt.show()

# function to plot curvature to see how it changes throughout the path
def plot_curvature(curvature_smooth):
    plt.figure(figsize=(10, 6))
    plt.plot(range(len(curvature_smooth)), curvature_smooth, label='Curvature', color='purple')
    plt.title('Curvature Along the Path')
    plt.xlabel('Path Point Index')
    plt.ylabel('Curvature')
    plt.grid(True)
    plt.show()

# main workflow
enu_coords, origin = load_waypoints('path.txt')
x_spline, y_spline = fit_spline(enu_coords)
curvature_smooth = calculate_curvature(x_spline, y_spline)

# max deviation settings
max_deviation = config.MAX_DEVIATION
max_curvature = calculate_max_curvature(max_deviation)

# classifying segments using the method with curvature constraints
straight_segments, arc_segments, clothoid_segments, spline_segments = classify_segments(
    x_spline, y_spline, curvature_smooth, 
    curvature_threshold=np.max(curvature_smooth) * config.MAX_DEVIATION,  
    curvature_variation_threshold=config.CURVATURE_VARIATION_THRESHOLD,
)

# debugging
print(f"Number of Straight Line segments: {len(straight_segments)}, \
    \nNumber of Circular Arc segments: {len(arc_segments)}, \
    \nNumber of Clothoid Curve segments: {len(clothoid_segments)}, \
    \nNumber of Spline segments: {len(spline_segments)}",)

# plotting the path and segments
plot_segments_with_markers(x_spline, y_spline, straight_segments, arc_segments, clothoid_segments, spline_segments)

# plot_curvature(curvature_smooth)