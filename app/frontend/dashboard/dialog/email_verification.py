from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

class verification(QDialog):
    def __init__(self):
        super().__init__()
        self.layout_primary = QtWidgets.QVBoxLayout()
        self.layout_primary.setContentsMargins(10, 10, 10, 10)
        self.layout_primary.setSpacing(10)

        self.box_text = QtWidgets.QHBoxLayout()
        self.box_text.setContentsMargins(0, 0, 0, 0)
        self.box_text.setSpacing(10)

        self.box_input = QtWidgets.QHBoxLayout()
        self.box_input.setContentsMargins(0, 0, 0, 0)
        self.box_input.setSpacing(10)

        self.text = QtWidgets.QLabel()
        self.input = QtWidgets.QLineEdit()
        self.send = QtWidgets.QPushButton("SEND")

        self.text.setText("Se a enviado un mail al correo ********************** con un codigo.\nIngrese el codigo para verificar su mail:\n(El codigo expira en 5 minutos)")
        self.input.setPlaceholderText("Fsr45BN1")

        self.box_text.addWidget(self.text)
        self.box_input.addWidget(self.input)
        self.box_input.addWidget(self.send)

        self.layout_primary.addLayout(self.box_text)
        self.layout_primary.addLayout(self.box_input)

        