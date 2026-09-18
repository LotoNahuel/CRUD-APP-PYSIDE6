import os
import json
import hashlib
import hmac
from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QDialog
from backend.data.connect import get_validate_email

style_button = """
        QPushButton {
            background: #009EDE;
            padding: 10px;
            color: white;
            font-size: 20px;
            font-weight: bold;
            width: 100px;
        }
        QPushButton:hover { background-color: #0075A3; }
        QPushButton:pressed { background-color: #003347; }
    """

class verification(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input Form")
        self.setFixedSize(700, 250)

        self.layout_primary = QtWidgets.QVBoxLayout(self)
        self.layout_primary.setContentsMargins(10, 10, 10, 10)
        self.layout_primary.setSpacing(10)
        self.layout_primary.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.box_text = QtWidgets.QHBoxLayout()
        self.box_text.setContentsMargins(0, 0, 0, 0)
        self.box_text.setSpacing(10)
        self.box_text.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.box_input = QtWidgets.QHBoxLayout()
        self.box_input.setContentsMargins(0, 0, 0, 0)
        self.box_input.setSpacing(10)

        self.box_button = QtWidgets.QHBoxLayout()
        self.box_button.setContentsMargins(0, 0, 0, 0)
        self.box_button.setSpacing(10)
        self.box_button.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)

        self.inputs = []
        self.text = QtWidgets.QLabel()
        for i in range(6):
            self.input_code = QtWidgets.QLineEdit()
            self.input_code.setMaxLength(1)
            self.input_code.setFixedSize(60, 60)
            self.input_code.setStyleSheet("background-color: white; color: black; font-size: 28px; padding: 10px; border: 1px; border-radius: 12px;")
            self.input_code.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
            self.inputs.append(self.input_code)
            self.box_input.addWidget(self.input_code)

        for j in range(len(self.inputs) - 1):
            actual = self.inputs[j]
            nextt = self.inputs[j + 1]
            
            actual.textChanged.connect(
                lambda _, c_act=actual, c_sig=nextt: self.salto(c_act, c_sig)
            )

        self.send = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)
        self.send.setStyleSheet(style_button)

        self.text.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.text.setText("Se a enviado un mail al correo ********************** con un codigo.\nIngrese el codigo para verificar su mail:\n(El codigo expira en 5 minutos)")

        self.box_text.addWidget(self.text)
        self.box_button.addWidget(self.send)
        self.layout_primary.addLayout(self.box_text)
        self.layout_primary.addLayout(self.box_input)
        self.layout_primary.addLayout(self.box_button)

        self.send.accepted.connect(self.magic)
        self.send.rejected.connect(self.reject)

    @QtCore.Slot()
    def magic(self):
        code = "".join(input.text() for input in self.inputs)
        if os.path.exists("backend/auth/encrypt/verify_email.json"):
            with open("backend/auth/encrypt/verify_email.json", "r") as f:
                data = json.load(f)
            print(f"Email : {data['email']}")
            boolean, get_data = get_validate_email(data['email'])
            if boolean:
                print(f"DATA TOKEN DB: {get_data[2]}")
                hash_code = hashlib.sha256(code.encode('utf-8')).hexdigest()
                if hmac.compare_digest(hash_code, get_data[2]):
                    print("COMPARACION, CORRECTA")
                    self.accept()
                else:
                    print("No hay coincidencia")
                    return False
            else:
                print(boolean)
                print("No hay Booleano o es False")
                return False
        else:
            print("NO EXISTE LA RUTA")
            return False

    @QtCore.Slot()
    def salto(self, c_act, c_sig):
        if len(c_act.text()) >= c_act.maxLength():
            c_sig.setFocus()