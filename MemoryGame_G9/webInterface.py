from flask import Flask, render_template, request
import database

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("login.html")
@app.route("/get_signup")
def get_signup():
    return render_template("signup.HTML")


@app.route("/login", methods = ["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    if database.login(email,password):
        return "Successfully signed in!"
    return "Invalid user or password. Try again!"

@app.route("/signup", methods = ["POST"])
def signup():
    email = request.form["email"]
    password = request.form["password"]
    confirmPass = request.form["confirmPass"]
    if database.signup(email,password,confirmPass):
        return "Successfully signed in!"
    return "Invalid user or password. Try again!"

if __name__ == "__main__":
    app.run()
