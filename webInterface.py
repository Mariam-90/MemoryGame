from flask import Flask, render_template, request, redirect, url_for
import database
from database import saveGame

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("chooseUser.html")


@app.route("/get_login/<user_mode>")
def get_login(user_mode):
    print("user_mode = " + user_mode)
    return render_template("login.html")


@app.route("/get_login2/<user_mode>")
def get_login2(user_mode):
    print("user_mode = " + user_mode)
    return render_template("login2.html")


@app.route("/get_signup")
def get_signup():
    return render_template("signup.HTML")


@app.route("/get_signup2")
def get_signup2():
    return render_template("signup2.html")


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


@app.route("/get_stars")
def get_stars():
    return render_template("stars.html")


@app.route("/login2", methods=["POST"])
def login2():
    email = request.form["email"]
    password = request.form["password"]
    if database.login2(email, password):
        return supervisor1()  # "Successfully signed in!"
    return "Invalid user or password. Try again!"


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


@app.route("/signup2", methods=["POST"])
def signup2():
    email = request.form["email"]
    password = request.form["password"]
    confirmPass = request.form["confirmPass"]
    if database.signup2(email, password, confirmPass):
        return supervisor1()  # "Successfully signed in!"
    return "Invalid user or password. Try again!"


@app.route("/selectUser", methods=["POST"])
def selectUser():
    selected = request.form['options']

    if selected == 'Player':
        return redirect(url_for('get_login', user_mode=selected))

    if selected == 'Supervisor':
        return redirect(url_for('get_login2', user_mode=selected))


@app.route("/categories")
def category():
    return render_template("chooseCategory.html")


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    saveGame(data["difficulty"], data["category"], data["matches"])
    return render_template("save")


@app.route("/supervisor1")
def supervisor1():
    return render_template("supervisor1.html")


@app.route("/supervisor22")
def supervisor():
    return render_template("supervisor22.html")


@app.route("/choose", methods=["POST"])
def choose():
    selectedLevel = request.form['level']
    selectedCategory = request.form['category']
    if selectedCategory == 'Pictures':
        if selectedLevel == 'Easy':
            return redirect(url_for('get_index1'))
        elif selectedLevel == 'Medium':
            return redirect(url_for('get_index2'))
        else:
            return redirect(url_for('get_index3'))
    # came bake her llooll

    if selectedCategory == 'Numbers':
        if selectedLevel == 'Easy':
            return redirect(url_for('get_numbersCard1'))
        elif selectedLevel == 'Medium':
            return redirect(url_for('get_numbersCard2'))
        else:
            return redirect(url_for('get_numbersCard3'))

    if selectedCategory == 'Letters':
        if selectedLevel == 'Easy':
            return redirect(url_for('get_letters1'))
        elif selectedLevel == 'Medium':
            return redirect(url_for('get_letters2'))
        else:
            return redirect(url_for('get_letters3'))


if __name__ == "__main__":
    app.run()
