from PySide6 import QtCore, QtWidgets
from PySide6.QtWidgets import QMessageBox
from .func import verify_data
from ...index import IndexApp

class Login(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.index_window = None

        self.setStyleSheet("background-color: #080707;")

        self.layout_primary = QtWidgets.QVBoxLayout(self)
        self.layout_primary.setContentsMargins(24, 24, 24, 24)
        self.layout_primary.setSpacing(20)

        self.header = QtWidgets.QHBoxLayout()
        self.header.setContentsMargins(0, 0, 0, 0)
        self.title = QtWidgets.QLabel("SCHOOL APP")
        self.title.setStyleSheet("color: white; font-family: Arial; font-weight: bold; font-size: 24px;")
        self.header.addWidget(self.title, alignment=QtCore.Qt.AlignLeft | QtCore.Qt.AlignTop)
        self.header.addStretch()

        ### #2b2b2b
        self.card = QtWidgets.QWidget(self)
        self.card.setObjectName("card")
        self.card.setStyleSheet("""
            #card {
                background-color: #2a2b2b;
                border: 5px solid #dbdbdb;
                border-radius: 16px;
            }
        """)
        self.card.setFixedSize(560, 300)

        self.card_layout = QtWidgets.QVBoxLayout(self.card)
        self.card_layout.setContentsMargins(32, 28, 32, 28)
        self.card_layout.setSpacing(16)

        self.subtitle = QtWidgets.QLabel("Login")
        self.subtitle.setStyleSheet("color: white; font-family: Arial; font-size: 22px; font-weight: bold; background-color: #2a2b2b;")
        self.subtitle.setAlignment(QtCore.Qt.AlignCenter)

        self.form_layout = QtWidgets.QGridLayout()
        self.form_layout.setHorizontalSpacing(12)
        self.form_layout.setVerticalSpacing(16)
        self.form_layout.setColumnStretch(1, 1)

        labels = ["Email", "Password"]

        self.entries = []
        def magic(entry):
            if entry.echoMode() == QtWidgets.QLineEdit.Password:
                entry.setEchoMode(QtWidgets.QLineEdit.Normal)
            else:
                entry.setEchoMode(QtWidgets.QLineEdit.Password)
        for row, label in enumerate(labels):
            label_widget = QtWidgets.QLabel(label)
            label_widget.setStyleSheet("color: #e6e6e6; font-size: 16px; background-color: #2a2b2b;")
            label_widget.setAlignment(QtCore.Qt.AlignLeft | QtCore.Qt.AlignVCenter)
            label_widget.setMinimumWidth(140)

            entry = QtWidgets.QLineEdit()
            entry.setPlaceholderText(label)
            entry.setStyleSheet("color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; border: 1px solid #5a5a5a; border-radius: 6px; min-width: 220px;")
            show_button = QtWidgets.QPushButton("SHOW")
            show_button.setFixedWidth(70)
            show_button.setStyleSheet("""
                QPushButton {
                    color: white;
                    font-size: 16px;
                    padding: 10px;
                    background-color: #007ACC;
                    border: none;
                    border-radius: 8px;
                }
                QPushButton:hover {
                    background-color: #005A9E;
                }
                QPushButton:pressed {
                    background-color: #003F6B;
                }
            """)
            if label == "Password":
                entry.setPlaceholderText("********")
                entry.setEchoMode(QtWidgets.QLineEdit.Password)
                entry.setFixedWidth(100)
                show_button.clicked.connect(lambda checked, e=entry: magic(e))
            elif label == "Email":
                entry.setPlaceholderText("email@example.com")
            else:
                pass

            self.form_layout.addWidget(label_widget, row, 0, alignment=QtCore.Qt.AlignRight | QtCore.Qt.AlignVCenter)
            self.form_layout.addWidget(entry, row, 1)
            if label == "Password":
                self.form_layout.addWidget(show_button, row, 1, alignment=QtCore.Qt.AlignRight)
                
            self.entries.append((label_widget, entry))
        
        self.button = QtWidgets.QPushButton("SAVE")
        self.button.setFixedWidth(220)
        self.button.setStyleSheet("""
            QPushButton {
                color: white;
                font-size: 16px;
                padding: 10px;
                background-color: #007ACC;
                border: none;
                border-radius: 8px;
            }
            QPushButton:hover {
                background-color: #005A9E;
            }
            QPushButton:pressed {
                background-color: #003F6B;
            }
        """)

        self.message = QtWidgets.QLabel("")
        self.message.setStyleSheet("color: #bbbbbb; font-size: 13px; background-color: #2a2b2b;")
        self.message.setAlignment(QtCore.Qt.AlignCenter)

        self.card_layout.addWidget(self.subtitle)
        self.card_layout.addLayout(self.form_layout)
        self.card_layout.addWidget(self.button, alignment=QtCore.Qt.AlignCenter)
        self.card_layout.addWidget(self.message, alignment=QtCore.Qt.AlignCenter)

        self.layout_primary.addLayout(self.header)
        self.layout_primary.addWidget(self.card, alignment=QtCore.Qt.AlignCenter)
        self.layout_primary.addStretch()

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        boolean, message = verify_data(self.entries)
        if boolean == True:
            self.message.setText("")
            self.redirect_to_index()
        else:
            QMessageBox.information(self, "Information", message)

    def redirect_to_index(self):
        self._clear_layout(self.layout_primary)
        self.index_window = IndexApp()
        self.index_window.setParent(self)
        self.layout_primary.setContentsMargins(0, 0, 0, 0)
        self.layout_primary.setSpacing(0)
        self.layout_primary.addWidget(self.index_window)

    def _clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()
            child_layout = item.layout()

            if widget is not None:
                widget.setParent(None)
                widget.deleteLater()
            elif child_layout is not None:
                self._clear_layout(child_layout)
