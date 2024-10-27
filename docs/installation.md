# Installation Guide

This guide will walk you through setting up the project on your local machine.

## Prerequisites

Ensure you have the following installed:

- **Python 3.8+**
- **PostgreSQL** (or another SQL database)
- **Pip** (Python package manager)

## Setup Instructions

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/FrenchFriesForBallerina/robot-path-db-integration.git
cd robot-path-db-integration
```

### 2. Install Dependencies

Use ```pip``` to install all required dependencies:

```
pip install -r requirements.txt
```

### 3. Database Configuration

Set up the database for the project:

1. **Update the Database URL:** Open ```config.py``` and update the ```DATABASE_URL``` variable with the URL of your database.

2. **Initialize the Database:** Run the following command to initialize the database and create necessary tables:

```
python -m app.db
```

### 4. Environment Configuration

Configure environment variables as needed for your setup:

- **PORT**: Define the port the application will use (default is usually 8000).

- **DATABASE_URL**: Ensure this variable points to your PostgreSQL database (or other SQL database) in ```config.py```.

### 5. Run the Application

To start the application, run the following command:

```
python -m app.main
```

### 6. Access the API Documentation

The application provides interactive API documentation via Swagger UI. After starting the application, you can access the documentation at the configured port. For example, for default settings, it will be on:

http://127.0.0.1:8000/docs