import sqlite3
import os

def get_connection():
    try:
        connection = sqlite3.connect("../db/database.db")
        connection.execute("PRAGMA foreign_keys = ON")
        return connection
    except Exception as e:
        print(f"Error al conectar con la base de datos.\nERROR: {e}")

### IF NOT DB ###
def create_tables():
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.executescript("""
                CREATE TABLE IF NOT EXISTS user (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    first_name TEXT NOT NULL,
                    second_name TEXT,
                    last_name TEXT NOT NULL,
                    birthdate TEXT NOT NULL,
                    phone NUMERIC NOT NULL UNIQUE,
                    email TEXT NOT NULL UNIQUE,
                    password TEXT NOT NULL,
                    create_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS teacher (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    firts_name TEXT NOT NULL,
                    secon_name TEXT,
                    last_name TEXT NOT NULL,
                    birthdate TEXT NOT NULL,
                    phone NUMERIC NOT NULL,
                    email TEXT NOT NULL,
                    create_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS student_subjects (
                    userId INTEGER NOT NULL,
                    subjectId INTEGER NOT NULL,
                    create_at TEXT NOT NULL,

                    PRIMARY KEY (userId, subjectId),

                    FOREIGN KEY (userId) REFERENCES user(id),
                    FOREIGN KEY (subjectId) REFERENCES subject(id)
                );
                CREATE TABLE IF NOT EXISTS session (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    userId INTEGER NOT NULL,
                    token TEXT NOT NULL UNIQUE,
                    device_info TEXT NOT NULL UNIQUE,
                    ip TEXT NOT NULL UNIQUE,
                    create_at TEXT NOT NULL,
                    expired_at TEXT NOT NULL
                );
                CREATE TABLE IF NOT EXISTS email_validation (
                    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                    email TEXT NOT NULL UNIQUE,
                    token TEXT NOT NULL UNIQUE,
                    create_at TEXT NOT NULL,
                    expired_at TEXT NOT NULL
                );
            """)
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

create_tables()

### COMMIT USER ###
def create_user(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO user (first_name, second_name, last_name, birthdate, phone, email, password, create_at)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (data["First Name"], data["Second Name"], data["Last Name"], data["Birth Date"], data["Phone Number"], data["Email"], data["Password"], data["Create At"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def create_student(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO student (id, create_at)
                VALUES (?, ?)
            ''', (data["id"], data["Create At"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def verify_email(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT email FROM user WHERE email = ?",
                    (data,)
            )
            email = cursor.fetchone()
            if email is not None:
                return True, "El email ya se encuentra registrado."
            else:
                return False, "Correcto"
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False, "Error al verificar los datos intente nuevamente en unos minutos."
        finally:
            cursor.close()

def createValidate_email(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO email_validation (email, token, create_at, expired_at)
                VALUES (?, ?, ?, ?)
            ''', (data["email"], data["token"], data["create_at"], data["expire_at"]))
            connection.commit()
            return True, "Datos subidos correctamente."
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False, "Error al subir los datos de la validacion del email."
        finally:
            cursor.close()

def get_validate_email(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM email_validation WHERE email = ?",
                    (data,)
            )
            get_data = cursor.fetchone()
            return get_data, True
        except sqlite3.IntegrityError as e:
            print(f"Error al recuperar los datos de validacion de email: {e}")
            return False, "Error al obtener los datos."
        finally:
            cursor.close()

def verify_phone(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT phone FROM user WHERE phone = ?",
                    (data,)
            )
            phone = cursor.fetchone()
            if phone is not None:
                return True, "El Nro. de celular ya se encuentra registrado en otra cuenta."
            else:
                return False, "Correcto"
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False, "Error al verificar los datos intente nuevamente en unos minutos."
        finally:
            cursor.close()

def edit_password(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET password = ? WHERE email = ?",
                    (data["password"], data["email"])
            )
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def edit_email(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE users SET email = ? WHERE userId = ?",
                    (data["email"], data["userId"])
            )
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(F"Database error: {e}")
            return False
        finally:
            cursor.close()

def create_superUser(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO superUser (idUser, create_at)
                VALUES (?, ?)
            ''', (data["userId"], data["create_at"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database Error: {e}")
            return False
        finally:
            cursor.close()

### COMMIT SUBJECT ###
def create_subject(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO subjects (name, grade, userId, create_at)
                VALUES (?, ?, ?, ?)
            ''', (data["name"], data["grade"], data["userId"], data["create_at"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database Error: {e}")
            return False
        finally:
            cursor.close()

def edit_subject(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "UPDATE subjects SET teacher = ? WHERE subjectId = ?",
                    (data["userId"], data["subjectId"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

### COMMIT INSCRIPTIONS ###
def student_inscription(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO studentSubject (subjectId, userId, create_at)
                VALUES (?, ?, ?)
            ''', (data["subjectId"], data["userId"], data["create_at"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

### COMMIT SESSION ###
def create_session(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute('''
                INSERT INTO session (userId, token_hashed, device_info, ip, create_at, expire_at)
                VALUES (?, ?, ?, ?)
            ''', (data["userId"], data["token"], data["device_info"], data["ip"], data["create_at"], data["expire_at"]))
            connection.commit()
            return True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def del_session_DB(hashed_token):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM sessions WHERE token_hash = ?",
                        (hashed_token,))
            connection.commit()
            return True
        except Exception as e:
            print("Error al eliminar la Session: ", e)
            return None
        finally:
            cursor.close()

### GET DATA ###
def user_login(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT password, id FROM user WHERE email = ?",
                    (data,)
            )
            userData = cursor.fetchone()
            return True, userData
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()
            
def session_id(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT userId FROM users WHERE email = ?",
                    (data["email"])
            )
            userId = cursor.fetchone()
            return userId, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_session(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM session WHERE userId = ?",
                    (data["userId"],)
            )
            dataS = cursor.fetchone()
            return dataS, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_user(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM users WHERE userId = ?",
                    (data["userId"],)
            )
            dataU = cursor.fetchone()
            return dataU, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_allSubjects():
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM subjects"
            )
            rows = cursor.fetchall()
            subjects = [dict(row) for row in rows]
            return subjects, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_subject(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM subjects WHERE subjectId = ?",
                    (data["subjectId"],)
            )
            dataS = cursor.fetchone()
            return dataS, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_allStudSub():
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM studentSubject"
            )
            rows = cursor.fetchall()
            studentSubjects = [dict(row) for row in rows]
            return studentSubjects, True
        except sqlite3.IntegrityError as e:
            print(f"Database Error: {e}")
            return False
        finally:
            cursor.close()

def get_withIdSubject(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELECT * FROM studentSubject WHERE subjectId = ?",
                    (data["subjectId"],)
            )
            rows = cursor.fetchall()
            studentSubjects = [dict(row) for row in rows]
            return studentSubjects, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()

def get_withIdStudent(data):
    with get_connection() as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "SELETCT * FROM studentSubject WHERE userId = ?",
                    (data["userId"],)
            )
            rows = cursor.fetchall()
            studentSubjects = [dict(row) for row in rows]
            return studentSubjects, True
        except sqlite3.IntegrityError as e:
            print(f"Database error: {e}")
            return False
        finally:
            cursor.close()