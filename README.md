# FastAPI Application

A simple FastAPI application with automatic reloading for development.

## Prerequisites

- Python 3.7 or higher
- pip (Python package installer)

## Setup

1. **Clone the repository** (if applicable)
   ```bash
   git clone <repository-url>
   cd <project-directory>


2. **Create a virtual environment** (recommended)
    python -m venv venv


3. **Activate the virtual environment**
    ``` On Windows:
    .\venv\Scripts\activate

    ``` On macOS/Linux:
    source venv/bin/activate


4. **Install dependencies**
    pip install -r requirements.txt


## Running the Application
Start the development server with auto-reload:
    uvicorn main:app --reload

The application will be available at:
    http://127.0.0.1:8000

Interactive API documentation:
    Swagger UI: http://127.0.0.1:8000/docs
    ReDoc: http://127.0.0.1:8000/redoc