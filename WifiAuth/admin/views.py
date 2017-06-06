from flask import render_template,redirect,url_for,request,flash,abort
from flask_login import login_user,logout_user,login_required

from . import admin
from .forms import AdminPasswordForm
from .models import Admin_user
from WifiAuth import db,photos


@admin.route('/')
@login_required
def index():
    return render_template('admin_index.html')


@admin.route('/login',methods = ['GET','POST'])
def login():
    form = AdminPasswordForm()
    if form.validate_on_submit():
        admin_user = Admin_user.query.filter_by(username=form.account.data).first_or_404()
        if admin_user.is_correct_password(form.password.data):
            login_user(admin_user)
            return redirect(url_for('profile.index'))
        else:
            return redirect(url_for('login'))
    return render_template('admin_login.html',form = form)

@admin.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@admin.route('/upload',methods=['GET','POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        url = photos.url(filename)
        return url
    return 'error'



@admin.route('/test')
def add_admin():
    admin_user = Admin_user('admin','admin')
    db.session.add(admin_user)
    db.session.commit()
    return 'success'