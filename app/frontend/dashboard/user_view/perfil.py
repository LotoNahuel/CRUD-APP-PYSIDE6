from PySide6 import QtWidgets, QtCore, QtGui

### FUNCIONES AUXILIARES ###
def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())

### RENDER USER PERFIL ###
def perfil(data):
    layout = QtWidgets.QFrame()
    layout.setContentsMargins(10, 10, 10, 10)
    layout.setStyleSheet(" border: 2px solid white; border-radius: 12px; ")
    # layout.setFixedHeight(550)
    layout.setFixedWidth(700)

    container = QtWidgets.QVBoxLayout(layout)
    container.setContentsMargins(10, 10, 10, 10)

    box = QtWidgets.QHBoxLayout()
    box.setContentsMargins(10, 10, 10, 10)

    box_subtitle = QtWidgets.QVBoxLayout()
    box_subtitle.setContentsMargins(10, 10, 10, 10)

    box_data = QtWidgets.QVBoxLayout()
    box_data.setContentsMargins(10, 10, 10, 10)

    tittle = QtWidgets.QLabel("USER DATA")
    tittle.setStyleSheet(" font-size: 30px; font-weight: bold; text-decoration: underline; border: none;")

    ### SUBTITLE ###
    labels = ["NAME", "LAST NAME", "BIRTHDATE", "PHONE NUMBER", "EMAIL", "PASSWORD"]

    ### DATA USER ###
    try:
        if data:
            name = QtWidgets.QLabel(data["first_name"] + data["second_name"])
            last_name = QtWidgets.QLabel(data["last_name"])
            birthdate = QtWidgets.QLabel(data["birthdate"])
            phone_number = QtWidgets.QLabel(data["phone"])
            email = QtWidgets.QLabel(data["email"])
            password = QtWidgets.QPushButton("EDIT PASSWORD")

            box_data.addWidget(name)
            box_data.addWidget(last_name)
            box_data.addWidget(birthdate)
            box_data.addWidget(phone_number)
            box_data.addWidget(email)
            box_data.addWidget(password)
        else:
            for label in labels:
                if label == "PASSWORD":
                    label = QtWidgets.QPushButton("EDIT PASSWORD")
                    label.setContentsMargins(0, 50, 0, 0)
                    label.setStyleSheet("""
                        QPushButton {
                            background: #009EDE;
                            padding: 10px;
                            color: white;
                            font-size: 16px;
                            font-weight: bold;
                            height: 60%;
                            border: none;
                        }
                        QPushButton:hover { background-color: #0075A3; }
                        QPushButton:pressed { background-color: #003347; }
                    """)
                    box_data.addWidget(label)
                else:
                    label = QtWidgets.QLabel("EMPTY")
                    label.setContentsMargins(0, 50, 0, 0)
                    label.setStyleSheet(" font-size: 20px; font-weight: bold; border: 1px; border-radius: 12px; ")
                    box_data.addWidget(label)
                
    except Exception as e:
        print(f"Error: {e}")
        empty = QtWidgets.QLabel("EMPTY")
        box_data.addWidget(empty)
        for label in labels:
            label =QtWidgets.QLabel("EMPTY")
            label.setContentsMargins(0, 50, 0, 0)
            box_data.addWidget(label)

    for label in labels:
        label = QtWidgets.QLabel(label)
        label.setStyleSheet(" font-size: 20px; font-weight: bold; border: 1px; border-radius: 12px; ")
        label.setContentsMargins(0, 50, 0, 0)
        box_subtitle.addWidget(label)

    container.addWidget(tittle)
    box.addLayout(box_subtitle, 4)
    box.addLayout(box_data, 4)
    container.addLayout(box)
    return layout