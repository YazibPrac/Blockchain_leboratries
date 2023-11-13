# app/__init__.py

from flask import Flask
from flask_mongoengine import MongoEngine
from flask_json import FlaskJSON

app = Flask(__name__)
app.config.from_object('app.config')

FlaskJSON(app)  # Initialize FlaskJSON before other extensions
db = MongoEngine(app)

# Import and register your blueprints (if you have any) here
from app.routes import api
app.register_blueprint(api)
