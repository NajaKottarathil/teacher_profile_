# Teacher Profile Backend API

A Flask-based REST API for managing teacher and student course information.

## Features

- Get courses for a specific student
- Get courses for a specific teacher
- Health check endpoint
- CORS enabled for frontend integration
- Mock data for demonstration

## Setup

1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

The server will start at `http://localhost:5000`

## API Endpoints

### Health Check
```
GET /api/health
```
Returns the API health status and timestamp.

### Get Student Courses
```
GET /api/courses/student/<student_id>
```
Returns all courses for a specific student.

Example response:
```json
{
    "student": {
        "id": "1",
        "name": "John Smith"
    },
    "courses": [
        {
            "id": "GEOM1010",
            "code": "GEOM 1010",
            "title": "Introduction to Geometry",
            "teacher": "Alex Martin",
            "schedule": "MWF 10:00-11:30",
            "semester": "Fall 2024"
        }
    ]
}
```

### Get Teacher Courses
```
GET /api/courses/teacher/<teacher_id>
```
Returns all courses for a specific teacher.

Example response:
```json
{
    "teacher": {
        "id": "1",
        "name": "Alex Martin",
        "subject": "Mathematics"
    },
    "courses": [
        {
            "id": "GEOM1010",
            "code": "GEOM 1010",
            "title": "Introduction to Geometry",
            "schedule": "MWF 10:00-11:30",
            "semester": "Fall 2024",
            "students": [
                {
                    "id": "1",
                    "name": "John Smith"
                }
            ]
        }
    ]
}
```

## Example API Calls

Using curl:
```bash
# Health check
curl http://localhost:5000/api/health

# Get student courses
curl http://localhost:5000/api/courses/student/1

# Get teacher courses
curl http://localhost:5000/api/courses/teacher/1
```

Using Python requests:
```python
import requests

# Health check
response = requests.get('http://localhost:5000/api/health')
print(response.json())

# Get student courses
response = requests.get('http://localhost:5000/api/courses/student/1')
print(response.json())

# Get teacher courses
response = requests.get('http://localhost:5000/api/courses/teacher/1')
print(response.json())
```

## Error Handling

The API returns appropriate HTTP status codes:
- 200: Success
- 404: Resource not found
- 500: Server error

Error responses include a message:
```json
{
    "error": "Student not found"
}
```

## Development

The project uses:
- Flask for the web framework
- Flask-CORS for cross-origin resource sharing
- Python-dotenv for environment variables
- Pytest for testing
- Black for code formatting
- Flake8 for linting 