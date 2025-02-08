from flask import Blueprint, request, jsonify
from app.services import TaskService
from http import HTTPStatus

tasks_blueprint = Blueprint('tasks', __name__)
task_service = TaskService()

@tasks_blueprint.route('/tasks', methods=['POST'])
def create_task():
    data = request.get_json()
    
    try:
        task = task_service.create_task(
            title=data.get('title'),
            description=data.get('description'),
            status=data.get('status', 'PENDING')
        )
        return jsonify(task.to_dict()), HTTPStatus.CREATED
    except ValueError as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

@tasks_blueprint.route('/tasks', methods=['GET'])
def get_all_tasks():
    page = request.args.get('page', default = 1, type=int)
    per_page = request.args.get('per_page', default = 10, type=int)
    pagination = task_service.get_all_tasks_paginated(page, per_page)

    response = {
        "total": pagination.total,
        'tasks': [task.to_dict() for task in pagination.items],
        'page': pagination.page,
        'per_page': pagination.per_page,
        'total_pages': pagination.pages,
    }
    return jsonify(response),HTTPStatus.OK

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()
    
    try:
        task = task_service.update_task(task_id, data)
        if task:
            return jsonify(task.to_dict())
        return jsonify({'error': 'Task not found'}), HTTPStatus.NOT_FOUND
    except ValueError as e:
        return jsonify({'error': str(e)}), HTTPStatus.BAD_REQUEST

@tasks_blueprint.route('/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    if task_service.delete_task(task_id):
        return '', HTTPStatus.NO_CONTENT
    return jsonify({'error': 'Task not found'}), HTTPStatus.NOT_FOUND