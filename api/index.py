from flask import Flask, redirect

app = Flask(__name__)


@app.route('/')
def home():
    return redirect('/resources/html/index.html')


@app.route('/about')
def about():
    return 'About'
