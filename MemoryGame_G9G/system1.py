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
"""""
window = tk.Tk()
window.minsize(height = 1000, width = 1000)
window.title("Memory Game")
LOGIN = tk.Frame(window)#mini window in winodw
label_email = tk.Label(LOGIN, text = "Enter your email :")#print
entry_email = tk.Entry(LOGIN)
LOGIN.pack()
label_email.grid(row = 0, column = 0)
entry_email.grid(row = 0 , column = 1)
label_password = tk.Label(LOGIN, text = "Enter your password :")
entry_password = tk.Entry(LOGIN, show="*")
label_password.grid(row = 1, column = 0)
entry_password.grid(row = 1 , column = 1)
button_login = tk.Button(LOGIN, text = "Login", fg = "green", bg = "grey", command = login ).grid(row = 2, column = 1,  ipadx = 50)
window.mainloop()
"""
firebase = pyrebase.initialize_app(firebaseConfig)
#db = firebase.database()
#storage = firebase.auth()
auth = firebase.auth()
#login
print("Memory Game")
def login():
    email = input("Enter your email")
    passward = input("Enter your password")
    try:
      auth.sign_in_with_email_and_password(email, passward)
      print("Successfully signed in!")
    except:
      print("Invalid user or password. Try again!")

#signup
def signup():
    email = input("Enter your email")
    password = input("Enter your password")
    confirmpass = input("Confirm password")
    if password == confirmpass :
        try:
            auth.create_user_with_email_and_password(email,password)
            print("Successfully")
        except:
            print("Email already exists")


