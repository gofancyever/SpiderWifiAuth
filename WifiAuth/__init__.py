
#!/usr/bin/python
# -*- coding: uft8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_uploads import UploadSet,configure_uploads


app = Flask(__name__,instance_relative_config=True)
app.config.from_object('config')
app.config.from_pyfile('config.py')





bcrypt = Bcrypt(app)
db = SQLAlchemy(app)
photos = UploadSet('PHOTOS')
configure_uploads(app,photos)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'profile.login'

#https://stackoverflow.com/questions/41828711/flask-blueprint-sqlalchemy-cannot-import-name-db-into-moles-file
from .admin import admin
app.register_blueprint(admin, url_prefix='/admin')



