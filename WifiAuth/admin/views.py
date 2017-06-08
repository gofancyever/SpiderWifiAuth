from flask import render_template,redirect,url_for,request,flash,abort
from flask_login import login_user,logout_user,login_required
from flask import json
from . import admin
from .forms import AdminPasswordForm,AdminPhoto
from .models import Admin_user
from WifiAuth import db,photos




# 登录
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

#主页
@admin.route('/',methods=['GET','POST'])
def upload():
    form = AdminPhoto()
    if form.validate_on_submit():
        filename = photos.save(form.photo.data)
        fileurl = photos.url(filename)
    else:
        fileurl = None
    return render_template('admin_index.html',form=form,file_url=fileurl)



@admin.route('/submit',methods=['GET','POST'])
def submit():
    print(request.form)
    return json.dumps(request.form)


@admin.route('/test_preview')
def preview():
    return render_template('admin_preview.html')

@admin.route('/test')
def add_admin():
    admin_user = Admin_user('admin','admin')
    db.session.add(admin_user)
    db.session.commit()
    return 'success'