# Testing Guide

This guide provides an overview of the testing approach used for the API project, including setup, test execution, and validation steps.

## Table of Contents
- [Overview](#overview)
- [Setting Up Testing Environment](#setting-up-testing-environment)
- [Running Tests](#running-tests)
- [Test Coverage](#test-coverage)
- [Troubleshooting](#troubleshooting)

## Overview
The project uses ```pytest``` for running tests and ```FastAPI```'s ```TestClient``` to make requests to the endpoints, verifying both API functionality and response structure. Tests are divided into main tests for endpoint availability and feature tests for each endpoint functionality (e.g., ```/paths/```).

[Back to Table of Contents](#table-of-contents)

## Setting Up Testing Environment
### Prerequisites
Ensure that the following are installed:

- Python 3.8+
- ```pytest``` library
- ```fastapi``` and ```httpx``` for API testing

### Installation of Required Packages
Install the dependencies by running:

```
pip install -r requirements.txt
```

Make sure you are in the correct environment, as certain dependencies (like ```FastAPI``` and ```pytest```) must align with the project's Python version.

[Back to Table of Contents](#table-of-contents)

## Running Tests

### Running All Tests

To run all tests, use:

```
pytest -vv --disable-warnings tests/
```
This command runs all test files within the ```tests/``` folder, providing verbose output.

### Running A Specific Test

To run a specific test file, specify its path:

```
pytest -s -vv --disable-warnings tests/test_paths.py
```
Use the ```-s``` flag to display ```print``` statements for debugging.

[Back to Table of Contents](#table-of-contents)

## Test Coverage

### Main Test File: ```test_main.py```

Tests the base functionality and root endpoint availability.

- **Example Test:**

```
def test_main():
    response = client.get("/")
    assert response.status_code == 200
    assert "main" in response.json()
```

### Path Tests: ```test_paths.py```

Verifies ```/paths/``` endpoint functionality, including retrieving paths and validating JSON response structure.

- **Get Paths Test:**

```
def test_get_paths():
    response = client.get("/paths/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0
```

### Extended Path Tests
Additional tests cover creating and retrieving specific paths.

- **Create Path Test**

```
def test_create_path():
    response = client.post("/paths", json={"name": "Test Path", "origin_lat": 0.0, "origin_lon": 0.0, "total_length": 100.0})
    assert response.status_code == 200
    assert response.json()["name"] == "Test Path"
```

[Back to Table of Contents](#table-of-contents)

## Troubleshooting
### Common Errors and Fixes
- **404 Not Found**: Ensure the endpoint is correctly registered in the router.
- **500 Internal Server Error**: Check database connection settings and ensure migrations are up to date.
- **JSON Parse Errors**: Confirm that the API response is structured correctly as JSON.

### Debugging Tips
- Use ```print``` statements in test files to view response data.
- Run tests individually with ```-s``` for easier debugging and detailed output.
- Check for response status code mismatches, as they can reveal configuration issues.

[Back to Table of Contents](#table-of-contents)