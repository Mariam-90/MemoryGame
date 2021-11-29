from flask import Flask, render_template, request
import pyrebase

firebaseConfig = {
    'apiKey': "AIzaSyCBKOCoHC9E_NkJVwFAqquQT-u08wki5D0",
    'authDomain': "memorygame-dcf08.firebaseapp.com",
    'databaseURL':'https://memorygame-dcf08-default-rtdb.firebaseio.com/',
    'projectId': "memorygame-dcf08",
    'storageBucket': "memorygame-dcf08.appspot.com",
    'messagingSenderId': "1038386322318",
    'appId': "1:1038386322318:web:9ee61b9c9c773606e322df",
    ' measurementId': "G-QX06D6EKEW"
}
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/handle_data", methods = ["POST"])
def handle_data():
    username = request.form["email"]
    passward = request.form["password"]
    try:
      auth.sign_in_with_email_and_password(username, passward)
      print("Successfully signed in!")
      return "Successfully signed in!"
    except:
        print("Invalid user or password. Try again!")
        return "Invalid user or password. Try again!"




if __name__ == "__main__":
    app.run()
