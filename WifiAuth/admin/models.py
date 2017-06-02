from WifiAuth import db
class Admin_user(db.Model):

    id = db.Column(db.Integer,primary_key=True,autoincrement=True)
    username = db.Column(db.String(20))
    password = db.Column(db.String(20))