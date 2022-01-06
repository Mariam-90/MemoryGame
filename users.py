import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth
from firebase_admin import firestore
import database

cred = credentials.Certificate("./serviceAccountKey.json")
firebase_admin.initialize_app(cred)
db = firestore.client()


def deletUser(uid):
    auth.delete_user(uid)


def saveGame(saveDifficulty, saveCategory, savePairs):
    data = {"user_id": database.get_user_id(), "save_difficulty": saveDifficulty, "save_category": saveCategory,
            "save_pairs": savePairs}
    db.colletion("games").document("player1").set(data)
