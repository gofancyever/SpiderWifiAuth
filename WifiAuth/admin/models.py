from WifiAuth import db,bcrypt,login_manager
from sqlalchemy.ext.hybrid import hybrid_property
from flask_login import UserMixin


@login_manager.user_loader
def load_user(userid):
    return Admin_user.query.filter(Admin_user.id==userid).first()

class Admin_user(db.Model,UserMixin):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    _password = db.Column(db.String(128))

    def __init__(self, username, plaintext_password):
        self.username = username
        self.password = plaintext_password
        self.authenticated = False

    @hybrid_property
    def password(self):
        return self._password
    @password.setter
    def set_password(self, plaintext_password):
        self._password = bcrypt.generate_password_hash(plaintext_password)

    def is_correct_password(self, plaintext):
        if bcrypt.check_password_hash(self._password, plaintext):
            return True
        return False