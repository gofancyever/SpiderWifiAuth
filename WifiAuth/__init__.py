from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from .admin import admin

app = Flask(__name__,instance_relative_config=True)
app.register_blueprint(admin, subdomain='admin')
app.config.from_object('config')
app.config.from_pyfile('config.py')

db = SQLAlchemy(app)