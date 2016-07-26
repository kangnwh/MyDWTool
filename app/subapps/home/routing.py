 # -*- coding: utf-8 -*-
from flask import Blueprint,url_for,flash,request,abort
from flask import render_template,redirect
from app.subapps.home.forms import LoginForm
from app.models.User import User
from flask_login import login_user,logout_user,login_required

import hashlib

homeRoute = Blueprint('homeRoute', __name__,
                     template_folder='templates', static_folder='static')


@homeRoute.route('/', methods=['GET', 'POST'])
@login_required
def index():

    return render_template('home/index.html')

@homeRoute.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Login and validate the user.
        # user should be an instance of your `User` class
        email = form.email.data
        md5 = hashlib.md5()
        md5.update(form.password.data.encode('utf-8'))
        #password = md5.hexdigest()
        password = form.password.data
        user = User.query.filter_by(email=email,password=password).first()
        if user :
            login_user(user,remember = form.remember_me.data)
            next = request.args.get('next')
            # TODO
            # next_is_valid should check if the user has valid
            # permission to access the `next` url
            #if not next_is_valid(next):
            #    return abort(400)

            return redirect(next or url_for('homeRoute.index'))

        else:
            flash("User ID or Password invalid.")

    return render_template('home/login.html', form=form)

@homeRoute.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('homeRoute.login'))