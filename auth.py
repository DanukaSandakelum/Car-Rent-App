from flask import Blueprint

auth = Blueprint('auth', __name__) 
@auth.route('/login')
def login():
  return render_template("login.html")

@auth.route('/sing-up')
def sing_up():
  return render_template("sing_up.html")