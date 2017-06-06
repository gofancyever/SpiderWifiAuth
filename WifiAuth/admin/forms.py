
from flask_wtf import Form
from wtforms import StringField,PasswordField
from wtforms.validators import DataRequired


class AdminPasswordForm(Form):
    account = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])


class AdminStyleForm(Form):
    pass