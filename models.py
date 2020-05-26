from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from app import APP
from flask_migrate import Migrate

db_url = "postgres://postgres:postgres@localhost:5432/castingAgency"
db = SQLAlchemy()

def setup_database(app, database_path=db_url):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.create_all()
    migrate = Migrate(app, db)