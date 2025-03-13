from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app.config import DATABASE_URL

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Configure PostgreSQL
    app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URL
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    # Initialize database with app
    db.init_app(app)

    return app
