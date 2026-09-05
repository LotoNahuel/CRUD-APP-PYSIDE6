import hashlib
import json
import os
import bcrypt
from ...data.connect import get_session, del_session_DB, user_login

SESSION_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "session.json")

def dataDB(data):
    try:
        dataS, success = get_session(data)
        if success and dataS:
            return dataS
        else:
            return None
    except Exception as e:
        print(f"Error retrieving session data: {e}")
        return None
    
def delete_session(token):
    try:
        with open(SESSION_PATH, "w") as f:
            json.dump({"token": ""}, f)
        if del_session_DB(token) == True:
            return True
    except IOError as e:
        print(f"Error deleting session: {e}")
        return False

def authSession():
    try:
        token = ""
        with open(SESSION_PATH, "r") as f:
            session_data = json.load(f)
            token = session_data.get("token")
        token_hashed = hashlib.sha256(token.encode()).hexdigest()
        data = dataDB(token_hashed)
        if data:
            if data["create_at"] < data["expire_at"]:
                return True
            else:
                delete_session(token)
                return False
        else:
            return False
    except IOError as e:
        print(f"Error reading session file: {e}")
        return False

def authLogin(data):
    try:
        print(data.get("email"), data.get("password"))
        dataDB, boolean = user_login(data.get("email"))
        if boolean == True and dataDB:
            if bcrypt.checkpw(data.get("password").encode(), dataDB["password"]):
                return True
            else:
                return False, "Email y/o contraseña incorrectos!!! Intente nuevamente."
        else:
            return False, "Email y/o contraseña incorrectos!!! Intente nuevamente."
    except Exception as e:
        return False, f"Error validating data: {e}"