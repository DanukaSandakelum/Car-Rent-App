
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path


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
    if not path.exists(DB_NAME):
        with app.app_context():
            db.create_all()
            print("Created Database!")
    else:
        print("Database already exists!")
    
    # Verify the database file was created
    if path.exists(DB_NAME):
        print(f"Database file '{DB_NAME}' confirmed to exist")
    else:
        print(f"Warning: Database file '{DB_NAME}' was not created")
    
