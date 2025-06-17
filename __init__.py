
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Danuka'
    # Create instance directory if it doesn't exist
    instance_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
    if not os.path.exists(instance_path):
        os.makedirs(instance_path)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{os.path.join(instance_path, DB_NAME)}'
    db.init_app(app)
    
    from viwes import views
    from auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import User, Note
    Create_database(app)
    
    return app

def Create_database(app):
    with app.app_context():
        # Ensure instance directory exists
        instance_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'instance')
        if not os.path.exists(instance_dir):
            os.makedirs(instance_dir)
            print(f"Created instance directory: {instance_dir}")
        
        # Database path should be in instance directory
        db_path = os.path.join(instance_dir, DB_NAME)
        print(f"Database path: {db_path}")
        
        try:
            db.create_all()
            print("Database tables created successfully!")
            
            # Verify the database file was created
            if os.path.exists(db_path):
                print(f"Database file '{DB_NAME}' confirmed to exist at: {db_path}")
            else:
                print(f"Warning: Database file '{DB_NAME}' was not found at: {db_path}")
                
        except Exception as e:
            print(f"Error creating database: {e}")
    
