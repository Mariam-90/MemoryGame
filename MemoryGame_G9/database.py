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
def login(email,password ):
    flag = False
    try:
      auth.sign_in_with_email_and_password(email, password)
      flag = True
    except:
        pass
    return flag
#signup
def signup(email,password,confirmpass):
    flag = False
    if password == confirmpass :
        try:
            auth.create_user_with_email_and_password(email,password)
            flag = True
        except:
            pass
    else:
        flag = False
    return flag

