# Employee and Department Management API

## Overview
This API allows for managing employee and department information. The API is built using Django and Django REST framework, enabling the user to retrieve all employee and department data (GET) or add new records (POST).

## Project Structure

- **`views.py`**: Contains the logic for handling API requests (GET and POST) for employee and department records.
- **`models.py`**: Defines the database models for storing employee and department information.
- **`serializer.py`**: Defines the serializer class used for validating and saving the incoming data.

## API Endpoints

### 1. **`/api/employees/`** (GET)
This endpoint retrieves a list of all employees along with their department details.

### Example Response:
```json
[
    {
        "employee": "John Doe",
        "department": "Engineering"
    },
    {
        "employee": "Jane Smith",
        "department": "Marketing"
    }
]
