import os
from backend.data.connect import get_validate_email

def validate_data(data):
    dataDb = get_validate_email(data["email"])

    try:
        if dataDb["token"] == data["token"]:
            return True, "Verificado correctamente"
    except Exception as e:
        print(f"Error: al verificar el email: {e}")
        return False, "Error al verificar el token"