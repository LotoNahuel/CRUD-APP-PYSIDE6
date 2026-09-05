import os
import platform
import secrets
import json
import hashlib
import socket

def session_token():
    try:
        token = os.urandom(32).hex()
        device_info = platform.node()
        ip = socket.gethostbyname(socket.gethostname())

        with open("auth/session.json", "w") as f:
            json.dump({"token": token}, f)

        token_hashed = hashlib.sha256(token.encode()).hexdigest()
        return True, token_hashed, device_info, ip 
    except IOError as e:
        print(f"Error writing token to file: {e}")
        return False

def email_token():
    token = secrets.token_hex(4)
    return token

if __name__ == "__main__":
    session_token()
    email_token()