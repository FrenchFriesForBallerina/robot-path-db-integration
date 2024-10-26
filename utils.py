import pymap3d as pm # module to handle ENU conversion
from eralchemy import render_er # module to create ER diagrams

from config import LAT_BASE, LON_BASE, DATABASE_URL 

def convert_to_enu(latitude, longitude, altitude = 0):
    """Convert latitude, longitude, and altitude to ENU coordinates based on a reference location."""
    E, N, _ = pm.geodetic2enu(latitude, longitude, altitude, LAT_BASE, LON_BASE, altitude)
    return E, N

def generate_er_diagram_png(filename = 'er_diagram.png'):
    render_er(DATABASE_URL, filename)