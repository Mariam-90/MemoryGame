from flask import Flask, render_template, request, redirect, url_for, jsonify
import database

import users

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


@app.route("/get_login3/<user_mode>")
def get_login3(user_mode):
    print("user_mode = " + user_mode)
    return render_template("login3.html")


@app.route("/get_signup")
def get_signup():
    return render_template("signup.HTML")


@app.route("/get_signup2")
def get_signup2():
    return render_template("signup2.html")


@app.route("/get_signup3")
def get_signup3():
    return render_template("signup3.html")


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


@app.route("/get_SupervisorPage")
def get_SupervisorPage():
    return render_template("SupervisorPage.html")


@app.route("/get_letters3")
def get_letters3():
    return render_template("letters3.html")


@app.route("/get_ManegerPage")
def get_manager():
    return render_template("ManegerPage.html")


@app.route("/get_stars")
def get_stars():
    return render_template("stars.html")


@app.route("/deleteUser", methods=["POST"])
def get_deleteUser():
    return users.deletUser(database.get_user_id())


@app.route("/login2", methods=["POST"])
def login2():
    email = request.form["email"]
    password = request.form["password"]
    if database.login2(email, password):
        return render_template("SupervisorPage.html")
        # "Successfully signed in!"


@app.route("/login3", methods=["POST"])
def login3():
    email = request.form["email"]
    password = request.form["password"]
    if database.login3(email, password):
        return render_template("ManegerPage.html")
        # "Successfully signed in!"


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
        return render_template("SupervisorPage.html")  # "Successfully signed in!"
    "Invalid user or password. Try again!"


@app.route('/about_us')
def about1():
    return render_template('about_us.html', title='About',
                           content='This is the About page')


@app.route("/signup3", methods=["POST"])
def signup3():
    email = request.form["email"]
    password = request.form["password"]
    confirmPass = request.form["confirmPass"]
    if database.signup3(email, password, confirmPass):
        return render_template("ManegerPage.html")  # "Successfully signed in!"
    "Invalid user or password. Try again!"


@app.route("/selectUser", methods=["POST"])
def selectUser():
    selected = request.form['options']

    if selected == 'Player':
        return redirect(url_for('get_login', user_mode=selected))

    if selected == 'Supervisor':
        return redirect(url_for('get_login2', user_mode=selected))
    if selected == 'Manager':
        return redirect(url_for('get_login3', user_mode=selected))


@app.route("/categories")
def category():
    return render_template("chooseCategory.html", title="Home page")


@app.route("/ContactUs")
def ContactUs():
    return render_template("ContactUs.html", title="Home page")


@app.route("/base")
def base():
    return render_template("base.html")


@app.route("/Instruction")
def Instruction():
    return render_template("Instruction.html")


@app.route("/save", methods=["POST"])
def save():
    data = request.get_json()
    users.saveGame(data["difficulty"], data["category"], data["matches"])
    response = jsonify(sucess=True)
    return response


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
