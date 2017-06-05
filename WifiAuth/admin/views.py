from flask import render_template,redirect,url_for
from . import admin
from .forms import AdminPasswordForm
from .models import Admin_user
from WifiAuth import db
@admin.route('/')
def index():
    return render_template('admin_index.html')


@admin.route('/login',methods = ['GET','POST'])
def login():
    form = AdminPasswordForm()
    if form.validate_on_submit():
        admin_user = Admin_user(form.account.data,form.password.data)
        db.session.add(admin_user)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('admin_login.html',form = form)


@admin.route('/test')
def add_admin():
    admin_user = Admin_user('admin','admin')
    db.session.add(admin_user)
    db.session.commit()
    return 'success'