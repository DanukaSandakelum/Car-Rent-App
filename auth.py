from flask import Blueprint, render_template,request

auth = Blueprint('auth', __name__) 


@auth.route('/login', methords=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("singin.html")

@auth.route('/register',methords=['GET', 'POST'])
def register():
    return render_template("signup.html")
from flask import Blueprint, render_template


