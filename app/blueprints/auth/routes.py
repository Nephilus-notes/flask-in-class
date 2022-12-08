from . import bp as app
from app.blueprints.main.models import User
from app import db
from flask import redirect, url_for, render_template, request
from flask_login import login_user, logout_user

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')

    email = request.form['email']
    password = request.form['password']

    user = User.query.filter_by(email=email).first()

    if user is None:
        return f'User with email {email} does not exist.'
    elif user.password == password:
        login_user(user)
        return redirect(url_for('main.home'))
    else:
        # user exists but password is wrong
        return f'Password is incorrect'