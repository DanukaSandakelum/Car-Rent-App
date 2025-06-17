
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
import os


db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Danuka'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)
    
    from viwes import views
    from auth import auth
    
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')

    from models import User, Note
    Create_database(app)
    
    return app

def Create_database(app):
    # Get absolute path for database
    basedir = os.path.abspath(os.path.dirname(__file__))
    db_path = os.path.join(basedir, DB_NAME)
    
    print(f"Checking for database at: {db_path}")
    
    if not os.path.exists(db_path):
        with app.app_context():
            try:
                db.create_all()
                print("Database tables created successfully!")
            except Exception as e:
                print(f"Error creating database: {e}")
    else:
        print("Database already exists!")
    
    # Verify the database file was created
    if os.path.exists(db_path):
        print(f"Database file '{DB_NAME}' confirmed to exist at: {db_path}")
    else:
        print(f"Warning: Database file '{DB_NAME}' was not created at: {db_path}")
    
