from WifiAuth import db,bcrypt
from sqlalchemy.ext.hybrid import hybrid_property

class Admin_user(db.Model):
    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def __init__(self, username, plaintext_password):
        self.username = username
        self.set_password(plaintext_password) 
        self.authenticated = False

    @hybrid_property
    def password(self):
        return self.password

    def set_password(self, plaintext_password):
        self.password = bcrypt.generate_password_hash(plaintext_password)
