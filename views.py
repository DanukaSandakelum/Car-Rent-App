
from flask import Blueprint, render_template
from flask_login import login_required, current_user

views = Blueprint('views', __name__)

@views.route('/')
#@login_required
def home():
    return render_template("home.html")

@views.route('/Cars.html')  # URL path
def cars():  # This is the endpoint name
    return render_template('Cars.html')  # Or your logic to render the Cars.html page
