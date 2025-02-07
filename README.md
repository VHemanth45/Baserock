# Task Management 

A simple Flask-based API for managing tasks. This project demonstrates a modular architecture separating the application into routes, services, and repositories layers. It also includes unit tests and coverage reports to ensure code quality.

## Features

- **Create Tasks:** Add new tasks with a title, description, and status.
- **Read Tasks:** Retrieve all tasks or a specific task by ID.
- **Update Tasks:** Modify an existing task’s details.
- **Delete Tasks:** Remove tasks by ID.
- **Error Handling:** Returns appropriate HTTP status codes and error messages for invalid operations.
- **Test Coverage:** Unit tests for services and repositories with [pytest](https://docs.pytest.org/) and [coverage.py](https://coverage.readthedocs.io/).

## Project Structure

```plaintext
project/
├── app/
│   ├── __init__.py          # Application factory and configuration setup
│   ├── databasedef.py       # Database model definitions (e.g., Task model)
│   ├── repositories.py      # Repository layer handling database operations
│   ├── routes.py            # API routes defined using Flask Blueprints
│   └── services.py          # Business logic and service layer for tasks
├── config.py                # Application configuration settings
├── tests/
│   ├── __init__.py          # Test package initializer
│   ├── test_repositories.py # Tests for the repository layer
│   ├── test_services.py     # Tests for the service layer

## Setup

Follow these steps to set up the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/task-management.git
    cd task-management
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. Adjust config.py as needed

5. **Run the application:**
    ```sh
    flask run
    ```
**The API will be available at your localhost

Now, you should have the application running and ready for development or testing.



