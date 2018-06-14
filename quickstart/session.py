from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

app.secret_key = "MyV3ryG00dPassw0rd"

@app.route('/')
def index():
    if 'username' in session:
        return "You are logged in as {}".format(escape(session['username']))
    else:
        return "You are not logged in."

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    else:
        return """
            <form method="post">
                <p><input type=text name=username>
                <p><input type=submit value=login>
            </form>
        """

@app.route("/logout")
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))
