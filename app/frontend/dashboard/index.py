import random
from PySide6 import QtCore, QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QLabel, QVBoxLayout, QHBoxLayout, QGridLayout, QLineEdit, QPushButton
from .index_view.subject import view
from .user_view.perfil import perfil
from ..utils import get_icon_path

userList = [
    {"id": 0, "firstName": "Marcelo", "lastName": "Quinteros"},
    {"id": 1, "firstName": "Fernando", "lastName": "Gago"},
    {"id": 2, "firstName": "Lionel", "lastName": "Messi"}
]
subjectList = [
    {"id": 0, "name": "Literature", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"},
    {"id": 1, "name": "History", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"},
    {"id": 2, "name": "Geography", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"},
    {"id": 3, "name": "Math", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"},
    {"id": 4, "name": "Physics", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"},
    {"id": 5, "name": "Sciences", "grade": 1, "init": "5/3/2026", "finish": "10/12/2026"}
]
teacherList = [
    {"id": 0, "user_id": 0, "subject_id": 0},
    {"id": 1, "user_id": 2, "subject_id": 1},
    {"id": 2, "user_id": 1, "subject_id": 2},
    {"id": 3, "user_id": 1, "subject_id": 3},
    {"id": 4, "user_id": 0, "subject_id": 4},
    {"id": 5, "user_id": 2, "subject_id": 5}
]

class IndexApp(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.setStyleSheet("background-color: #080707;")
        self.layout_primary = QtWidgets.QHBoxLayout(self)
        self.layout_primary.setContentsMargins(0, 0, 0, 0)
        self.layout_primary.setSpacing(0)

        # Caja izquierda: siempre mide 200 px de ancho.
        self.left_container = QtWidgets.QWidget()
        self.left_container.setFixedWidth(250)
        self.left_container.setStyleSheet(
            "border-right: 1px solid rgba(237, 237, 237, 0.2);"
        )
        self.left_layout = QtWidgets.QVBoxLayout(self.left_container)
        self.left_layout.setContentsMargins(0, 0, 0, 0)
        self.left_layout.setSpacing(0)

        self.top_buttons = QtWidgets.QVBoxLayout()
        self.top_buttons.setContentsMargins(10, 0, 10, 0)
        self.top_buttons.setSpacing(0)

        # Caja inferior: contiene OPTIONS y USER en una sola fila.
        self.bottom_container = QtWidgets.QFrame()
        self.bottom_container.setObjectName("bottomContainer")
        self.bottom_container.setStyleSheet("""
            QFrame#bottomContainer {
                background-color: transparent;
                margin: 10px;
                border: 2px solid rgba(237, 237, 237, 0.2);
                border-radius: 18px;
            }
        """)
        self.bottom_buttons = QtWidgets.QHBoxLayout(self.bottom_container)
        self.bottom_buttons.setContentsMargins(6, 6, 6, 6)
        self.bottom_buttons.setSpacing(0)
        
        self.buttons = []
        self.sidebar_buttons = []

        def set_button_style(button, active=False):
            compact = button.property("compact")
            background = "#363636" if active else "transparent"
            font_size = "15px" if compact else "20px"
            padding = "0 10px" if compact else "0 12px"
            margin = "0" if compact else "10px 0 0 0"

            button.setStyleSheet(f"""
                QPushButton {{
                    color: white;
                    font-size: {font_size};
                    font-family: Arial;
                    font-weight: bold;
                    background: {background};
                    border: none;
                    border-radius: 12px;
                    text-align: left;
                    padding: {padding};
                    margin: {margin};
                }}
                QPushButton:hover {{ background-color: rgba(237, 237, 237, 0.2); }}
                QPushButton:pressed {{ background-color: #454545; }}
            """)

        def set_active_sidebar(active_button):
            for button in self.sidebar_buttons:
                set_button_style(button, button is active_button)

        def create_button(text, icon_path=None, compact=False, active=False):
            button = QtWidgets.QPushButton(text)
            button.setProperty("compact", compact)
            button.setFixedHeight(40 if compact else 70)
            button.setSizePolicy(
                QtWidgets.QSizePolicy.Policy.Expanding,
                QtWidgets.QSizePolicy.Policy.Fixed,
            )
            if icon_path:
                icon = QtGui.QIcon(icon_path)
                button.setIcon(icon)
                button.setIconSize(QtCore.QSize(28 if compact else 40, 28 if compact else 40))

            set_button_style(button, active)
            return button

        for i, subject in enumerate(subjectList):
            label_button = create_button(
                subject["name"],
                get_icon_path(f"{subject['name']}.png"),
                active=i == 0,
            )
            label_button.clicked.connect(
                lambda checked=False, s=subject, button=label_button:
                    (set_active_sidebar(button), self.updateView(s))
            )
            self.top_buttons.addWidget(label_button)
            self.buttons.append(label_button)
            self.sidebar_buttons.append(label_button)

        data = {}
        current_user = userList[0]
        self.button_user = create_button(
            f"{current_user['firstName']} {current_user['lastName']}",
            get_icon_path("account.png"),
            compact=True,
        )
        self.sidebar_buttons.append(self.button_user)
        self.button_user.clicked.connect(
            lambda: (set_active_sidebar(self.button_user), self.append_view(perfil(data)))
        )

        self.button_config = create_button(
            "",
            get_icon_path("settings.png"),
            compact=True,
        )
        self.button_config.setFixedWidth(70)
        self.sidebar_buttons.append(self.button_config)
        self.button_config.clicked.connect(
            lambda: (set_active_sidebar(self.button_config), self.show_message("Opciones"))
        )
        self.bottom_buttons.addWidget(self.button_user)
        self.bottom_buttons.addWidget(self.button_config, 1)

        self.left_layout.addLayout(self.top_buttons)
        self.left_layout.addStretch(1)
        self.left_layout.addWidget(self.bottom_container)


        ### CONTIANER RIGHT ###
        sub = list(subjectList)[0]
        container_subject = view(self, sub)

        # Caja derecha: ocupa todo el espacio restante.
        self.right_container = QtWidgets.QWidget()
        self.right_layout = QtWidgets.QVBoxLayout(self.right_container)
        self.right_layout.setContentsMargins(24, 24, 24, 24)
        self.right_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        self.right_layout.setContentsMargins(0, 0, 0, 0)
        self.right_layout.setSpacing(0)
        self.right_layout.addLayout(container_subject)

        self.layout_primary.addWidget(self.left_container)
        self.layout_primary.addWidget(self.right_container, 1)

    def clear_layout(self, layout):
        while layout.count():
            item = layout.takeAt(0)
            widget = item.widget()

            if widget:
                widget.deleteLater()
            elif item.layout():
                self.clear_layout(item.layout())

    def updateView(self, subject):
        sub = subjectList[subject["id"]]
        self.clear_layout(self.right_layout)
        cleanView = view(self, sub)
        self.right_layout.addLayout(cleanView)

    def show_message(self, message):
        self.clear_layout(self.right_layout)
        label = QtWidgets.QLabel(message)
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        label.setStyleSheet("color: white; font-size: 22px;")
        self.right_layout.addWidget(label)

    def append_view(self, view):
        self.clear_layout(self.right_layout)
        self.right_layout.addWidget(view)
        self.right_layout.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)


### codex resume 019f6c18-c31c-7710-bcd7-804bb9074735
