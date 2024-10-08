from src import models
from src.app import app
from src.models.db import db

with app.app_context():
    db.create_all()