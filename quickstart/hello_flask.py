from flask import Flask
app = Flask(__name__)

@app.route('/hello')
def hello_world():
    return "Hello Flask!"


@app.route('/')
def index():
    return "Flask Index"


@app.route('/user/<name>')
def hello_user(name):
    return "Hello {}".format(name)


@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    return "Hello from {}".format(subpath)


@app.route('/projects/')
def projects():
    return "Projects page"


@app.route('/about')
def about():
    return "About page"
