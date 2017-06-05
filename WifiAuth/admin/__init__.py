from flask import Blueprint
admin = Blueprint('profile', __name__, url_prefix='/admin',template_folder='templates')
from . import views