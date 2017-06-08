
from flask_wtf import Form
from wtforms import StringField,PasswordField,SubmitField
from flask_wtf.file import FileField,FileAllowed,FileRequired
from wtforms.validators import DataRequired
from WifiAuth import photos

class AdminPasswordForm(Form):
    account = StringField('用户名',validators=[DataRequired()])
    password = PasswordField('密码',validators=[DataRequired()])
    submit = SubmitField(u'登录')


class AdminPhoto(Form):
    photo = FileField('图片上传',validators=[FileAllowed(photos,'只能上传图片'),FileRequired('web花瓣为选择')])
    submit = SubmitField(u'上传')