import bcrypt

def hash_password(password: str) -> str:
    # Generate a salt
    salt = bcrypt.gensalt()
    
    try:
        if isinstance(password, str):
            # Hash the password with the salt
            hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
            
            # Return the hashed password as a string
            return hashed_password.decode('utf-8')
    except Exception as e:
        print(f"Error hashing password: {e}")
        return ""
    
def verifyPassword(passwordEncrypt, password_user: str) -> str:
    if isinstance(passwordEncrypt, str):
        passwordEncrypt = passwordEncrypt.encode()

    if bcrypt.checkpw(password_user.encode(), passwordEncrypt):
        # save_login(user_id)
        pass


if __name__ == "__main__":
    password = "my_secure_password"
    hashed = hash_password(password)
    print(f"Generated hash: {hashed}")