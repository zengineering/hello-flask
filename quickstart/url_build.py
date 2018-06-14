from flask import Flask, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/login")
def login():
    return "login"

@app.route("/user/<user_name>")
def profile(user_name):
    return "{}'s profile".format(user_name)

with app.test_request_context():
    print(url_for("index"))
    print(url_for("login"))
    print(url_for("login", next="/"))
    print(url_for("profile", user_name="Buzz Yj"))

#/
#/login
#/login?next=/
#/user/Buzz
