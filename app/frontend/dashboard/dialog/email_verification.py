from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QDialog

class verification(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Input Form")
        self.setFixedSize(700, 250)

        self.layout_primary = QtWidgets.QVBoxLayout(self)
        self.layout_primary.setContentsMargins(10, 10, 10, 10)
        self.layout_primary.setSpacing(10)

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
            # salto(self.input_code)
            if len(self.input_code.text()) >= 1:
                self.input_code.setFocus()

        # def salto(input_code):
        #     if len(self.inputs.text()) >= 1:
        #         self.inputs.setFocus()

        self.send = QtWidgets.QDialogButtonBox(QtWidgets.QDialogButtonBox.Ok | QtWidgets.QDialogButtonBox.Cancel)

        self.text.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        self.send.setStyleSheet("color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; border: 1px solid #5a5a5a; border-radius: 6px; min-width: 220px;")
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
        print("Se presiono el boton de enviar")
        code = "".join(input.text() for input in self.inputs)
        print(code)
        # if input == input:
        # return True
        # else:
            # return False