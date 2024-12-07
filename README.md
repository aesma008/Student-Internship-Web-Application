# Student-Internship-Web-Application-for-Computer-Science-Students

## Prerequisites
Ensure you have the following installed on your system:
- **Python** (>= 3.x)
- **pip** (Python package installer)
- **Virtualenv** (optional but recommended)

## Installation

1. **Clone the repository**:
   ```bash
   git clone git@github.com:aesma008/Student-Internship-Web-Application.git
   ```
    ```bash
   cd Student-Internship-Web-Application
   ```
1. **Set up a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    ```
    ```bash
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```
1. ***Install dependencies:***
    ```bash
    pip install -r requirements.txt
    ```
1. ***Apply migrations:***
    ```bash
    python manage.py makemigrations
    ```
    ```bash
    python manage.py migrate
    ```

## Running the Project
1. ***Start the development server:***
    ```bash
    python manage.py runserver
    ```
1. ***Open your browser and navigate to:***
    ```bash
    localhost:8000/login
    ```