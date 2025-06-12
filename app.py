from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('singin.html')

@app.route('/register')
def register():
    return render_template('signup.html')

@app.route('/about')
def about():
    return "About page will go here"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

