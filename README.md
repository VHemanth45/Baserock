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
|_
```
## Setup

Follow these steps to set up the project:

1. **Clone the repository:**
    ```sh
    git clone https://github.com/VHemanth45/Baserock.git
    cd Baserock
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
**The API will be available at your localhost**

Now, you should have the application running and ready for development or testing.

# API EndPoints
You can test the API endpoints using Postman and create your own requests using the details below.
### Create Task
1. URL: add local host URL
2. Method: POST
3. Headers: Content-Type: application/json
4. Body: (raw JSON)
```sh
  {
  "id" : 1
  "title": "New Task",
  "description": "Task description",
  "status": "PENDING"
}
```
**Instructions in Postman:**

- Open Postman and click on New > Request.
- Set the request method to POST and enter the local Host URL [Before this Make sure the flask Application is running].
- In the Headers tab, add a header: Content-Type with value application/json.
- In the Body tab, select raw and paste the JSON example above.
- Click Send to submit the request.

### Get all Tasks
To get all the Tasks just change the METHOD to GET

### Update Task
To updata task add the task_id in the URL of which you want to change the details for eg. http://localhost:5000/tasks/1
and change the METHOD to PUT
```sh
{
  "title": "Updated Task",
  "description": "Updated Description",
  "status": "COMPLETED"
}
```
### Delete a Task
To delete a Task change Method to DELETE and then  past the URL and add the task_id at the end of the URL for eg: http://localhost:5000/tasks/{task_id}
** For this You get a 204 NO CONTENT**
## To Run the Test run the pytest command in command prompt
## To get the Coverage report run
```sh
coverage run -m pytest
coverage report -m
```
![image](https://github.com/user-attachments/assets/5c36a6f9-2c6f-455f-8138-82418b2a4013)
![image](https://github.com/user-attachments/assets/6b9ea5f1-7552-42ba-9e3f-8e6380f4dadf)

