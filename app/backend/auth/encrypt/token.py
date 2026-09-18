import os
import platform
import secrets
import json
import hashlib
import socket
from datetime import datetime, timedelta

def session_token():
    try:
        token = os.urandom(32).hex()
        device_info = platform.node()
        ip = socket.gethostbyname(socket.gethostname())

        with open("auth/session.json", "w") as f:
            json.dump({"token": token}, f)

        token_hashed = hashlib.sha256(token.encode('utf-8')).hexdigest()
        return True, token_hashed, device_info, ip 
    except IOError as e:
        print(f"Error writing token to file: {e}")
        return False

def email_token():
    token = secrets.token_hex(3)
    print(token)
    token_hashed = hashlib.sha256(token.encode('utf-8')).hexdigest()

    create_at = datetime.now()
    expire_at = create_at + timedelta(minutes=5)

    data = {"token" : token, "token_hashed" : token_hashed, "create_at" : create_at, "expire_at" : expire_at}
    return data

if __name__ == "__main__":
    session_token()
    email_token()