from PySide6 import QtCore, QtWidgets, QtGui

style = """
    background: transparent;
    font-size: 16px;
    font-weight: bold;
"""
### FUNCIONES AUXILIARES ###
def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())

### RENDER DE CADA MSJ ###
def create_msj_row(data):
    layout_msj = QtWidgets.QFrame()
    layout_msj.setStyleSheet(style)
    layout_msj.setContentsMargins(10, 10, 10, 10)

    container_msj = QtWidgets.QHBoxLayout(layout_msj)
    container_msj.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    container_msj.setContentsMargins(0, 0, 0, 0)

    username = QtWidgets.QLabel(data["username"])
    textMsj = QtWidgets.QLabel(data["textMsj"])

    if data["username"] == "Cobby":
        username.setStyleSheet(" bakcground: transparent; text-align: justify; ")
        textMsj.setStyleSheet(" background: white; color: black; border: 1px solid white; boder-radius: 12px; text-align: justify; ")

        container_msj.addWidget(username, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
        container_msj.addWidget(textMsj, alignment=QtCore.Qt.AlignmentFlag.AlignRight)
    else:
        username.setStyleSheet(" background: transparent; text-align: justify; ")
        textMsj.setStyleSheet(" background: gray; color: white; border: 1px solid gray; border-radius: 12px; text-align: justify; ")

        container_msj.addWidget(username, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)
        container_msj.addWidget(textMsj, alignment=QtCore.Qt.AlignmentFlag.AlignLeft)

    return layout_msj

def chat(subject):
    main_layout = QtWidgets.QVBoxLayout()
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    # -------------------------
    # SCROLL DE MENSAJES
    # -------------------------

    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)

    content = QtWidgets.QWidget()
    mesaje_rows = QtWidgets.QVBoxLayout(content)
    mesaje_rows.setContentsMargins(20, 20, 20, 20)
    mesaje_rows.setSpacing(10)

    # Agregar mensajes
    try:
        for msj in subject_msj:
            mesaje_rows.addWidget(create_msj_row(msj))
    except Exception as e:
        error = QtWidgets.QLabel("No hay mensajes para mostrar.")
        error.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        error.setStyleSheet(" background: transparent; color: white; border: none; font-size: 20px; font-weight: bold; padding: 30px; ")
        mesaje_rows.addWidget(error)
    # MUY IMPORTANTE
    mesaje_rows.addStretch()

    scroll_area.setWidget(content)

    main_layout.addWidget(scroll_area)


    # -------------------------
    # INPUT INFERIOR
    # -------------------------

    input_box = QtWidgets.QHBoxLayout()
    input_box.setContentsMargins(20, 10, 20, 20)
    input_box.setSpacing(10)

    input = QtWidgets.QLineEdit()
    input.setPlaceholderText("...")
    input.setFixedHeight(80)
    input.setStyleSheet("""
        background: white;
        color: black;
        border: 1px;
        border-radius: 12px;
        font-size: 22px;
        font-weight: bold;
    """)

    sendMsj = QtWidgets.QPushButton("SEND")
    sendMsj.setFixedWidth(100)
    sendMsj.setFixedHeight(100)
    sendMsj.setStyleSheet("""
        QPushButton {
        background: #009EDE;
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
        QPushButton:hover { background-color: #0075A3; }
        QPushButton:pressed { background-color: #003347; }
    """)

    input_box.addWidget(input, 4)
    input_box.addWidget(sendMsj, 1)

    main_layout.addLayout(input_box)

    container = QtWidgets.QWidget()
    container.setLayout(main_layout)

    return container