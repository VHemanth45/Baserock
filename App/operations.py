from app import db
from app.models import Task
from datetime import datetime

class TaskRepository:
    def create(self, title, description, status):
        task = Task(
            title=title,
            description=description,
            status=status
        )
        db.session.add(task)
        db.session.commit()
        return task

    def get_all(self):
        return Task.query.all()

    def get_by_id(self, task_id):
        return Task.query.get(task_id)

    def update(self, task_id, data):
        task = self.get_by_id(task_id)
        if task:
            for key, value in data.items():
                setattr(task, key, value)
            db.session.commit()
        return task

    def delete(self, task_id):
        task = self.get_by_id(task_id)
        if task:
            db.session.delete(task)
            db.session.commit()
            return True
        return False