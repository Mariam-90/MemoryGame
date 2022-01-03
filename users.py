import firebase_admin
from firebase_admin import auth

def deletUser(uid):
    auth.delete_user(uid)