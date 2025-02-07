from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    from app.controllers import tasks_blueprint
    app.register_blueprint(tasks_blueprint)
    
    with app.app_context():
        db.create_all()
    
    return app