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


class System:
    def __init__(self):
        self.__dic={}

    def new_accunt(self,username,password):
        if username not in self.__dic:
            self.__dic[username] = password
            print("Registered successfully")

        else:
            print("Username is already registered")

    def login(self,username,password):
        if username in self.__dic:
            if self.__dic[username] == password:
                print("Login successfully")
            else:
                print("Wrong password")
        else:
            print("there's no username such as that")