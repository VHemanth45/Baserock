from app.operations import TaskRepository

class TaskService:
    def __init__(self):
        self.repository = TaskRepository()

    def create_task(self, title, description, status):
        if not title or not status:
            raise ValueError("Title and status are required")
        
        if status not in ['PENDING', 'COMPLETED']:
            raise ValueError("Invalid status value")
            
        return self.repository.create(title, description, status)

    def get_all_tasks(self):
        return self.repository.get_all()

    def update_task(self, task_id, data):
        if 'status' in data and data['status'] not in ['PENDING', 'COMPLETED']:
            raise ValueError("Invalid status value")
            
        return self.repository.update(task_id, data)

    def delete_task(self, task_id):
        return self.repository.delete(task_id)