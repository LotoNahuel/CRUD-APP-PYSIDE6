import os
from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui
from ....utils import get_icon_path

projects_list = [
    {
        "id": 0,
        "subject_id": 0,
        "tittle": "Análisis de una obra literaria",
        "description": "Preparar un análisis breve sobre la obra vista en clase.",
        "objectives": [
            "Leer la obra asignada.",
            "Identificar personajes, tema y contexto.",
            "Redactar una conclusión personal.",
        ],
        "date_up": "05/08/2026",
        "expirate_date": "20/08/2026",
        "document_file": "guia_analisis_literario.pdf",
        "note": "5",
    },
    {
        "id": 1,
        "subject_id": 1,
        "tittle": "Línea de tiempo histórica",
        "description": "Crear una línea de tiempo con los hechos principales del período.",
        "objectives": [
            "Investigar cinco acontecimientos importantes.",
            "Ordenar los hechos cronológicamente.",
            "Agregar una fuente para cada acontecimiento.",
        ],
        "date_up": "01/08/2026",
        "expirate_date": "25/08/2026",
        "document_file": "consigna_linea_de_tiempo.pdf",
        "note": "3",
    },
    {
        "id": 2,
        "subject_id": 3,
        "tittle": "Resolución de problemas",
        "description": "Resolver ejercicios aplicando los contenidos de álgebra.",
        "objectives": [
            "Resolver los diez ejercicios.",
            "Mostrar el procedimiento de cada resultado.",
            "Comprobar las respuestas finales.",
        ],
        "date_up": "08/08/2026",
        "expirate_date": "30/08/2026",
        "document_file": "problemas_algebra.pdf",
        "note": "7",
    },
    {
        "id": 0,
        "subject_id": 0,
        "tittle": "Análisis de una obra literaria",
        "description": "Preparar un análisis breve sobre la obra vista en clase.",
        "objectives": [
            "Leer la obra asignada.",
            "Identificar personajes, tema y contexto.",
            "Redactar una conclusión personal.",
        ],
        "date_up": "05/08/2026",
        "expirate_date": "20/08/2026",
        "document_file": "guia_analisis_literario.pdf",
        "note": "",
    },
    {
        "id": 1,
        "subject_id": 1,
        "tittle": "Línea de tiempo histórica",
        "description": "Crear una línea de tiempo con los hechos principales del período.",
        "objectives": [
            "Investigar cinco acontecimientos importantes.",
            "Ordenar los hechos cronológicamente.",
            "Agregar una fuente para cada acontecimiento.",
        ],
        "date_up": "01/08/2026",
        "expirate_date": "25/08/2026",
        "document_file": "consigna_linea_de_tiempo.docx",
        "note": "",
    },
    {
        "id": 2,
        "subject_id": 3,
        "tittle": "Resolución de problemas",
        "description": "Resolver ejercicios aplicando los contenidos de álgebra.",
        "objectives": [
            "Resolver los diez ejercicios.",
            "Mostrar el procedimiento de cada resultado.",
            "Comprobar las respuestas finales.",
        ],
        "date_up": "08/08/2026",
        "expirate_date": "30/08/2026",
        "document_file": "problemas_algebra.pdf",
        "note": "",
    },
    {
        "id": 0,
        "subject_id": 0,
        "tittle": "Análisis de una obra literaria",
        "description": "Preparar un análisis breve sobre la obra vista en clase.",
        "objectives": [
            "Leer la obra asignada.",
            "Identificar personajes, tema y contexto.",
            "Redactar una conclusión personal.",
        ],
        "date_up": "05/08/2026",
        "expirate_date": "20/08/2026",
        "document_file": "guia_analisis_literario.pdf",
        "note": "",
    },
    {
        "id": 1,
        "subject_id": 1,
        "tittle": "Línea de tiempo histórica",
        "description": "Crear una línea de tiempo con los hechos principales del período.",
        "objectives": [
            "Investigar cinco acontecimientos importantes.",
            "Ordenar los hechos cronológicamente.",
            "Agregar una fuente para cada acontecimiento.",
        ],
        "date_up": "01/08/2026",
        "expirate_date": "25/08/2026",
        "document_file": "consigna_linea_de_tiempo.pdf",
        "note": "",
    },
    {
        "id": 2,
        "subject_id": 3,
        "tittle": "Resolución de problemas",
        "description": "Resolver ejercicios aplicando los contenidos de álgebra.",
        "objectives": [
            "Resolver los diez ejercicios.",
            "Mostrar el procedimiento de cada resultado.",
            "Comprobar las respuestas finales.",
        ],
        "date_up": "08/08/2026",
        "expirate_date": "30/08/2026",
        "document_file": "problemas_algebra.pdf",
        "note": "",
    },
]

style = """
        color: white;
        background: rgba(237, 237, 237, 20);
        border: 1px solid rgba(237, 237, 237, 80);
        border-radius: 12px;
        padding: 0, 10 px;
        text-align: center;
    """

style_label = """
        background: transparent;
        color: white;
        border: none;
        font-size: 18px;
        font-weight: bold;
    """

style_button = """
        QPushButton {
            background: #009EDE;
            padding: 10px;
            color: white;
            font-size: 20px;
            font-weight: bold;
        }
        QPushButton:hover { background-color: #0075A3; }
        QPushButton:pressed { background-color: #003347; }
    """

def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())

def create_projects_row(project):
    layout_proj = QtWidgets.QFrame()
    layout_proj.setStyleSheet(style)
    layout_proj.setContentsMargins(10, 10, 10, 10)

    container_proj = QtWidgets.QVBoxLayout(layout_proj)
    container_proj.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    container_proj.setSpacing(10)
    container_proj.setContentsMargins(0, 0, 0, 0)

    boxDocuments = QtWidgets.QHBoxLayout()
    boxDocuments.setSpacing(10)
    boxDocuments.setContentsMargins(0, 0, 0, 0)

    boxDate = QtWidgets.QHBoxLayout()
    boxDate = QtWidgets.QHBoxLayout()
    boxDate.setSpacing(10)
    boxDate.setContentsMargins(0, 0, 0, 0)

    boxFileUp = QtWidgets.QHBoxLayout()
    boxFileUp.setSpacing(10)
    boxFileUp.setContentsMargins(0, 0, 0, 0)

    if project != {""}:

        iconDoc = QtWidgets.QLabel()
        iconNameDoc = "pdf.png" if project["document_file"].split(".")[1] == "pdf" else "docx.png"
        iconDoc.setPixmap(QtGui.QPixmap(get_icon_path(iconNameDoc)).scaled(
            50,
            50,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        ))

        tittle = QtWidgets.QLabel(project["tittle"])
        description = QtWidgets.QLabel(project["description"])
        objectives_text = "\n".join(
            f"° {objective}"
            for objective in project["objectives"]
        )
        objectives = QtWidgets.QLabel(objectives_text)
        objectives.setWordWrap(True)
        document = QtWidgets.QLabel(project["document_file"])
        icon = QtWidgets.QLabel()
        icon_name = "pdf.png" if project["document_file"].split(".")[1] == "pdf" else "docx.png"
        icon.setPixmap(QtGui.QPixmap(get_icon_path(icon_name)).scaled(
            50,
            50,
            QtCore.Qt.AspectRatioMode.KeepAspectRatio,
            QtCore.Qt.TransformationMode.SmoothTransformation,
        ))
        download = QtWidgets.QPushButton()
        download.setIcon(QtGui.QIcon(get_icon_path("download.png")))
        download.setIconSize(QtCore.QSize(50, 50))
        create = QtWidgets.QLabel(f"CREADO EL : {project['date_up']}")
        expired = QtWidgets.QLabel(f"FECHA LIMITE : {project['expirate_date']}")

        if project["note"] == "":
            note = QtWidgets.QLabel("Note:   0 ")
        else:
            note = QtWidgets.QLabel(f"Note:   {project['note']} ")
            
        ### STYLE LABELS ###
        for label in (tittle, description, objectives, document, create, expired, note):
            label.setStyleSheet(style_label)
            label.setFixedHeight(50)

        tittle.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        note.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        create.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
        expired.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)
        tittle.setStyleSheet(" font-size: 26px; font-weight: bold; background: transparent; border: none;")
        note.setStyleSheet(" font-size: 22px; font-weight: bold; background: transparent; border: none; ")
        document.setStyleSheet(" border: 1px solid white; background: white; color: black; font-size: 20px; font-weight: bold; ")

        icon.setStyleSheet("background: transparent; border: none;")
        iconDoc.setStyleSheet("background: transparent; border: none; padding-left: 18px;")
        download.setStyleSheet("""
            QPushButton {
                background: #009EDE;
                padding: 10px;
                color: white;
                font-size: 16px;
                font-weight: bold;
                width: 150px;
                height: 30%;
            }
            QPushButton:hover { background-color: #0075A3; }
            QPushButton:pressed { background-color: #003347; }
        """)

        ### SELEC FILE ###
        label_file = QtWidgets.QLabel("SIN SELECIONAR")
        button_file = QtWidgets.QPushButton("SELECCIONAR ARCHIVO")
        button_send = QtWidgets.QPushButton("SUBIR ARCHIVO")

        ### STYLE SELEC FILE ###
        label_file.setStyleSheet("background: white; color: black; font-size: 20px; font-weight: bold; padding: 5px; ")
        label_file.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        button_file.setStyleSheet(style_button)
        button_send.setStyleSheet(style_button)
        
        ### CONDITION FILE ###
        def select_file():
            file_path = QtWidgets.QFileDialog.getOpenFileName(
                layout_proj,
                "Seleccionar archivo",
                "",
                "Documentos (*.pdf *.docx);"
            )

            if file_path != ("",""):
                print(file_path)
                label_file.setText(os.path.basename(file_path[0]))
            else:
                pass

        button_file.clicked.connect(select_file)


        container_proj.addWidget(tittle)
        container_proj.addWidget(note)
        container_proj.addWidget(description)
        container_proj.addWidget(objectives)
        boxDocuments.addWidget(iconDoc)
        boxDocuments.addWidget(document, 4)
        boxDocuments.addWidget(download, 1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        boxDate.addWidget(create)
        boxDate.addWidget(expired)
        boxFileUp.addWidget(label_file, 4)
        boxFileUp.addWidget(button_file, 1)
        container_proj.addLayout(boxDocuments)
        container_proj.addLayout(boxDate)
        container_proj.addLayout(boxFileUp)
        container_proj.addWidget(button_send)

    else:
        empty = QtWidgets.QLabel("Todavia no hay nuevos proyectos a entregar.")
        empty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet(" background: transparent; border: none; text-align: center; font-size: 26px; font-weight: bold; ")

        container_proj.addWidget(empty)

    return layout_proj

def projects(data):
    print(data)
    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    )
    scroll_area.setStyleSheet("""
        QScrollArea { background: transparent; border: none; margin-right: 5px; }
        QScrollBar::handle:horizontal { background: #555; border-radius: 5px; }
        QScrollBar:vertical { width: 10px; background: transparent; }
        QScrollBar::handle:vertical { background: #555; border-radius: 5px; }
    """)

    content = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(content)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(10)

    subject_projects = [
        project for project in projects_list
        if project["subject_id"] == data["id"]
    ]

    project_rows = QtWidgets.QVBoxLayout()
    project_rows.setSpacing(10)

    if len(subject_projects) == 0:
        project_rows.addWidget(create_projects_row({""}))
    else:
        for project in subject_projects:
            project_rows.addWidget(create_projects_row(project))
    project_rows.addStretch(1)

    layout.addLayout(project_rows)
    scroll_area.setWidget(content)

    return scroll_area
