import pytest
from app import create_app, db
from app.operations import TaskRepository
from app.databasedef import Task

@pytest.fixture
def repo():
    """
    Fixture to create a fresh app context and database for repository tests.
    """
    app = create_app()
    with app.app_context():
        db.create_all()
        repository = TaskRepository()
        yield repository
        db.session.remove()
        db.drop_all()

def test_create_task(repo):
    task = repo.create(title="Test Task", description="Test Description", status="PENDING")
    assert task.id is not None
    assert task.title == "Test Task"
    assert task.description == "Test Description"
    assert task.status == "PENDING"

def test_get_all_tasks(repo):
    # Create two tasks
    task1 = repo.create(title="Task 1", description="Desc 1", status="PENDING")
    task2 = repo.create(title="Task 2", description="Desc 2", status="COMPLETED")
    tasks = repo.get_all()
    assert len(tasks) == 2
    assert any(t.id == task1.id for t in tasks)
    assert any(t.id == task2.id for t in tasks)

def test_get_by_id(repo):
    task = repo.create(title="Task", description="Desc", status="PENDING")
    found = repo.get_by_id(task.id)
    assert found is not None
    assert found.id == task.id

def test_update_task(repo):
    task = repo.create(title="Old Title", description="Old Desc", status="PENDING")
    updated = repo.update(task.id, {"title": "New Title", "description": "New Desc", "status": "COMPLETED"})
    assert updated is not None
    assert updated.title == "New Title"
    assert updated.description == "New Desc"
    assert updated.status == "COMPLETED"

def test_delete_task(repo):
    task = repo.create(title="Task to delete", description="Desc", status="PENDING")
    result = repo.delete(task.id)
    assert result is True
    assert repo.get_by_id(task.id) is None

def test_update_nonexistent_task(repo):
    # Update a task that doesn't exist should return None
    result = repo.update(999, {"title": "New Title"})
    assert result is None

def test_delete_nonexistent_task(repo):
    # Deleting a non-existent task should return False.
    result = repo.delete(999)
    assert result is False

def test_get_all_tasks_empty(repo):
    tasks = repo.get_all()
    assert tasks == []

def test_update_task_no_changes(repo):
    task = repo.create(title="No Changes", description="Desc", status="PENDING")
    updated = repo.update(task.id, {})
    # Expect no changes
    assert updated is not None
    assert updated.title == "No Changes"
    assert updated.description == "Desc"
    assert updated.status == "PENDING"

def test_update_task_partial_fields(repo):
    task = repo.create(title="Partial Update", description="Desc", status="PENDING")
    updated = repo.update(task.id, {"status": "COMPLETED"})
    assert updated is not None
    assert updated.title == "Partial Update"  # unchanged
    assert updated.status == "COMPLETED"


