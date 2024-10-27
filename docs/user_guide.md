# User Guide

## Running the API Locally

### 1. Start the Server:

```bash
python -m app.main
```

### 2. Navigate to Documentation:

- Swagger UI: http://127.0.0.1:8000/docs
- Redoc UI: http://127.0.0.1:8000/redoc

## Interacting with API Endpoints

The following endpoints are available:

- GET /paths/: Retrieve all paths.
- POST /paths/: Create a new path.
- GET /segments/: Retrieve all segments.
- POST /segments/: Create a new segment.