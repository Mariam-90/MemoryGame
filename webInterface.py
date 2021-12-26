from flask import Flask, render_template, request, redirect, url_for
import database

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chooseUser.html")


@app.route("/get_login/<user_mode>")
def get_login(user_mode):
    print("user_mode = " + user_mode)
    return render_template("login.html")


@app.route("/get_signup")
def get_signup():
    return render_template("signup.HTML")


@app.route("/get_index1")
def get_index1():
    return render_template("index1.html")


@app.route("/get_index2")
def get_index2():
    return render_template("index2.html")


@app.route("/get_index3")
def get_index3():
    return render_template("index3.html")


@app.route("/get_numbersCard1")
def get_numbersCard1():
    return render_template("numbersCard1.html")


@app.route("/get_numbersCard2")
def get_numbersCard2():
    return render_template("numbersCard2.html")


@app.route("/get_numbersCard3")
def get_numbersCard3():
    return render_template("numbersCard3.html")


@app.route("/get_letters1")
def get_letters1():
    return render_template("letters1.html")


@app.route("/get_letters2")
def get_letters2():
    return render_template("letters2.html")


@app.route("/get_letters3")
def get_letters3():
    return render_template("letters3.html")


@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    if database.login(email, password):
        return category()  # "Successfully signed in!"
    return "Invalid user or password. Try again!"


@app.route("/signup", methods=["POST"])
def signup():
    email = request.form["email"]
    password = request.form["password"]
    confirmPass = request.form["confirmPass"]
    if database.signup(email, password, confirmPass):
        return category()  # "Successfully signed in!"
    return "Invalid user or password. Try again!"


@app.route("/selectUser", methods=["POST"])
def selectUser():
    selected = request.form['options']

    return redirect(url_for('get_login', user_mode=selected))


@app.route("/categories")
def category():
    return render_template("chooseCategory.html")


@app.route("/supervisor")
def supervisor():
    return render_template("supervisor.html")


@app.route("/choose", methods=["POST"])
def choose():
    selectedLevel = request.form['level']
    selectedCategory = request.form['category']
    if selectedLevel == 'Easy':
        if selectedCategory == 'Pictures':
            return redirect(url_for('get_index1'))
    if selectedLevel == 'Medium':
        if selectedCategory == 'Pictures':
            return redirect(url_for('get_index2'))
    if selectedLevel == 'Hard':
        if selectedCategory == 'Pictures':
            return redirect(url_for('get_index3'))
    if selectedLevel == 'Easy':
        if selectedCategory == 'Numbers':
            return redirect(url_for('get_numbersCard1'))
    if selectedLevel == 'Medium':
        if selectedCategory == 'Numbers':
            return redirect(url_for('get_numbersCard2'))
    if selectedLevel == 'Hard':
        if selectedCategory == 'Numbers':
            return redirect(url_for('get_numbersCard3'))
    if selectedLevel == 'Easy':
        if selectedCategory == 'Letters':
            return redirect(url_for('get_letters1'))
    if selectedLevel == 'Medium':
        if selectedCategory == 'Letters':
            return redirect(url_for('get_letters2'))
    if selectedLevel == 'Hard':
        if selectedCategory == 'Letters':
            return redirect(url_for('get_letters3'))


if __name__ == "__main__":
    app.run()
