from datetime import datetime
from PySide6 import QtCore, QtWidgets, QtGui
from ....utils import get_icon_path


# Datos temporales: luego pueden venir de tu base de datos.
document_list = [
    {"id": 0, "subject_id": 0, "name": "Guía de lectura.pdf", "type": "PDF", "date_up": "26/07/2026"},
    {"id": 1, "subject_id": 0, "name": "Actividad 1.docx", "type": "DOCX", "date_up": "15/05/2026"},
    {"id": 2, "subject_id": 1, "name": "Línea de tiempo.pdf", "type": "PDF", "date_up": "5/03/2026"},
    {"id": 0, "subject_id": 0, "name": "Guía de lectura.pdf", "type": "PDF", "date_up": "26/07/2026"},
    {"id": 1, "subject_id": 0, "name": "Actividad 1.docx", "type": "DOCX", "date_up": "15/05/2026"},
    {"id": 2, "subject_id": 1, "name": "Línea de tiempo.pdf", "type": "PDF", "date_up": "5/03/2026"},
    {"id": 0, "subject_id": 0, "name": "Guía de lectura.pdf", "type": "PDF", "date_up": "26/07/2026"},
    {"id": 1, "subject_id": 0, "name": "Actividad 1.docx", "type": "DOCX", "date_up": "15/05/2026"},
    {"id": 2, "subject_id": 1, "name": "Línea de tiempo.pdf", "type": "PDF", "date_up": "5/03/2026"},
    {"id": 0, "subject_id": 0, "name": "Guía de lectura.pdf", "type": "PDF", "date_up": "26/07/2026"},
    {"id": 1, "subject_id": 0, "name": "Actividad 1.docx", "type": "DOCX", "date_up": "15/05/2026"},
    {"id": 2, "subject_id": 1, "name": "Línea de tiempo.pdf", "type": "PDF", "date_up": "5/03/2026"},
    {"id": 0, "subject_id": 0, "name": "Guía de lectura.pdf", "type": "PDF", "date_up": "26/07/2026"},
    {"id": 1, "subject_id": 0, "name": "Actividad 1.docx", "type": "DOCX", "date_up": "15/05/2026"},
    {"id": 2, "subject_id": 1, "name": "Línea de tiempo.pdf", "type": "PDF", "date_up": "5/03/2026"},
]

### Estilo de cada fila de documento ###
style = """
        color: white;
        font-size: 25px;
        font-weight: bold;
        text-align: left;
        padding-left: 18px;
        border: 1px solid rgba(237, 237, 237, 80);
        border-radius: 12px;
        background: rgba(237, 237, 237, 20);
    """

style_button = """
        QPushButton {
            background: #009EDE;
            padding: 10px;
            color: white;
            font-size: 16px;
            font-weight: bold;
            height: 30%;
        }
        QPushButton:hover { background-color: #0075A3; }
        QPushButton:pressed { background-color: #003347; }
    """

### FUNCIONES AUXILIARES ###
def clear_layout(layout):
    while layout.count():
        item = layout.takeAt(0)
        if item.widget():
            item.widget().deleteLater()
        elif item.layout():
            clear_layout(item.layout())

### RENDER DE CADA DOCUMENTO ###
def create_document_row(document):
    """Crea una fila de la lista de documentos."""
    layout_doc = QtWidgets.QFrame()
    layout_doc.setStyleSheet(style)
    layout_doc.setContentsMargins(10, 10, 10, 10)

    container_doc = QtWidgets.QHBoxLayout(layout_doc)
    container_doc.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    container_doc.setSpacing(10)
    container_doc.setContentsMargins(0, 0, 0, 0)

    icon = QtWidgets.QLabel()
    icon_name = "pdf.png" if document["type"] == "PDF" else "docx.png"
    icon.setPixmap(QtGui.QPixmap(get_icon_path(icon_name)).scaled(
        50,
        50,
        QtCore.Qt.AspectRatioMode.KeepAspectRatio,
        QtCore.Qt.TransformationMode.SmoothTransformation,
    ))

    name = QtWidgets.QLabel(document["name"])
    type_file = QtWidgets.QLabel(document["type"])
    date_up = QtWidgets.QLabel(document["date_up"])
    download = QtWidgets.QPushButton()
    download.setIcon(QtGui.QIcon(get_icon_path("download.png")))
    download.setIconSize(QtCore.QSize(50, 50))
    separator = QtWidgets.QLabel("|")

    for label in (name, type_file, date_up):
        label.setStyleSheet("background: transparent; color: white; font-size: 18px; font-weight: bold; border: none; text-align: left; padding-left: 10px;")
        label.setFixedHeight(60)

    icon.setStyleSheet("background: transparent; border: none;")
    separator.setStyleSheet("background: transparent; color: white; font-size: 18px; font-weight: bold; border: none; text-align: center; padding-left: 10px;")
    download.setStyleSheet(style_button)

    container_doc.addWidget(icon, 1)
    container_doc.addWidget(name, 4)
    container_doc.addWidget(separator)
    container_doc.addWidget(type_file, 1)
    container_doc.addWidget(date_up, 1)
    container_doc.addWidget(download, 1, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)

    return layout_doc

### FILTRAR DOCUMENTOS POR MATERIA ###
def documents(subject):
    """Devuelve la lista desplazable de documentos de una materia."""
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

    # Esta fila mantiene el título a la izquierda y el selector a la derecha.
    header = QtWidgets.QHBoxLayout()
    header.setContentsMargins(0, 0, 0, 0)
    title = QtWidgets.QLabel(f"Documentos de {subject['name']}")
    title.setStyleSheet("color: white; font-size: 22px; font-weight: bold;")
    filter_select = QtWidgets.QComboBox()
    filter_select.addItem("NEW", True)
    filter_select.addItem("OLDER", False)
    filter_select.setFixedWidth(190)
    filter_select.setStyleSheet("""
        QComboBox {
            color: white;
            background: transparent;
            border: 1px solid rgba(237, 237, 237, 80);
            border-radius: 10px;
            padding: 8px 12px;
            font-size: 16px;
            font-weight: bold;
        }
        QComboBox QAbstractItemView {
            color: white;
            background: #252525;
            selection-background-color: #3B3B3B;
        }
    """)
    header.addWidget(title)
    header.addStretch(1)
    header.addWidget(filter_select)
    layout.addLayout(header)

    subject_documents = [
        document for document in document_list
        if document["subject_id"] == subject["id"]
    ]
    
    document_rows = QtWidgets.QVBoxLayout()
    document_rows.setSpacing(10)

### FILTRADO DE DOCUMENTOS POR FECHA ###
    def filter_documents(newest_first):
        clear_layout(document_rows)
        ordered_documents = sorted(
            subject_documents,
            key=lambda document: datetime.strptime(document["date_up"], "%d/%m/%Y"),
            reverse=newest_first,
        )
        if not ordered_documents:
            empty = QtWidgets.QLabel("Todavía no hay documentos para esta materia.")
            empty.setStyleSheet("color: #EDEDED; font-size: 16px;")
            document_rows.addWidget(empty)
        else:
            for document in ordered_documents:
                document_rows.addWidget(create_document_row(document))
        document_rows.addStretch(1)

    filter_select.currentIndexChanged.connect(
        lambda _: filter_documents(filter_select.currentData())
    )
    filter_documents(filter_select.currentData())
    layout.addLayout(document_rows)

    scroll_area.setWidget(content)

    return scroll_area