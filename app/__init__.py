# app/__init__.py
from flask import Flask
from .models import db
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///inv.db'
    db.init_app(app)
    Migrate(app, db)
    return app
