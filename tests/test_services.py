import pytest
from app import create_app, db
from app.services import TaskService

@pytest.fixture
def task_service():
    """
    Fixture to create a fresh app context and database for service tests.
    """
    app = create_app()
    with app.app_context():
        db.create_all()
        service = TaskService()
        yield service
        db.session.remove()
        db.drop_all()

def test_create_task_success(task_service):
    task = task_service.create_task(title="Service Task", description="Service Desc", status="PENDING")
    assert task.id is not None
    assert task.title == "Service Task"
    assert task.status == "PENDING"

def test_create_task_missing_title(task_service):
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task(title="", description="No title", status="PENDING")
    assert "Title and status are required" in str(exc_info.value)

def test_create_task_missing_status(task_service):
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task(title="Title", description="Desc", status=None)
    assert "Title and status are required" in str(exc_info.value)

def test_create_task_invalid_status(task_service):
    with pytest.raises(ValueError) as exc_info:
        task_service.create_task(title="Title", description="Desc", status="INVALID")
    assert "Invalid status value" in str(exc_info.value)

def test_get_all_tasks(task_service):
    # Create two tasks
    task_service.create_task(title="Task 1", description="Desc 1", status="PENDING")
    task_service.create_task(title="Task 2", description="Desc 2", status="COMPLETED")
    tasks = task_service.get_all_tasks()
    assert len(tasks) == 2

def test_update_task_success(task_service):
    task = task_service.create_task(title="Old Title", description="Old Desc", status="PENDING")
    updated = task_service.update_task(task.id, {"title": "Updated Title", "status": "COMPLETED"})
    assert updated is not None
    assert updated.title == "Updated Title"
    assert updated.status == "COMPLETED"

def test_update_task_invalid_status(task_service):
    task = task_service.create_task(title="Task", description="Desc", status="PENDING")
    with pytest.raises(ValueError) as exc_info:
        task_service.update_task(task.id, {"status": "INVALID"})
    assert "Invalid status value" in str(exc_info.value)

def test_update_nonexistent_task(task_service):
    # Attempt to update a task that does not exist (e.g., with id 999)
    updated = task_service.update_task(999, {"title": "Doesn't matter"})
    assert updated is None

def test_delete_task(task_service):
    task = task_service.create_task(title="Task", description="Desc", status="PENDING")
    result = task_service.delete_task(task.id)
    assert result is True
    # Deleting again should return False since the task no longer exists.
    result_again = task_service.delete_task(task.id)
    assert result_again is False

def test_delete_nonexistent_task(task_service):
    # Deleting a non-existent task should return False.
    result = task_service.delete_task(999)
    assert result is False
