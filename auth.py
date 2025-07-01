
from flask import Blueprint, render_template, request, flash,redirect, url_for
from models import User
from werkzeug.security import generate_password_hash, check_password_hash
from __init__ import db

auth = Blueprint('auth', __name__) 


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("singin.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form.get('email')
        name = request.form.get('name')
        password = request.form.get('password')
        comfirm_password = request.form.get('confirm-password')
        phone = request.form.get('phone')
        
        if len(email) < 4:
            flash("Email must be greater than 3 characters", category="error")
        elif len(name) < 3:
            flash("Name must be greater than 2 character", category="error")
        elif password != comfirm_password:
            flash("Passwords don't match", category="error")
        elif len(password) < 7:
            flash("Password must be at least 7 characters", category="error")
        else:
            new_user = User(email=email, name=name, password=generate_password_hash(password,method="sha256"), phone=phone)
            db.session.add(new_user)
            db.session.commit()
            flash("Account created successfully! You can now sign in.", category="Success")
            return redirect(url_for('views.home'))

    return render_template("signup.html")
