from PySide6 import QtWidgets, QtCore
from .parts.documents import documents
from .parts.projects import projects
from .parts.exams import exams
from .parts.notes import notes
from .parts.chat import chat

def view(self, sub):
    self.body = QtWidgets.QVBoxLayout()
    self.body.setContentsMargins(0, 0, 0, 0)
    self.body.setSpacing(0)

    self.container_subject = QtWidgets.QWidget()
    self.container_subject.setFixedHeight(80)
    self.container_subject.setStyleSheet("""
        border-bottom: 1px solid rgba(237, 237, 237, 0.2);
    """)

    self.box_navbar = QtWidgets.QHBoxLayout(self.container_subject)
    self.box_navbar.setContentsMargins(0, 0, 0, 0)
    self.box_navbar.setSpacing(0)

    self.box_container = QtWidgets.QHBoxLayout()
    self.box_container.setContentsMargins(0, 0, 0, 0)
    self.box_container.setSpacing(0)

    self.button_nav = []
    def setStyleButton(label, active=False):
        if active:
            label.setStyleSheet("""
                QPushButton {
                    background: #363636;
                    color: white;
                    font-size: 20px;
                    font-family: Arial;
                    font-weight: bold;
                    text-align: center;
                    border: none;
                    border-radius: 12px;
                    padding: 12px;
                    margin: 10px;
                }
                QPushButton:hover { background-color: rgba(237, 237, 237, 0.2); }
                QPushButton:pressed { background-color: #003F6B; }
            """)
        else:
            label.setStyleSheet("""
                QPushButton {
                    background: transparent;
                    color: white;
                    font-size: 20px;
                    font-family: Arial;
                    font-weight: bold;
                    text-align: center;
                    border: none;
                    border-radius: 12px;
                    padding: 12px;
                    margin: 10px;
                }
                QPushButton:hover { background-color: rgba(237, 237, 237, 0.2); }
                QPushButton:pressed { background-color: #003F6B; }
            """)

    def set_active_navbar(active_button):
        """Deja activo solo el botón que se acaba de presionar."""
        for button in self.button_nav:
            setStyleButton(button, button is active_button)
        # Los estilos de los botones no activos ya se restablecieron arriba.
        return

    self.navbarLabels = ["DOCUMENTS", "PROJECTS", "EXAMS", "NOTES", "CHAT"]

    for label in enumerate(self.navbarLabels):
        navbar = QtWidgets.QPushButton(label[1])
        navbar.setFixedHeight(80)
        navbar.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Expanding,
            QtWidgets.QSizePolicy.Policy.Fixed,
        )
        setStyleButton(navbar, label[0] == 0)
        try:
            navbar.clicked.connect(
                lambda checked=False,
                s={'id': sub['id'], 'name': sub['name'], 'label': label[1]},
                button=navbar: (set_active_navbar(button), change_view(s))
            )
        except Exception as e:
            print("Error al conectar la señal del botón:", e)

        self.box_navbar.addWidget(navbar)
        self.button_nav.append(navbar)

    def clear_layout(layout):
        while layout.count():
            item = layout.takeAt(0)
            if item.widget():
                item.widget().deleteLater()
            elif item.layout():
                clear_layout(item.layout())
    
    def change_view(label):
        try:
            clear_layout(self.box_container)
            str = {'id': label['id'], 'name': label['name'].lower()}
            match label['label'].lower():
                case "documents":
                    cleanView = documents(str)
                    self.box_container.addWidget(cleanView)
                    return True
                case "projects":
                    cleanView = projects(str)
                    self.box_container.addWidget(cleanView)
                    return True
                case "exams":
                    cleanView = exams(str)
                    self.box_container.addWidget(cleanView)
                case "notes":
                    cleanView = notes(str)
                    self.box_container.addWidget(cleanView)
                case "chat":
                    cleanView = chat(str)
                    self.box_container.addWidget(cleanView)
        except Exception as e:
            print("Error al cambiar la vista:", e)

    str = {'id': sub['id'], 'name': sub['name']}
    cleanView = documents(str)
    self.box_container.addWidget(cleanView)
    self.body.addWidget(self.container_subject)
    self.body.addLayout(self.box_container, 1)

    return self.body
