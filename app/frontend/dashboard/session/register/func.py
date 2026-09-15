import os
import json
import re
from datetime import datetime
from email_validator import validate_email, EmailNotValidError
from backend.auth.encrypt.hashed import hash_password
from backend.data.connect import create_user, verify_email, createValidate_email, verify_phone
# from backend.data.connect import verify_email
# from backend.data.connect import createValidate_email
# from backend.data.connect import verify_phone
from backend.auth.encrypt.token import email_token
from ...dialog.email_verification import verification

RED_STYLE = (
    "color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; "
    "border: 1px solid red; border-radius: 6px; min-width: 220px;"
)
NORMAL_STYLE = (
    "color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; "
    "border: 1px solid #5a5a5a; border-radius: 6px; min-width: 220px;"
)

def set_input_style(input_widget, is_valid):
    if input_widget is None:
        return
    input_widget.setStyleSheet(NORMAL_STYLE if is_valid else RED_STYLE)

def verify_data(data):
    c = 0
    email = ""
    phone_number = ""
    password = ""
    confirm_password = ""
    fields = {}
    save = {}

    try:
        for label_widget, input_widget in data:
            label = label_widget.text()
            fields[label] = input_widget
            text = input_widget.text()

            if label == "Email":
                email = text
            elif label == "Phone Number":
                phone_number = text
            elif label == "Password":
                password = text
            elif label == "Confirm Password":
                confirm_password = text

            if label != "Second Name" and text == "":
                set_input_style(input_widget, False)
                c += 1
            else:
                set_input_style(input_widget, True)

        if email and not email_review(email):
            set_input_style(fields.get("Email"), False)
            c += 1

        boolean, hashed_password = password_validator(password, confirm_password)
        if boolean is False:
            set_input_style(fields.get("Password"), False)
            set_input_style(fields.get("Confirm Password"), False)
            # c += 1
            return False, hashed_password
        else:
            set_input_style(fields.get("Password"), True)
            set_input_style(fields.get("Confirm Password"), True)

        
        if c == 0:
            boolPhone, msjPhone = verify_phone(phone_number)
            boolEmail, msjEmail = verify_email(email)
            if boolPhone:
                set_input_style(fields.get("Phone Number"), False)
                return False, msjPhone
            if boolEmail:
                set_input_style(fields.get("Email"), False)
                return False, msjEmail
            boolToken, msjToken = validateTokenMail(email)
            if boolToken:
                return True, hashed_password
            else:
                return False, msjToken
            # if save_data(data, hashed_password) == True:
            #                     return True, "Correcto"
            # else:
            #     return False, "Error al guardar los datos intente nuevamente."
            
        # return c == 0, "Datos incompletos o incorrectos. Por favor, revise los campos resaltados en rojo."
        return c == 0
    except Exception as e:
        print(f"Error al verificar los datos: {e}")
        return False, "Datos incompletos o incorrectos. Por favor, revise los campos resaltados en rojo."



def email_review(email):
    email_verify = email.strip()
    try:
        if validate_email(email_verify):
            return True

    except EmailNotValidError as e:
        print("Correo invalido:", str(e))
        return False


def password_validator(password, confirm_password):
    if password != confirm_password:
        # print("Las contraseñas son diferentes. Intente nuevamente.")
        return False, "Las contraseñas son diferentes. Intente nuevamente."

    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{8,20}$"
    if not re.search(reg, password):
        print(
            "La contraseña debe tener minimo 8 caracteres, un signo, una minuscula y/o una mayuscula "
            "y/o un numero: Ejemplo: fsaT15-685"
        )
        return False, "La contraseña debe tener minimo 8 caracteres:\nun signo, una minuscula y/o una mayuscula y/o un numero: Ejemplo: fsaT15-685"

    hashed_password = hash_password(password)
    if hashed_password == "":
        return False, "Error Terrible"
    return True, hashed_password

def validateTokenMail(email):
    data_token = email_token()
    send_data = {"email" : email} | data_token

    ruta = os.path.abspath(os.path.join(
        os.path.dirname(__file__),
        "..", "..", "..", "..",
        "backend", "auth", "encrypt", "verify_email.json",
    ))
    with open(ruta, "w") as f:
        json.dump({"email" : email}, f)

    # dialog = verification()
    if createValidate_email(send_data):
        return True, "Se ha enviado un correo de verificacion a su correo electronico, por favor ingrese el codigo para verificar su correo."
    else:
        return False, "Error al guardar el token de verificacion en la base de datos. Intente nuevamente."
        # if dialog:
        #     return True, "Correcto"
        # else:
        #     return False

# def save_data(data, hashed_password):
#     fields = {}
#     save = {}
#     for label_widget, input_widget in data:
#         label = label_widget.text()
#         fields[label] = input_widget
#         text = input_widget.text()

#         if label == "Confirm Password":
#             time = datetime.now()
#             save["Create At"] = time.strftime("%d/%m/%Y %H:%M:%S")
#             pass
#         elif label == "Password":
#             pass
#             save[label] = hashed_password
#         else:
#             save[label] = text
#     if create_user(save):
#         return True