from flask import Flask, render_template
import sys

application = Flask(__name__)

@application.route("/")
def hello():
    return render_template("index.html")

@application.route("/login")
def view_login():
    return render_template("login.html")

if __name__ == "__main__":
    application.run(host='0.0.0.0', port=5000)