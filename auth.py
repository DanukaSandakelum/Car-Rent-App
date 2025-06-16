from flask import Blueprint, render_template,request,flash

auth = Blueprint('auth', __name__) 


@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("singin.html")

@auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST'
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    comfirm_password = request.form.get('confirm_password')
    phone = request.form.get('phone')
    if len(email)<4
        flash("Email must be greater than 3 characters",category="error")
    elif len(name)<3
        flash("Name must be greater than 2 character",category="error")
    elif password != comfirm_password
        flash("Passwords don't match")
    elif len(password)<7
        flash("Password must be at least 7 characters",category="error")
    else
    flash("Account created",category="Sucsess")

    
    return render_template("signup.html")


