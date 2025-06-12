from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('navbar.html')  # Or your actual template that extends navbar

@app.route('/login')
def login():
    return "Login page will go here"

@app.route('/register')
def register():
    return "Registration page will go here"

if __name__ == '__main__':
    app.run(debug=True)

