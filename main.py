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

#db = firebase.database()
#storage = firebase.auth()
auth = firebase.auth()
#print("Memory Game")
#login
def login():
    email = input("Enter your email")
    passward = input("Enter your password")
    try:
      auth.sign_in_with_email_and_password(email, passward)
      print("Successfully signed in!")
    except:
      print("Invalid user or password. Try again!")

#signup
def signin():
    email = input("Enter your email")
    password = input("Enter your password")
    confirmpass = input("Confirm password")
    if password == confirmpass :
        try:
            auth.create_user_with_email_and_password(email,password)
            print("Successfully")
        except:
            print("Email already exists")

def print_table():
    print("1. login\n"
          "2.signin\n"
          "3.exit\n\n")

while(True):
    print_table()
    op = input("Enter your number")
    print("\n")
    if int(op) == 1:
        login()
    elif int(op) == 2:
        signin()
    else:
        break


