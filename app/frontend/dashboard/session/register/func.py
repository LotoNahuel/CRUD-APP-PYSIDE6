import re
from email_validator import validate_email, EmailNotValidError

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
    password = ""
    confirm_password = ""
    fields = {}

    try:
        for label_widget, input_widget in data:
            label = label_widget.text()
            fields[label] = input_widget
            text = input_widget.text()

            if label == "Email":
                email = text
            elif label == "Password":
                password = text
            elif label == "Confirm Password":
                confirm_password = text

            if text == "":
                set_input_style(input_widget, False)
                c += 1
            else:
                set_input_style(input_widget, True)

        if email and not email_review(email):
            set_input_style(fields.get("Email"), False)
            c += 1

        if not password_validator(password, confirm_password):
            set_input_style(fields.get("Password"), False)
            set_input_style(fields.get("Confirm Password"), False)
            c += 1
        else:
            set_input_style(fields.get("Password"), True)
            set_input_style(fields.get("Confirm Password"), True)

        return c == 0
    except Exception as e:
        print(f"Error al verificar los datos: {e}")
        return False


def email_review(email):
    email = email.strip()
    try:
        validate_email(email)
        return True
    except EmailNotValidError as e:
        print("Correo invalido:", str(e))
        return False


def password_validator(password, confirm_password):
    if password != confirm_password:
        print("Las contraseñas son diferentes. Intente nuevamente.")
        return False

    reg = r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$#%])[A-Za-z\d@$#%]{8,20}$"
    if not re.search(reg, password):
        print(
            "La contraseña debe tener minimo 8 caracteres, un signo, una minuscula y/o una mayuscula "
            "y/o un numero: Ejemplo: fsaT15-685"
        )
        return False

    return True
