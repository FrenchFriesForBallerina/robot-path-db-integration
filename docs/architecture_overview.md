# Architecture Overview

This API is designed with modularity and scalability in mind, featuring:

## 1. Folder Structure:
- ```app/``` contains all core application files.
- ```routers/``` for API routes.
- ```schemas/``` for Pydantic models (data validation and serialization).
- ```models/``` for SQLAlchemy models (database interactions).
- ```db.py``` handles database configuration and session management.

## 2. Key Components:
- **FastAPI Routers:** Modular API route files (e.g., paths, segments) enable maintainable and scalable code.
- **Pydantic Models:** Used for validation and serialization in API requests and responses.
- **SQLAlchemy ORM:** Manages database interactions, providing a clean, Pythonic approach to SQL.