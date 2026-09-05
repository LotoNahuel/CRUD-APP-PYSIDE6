from PySide6 import QtCore, QtWidgets


# Datos temporales: después pueden obtenerse de la base de datos.
exams_list = [
    {
        "id": 0,
        "subject_id": 0,
        "tittle": "Examen de Literatura",
        "note": "",
        "list_topics": [
            "Géneros literarios.",
            "Análisis de personajes.",
            "La obra trabajada en clase.",
        ],
        "date_exam": "28/08/2026",
    },
    {
        "id": 1,
        "subject_id": 1,
        "tittle": "Evaluación de Historia",
        "note": "8",
        "list_topics": [
            "Revoluciones del siglo XVIII.",
            "Procesos de independencia.",
        ],
        "date_exam": "02/09/2026",
    },
    {
        "id": 2,
        "subject_id": 3,
        "tittle": "Examen de Álgebra",
        "note": "",
        "list_topics": [
            "Ecuaciones de primer grado.",
            "Sistemas de ecuaciones.",
            "Factorización.",
        ],
        "date_exam": "05/09/2026",
    },
]


LABEL_STYLE = """
    background: transparent;
    color: white;
    border: none;
    font-size: 18px;
    font-weight: bold;
"""


def create_exam_row(exam):
    row = QtWidgets.QFrame()
    row.setObjectName("examRow")
    row.setStyleSheet("""
        QFrame#examRow {
            background: rgba(237, 237, 237, 20);
            border: 1px solid rgba(237, 237, 237, 80);
            border-radius: 12px;
        }
    """)

    layout = QtWidgets.QVBoxLayout(row)
    layout.setContentsMargins(18, 14, 18, 14)
    layout.setSpacing(10)

    header = QtWidgets.QHBoxLayout()
    title = QtWidgets.QLabel(exam["tittle"])
    title.setStyleSheet(LABEL_STYLE + "font-size: 26px;")

    note_value = exam["note"] or "Sin nota"
    note = QtWidgets.QLabel(f"Nota: {note_value}")
    note.setStyleSheet(LABEL_STYLE + "font-size: 22px;")
    note.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

    header.addWidget(title, 1)
    header.addWidget(note)

    topics_text = "\n".join(f"• {topic}" for topic in exam["list_topics"])
    topics = QtWidgets.QLabel(topics_text)
    topics.setStyleSheet(LABEL_STYLE)
    topics.setWordWrap(True)

    date_exam = QtWidgets.QLabel(f"Fecha del examen: {exam['date_exam']}")
    date_exam.setStyleSheet(LABEL_STYLE)
    date_exam.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight)

    layout.addLayout(header)
    layout.addWidget(topics)
    layout.addWidget(date_exam)
    return row


def exams(subject):
    """Muestra los exámenes correspondientes a una materia."""
    scroll_area = QtWidgets.QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
    scroll_area.setHorizontalScrollBarPolicy(
        QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff
    )
    scroll_area.setStyleSheet("""
        QScrollArea { background: transparent; }
        QScrollBar:vertical { width: 10px; background: transparent; }
        QScrollBar::handle:vertical { background: #555; border-radius: 5px; }
    """)

    content = QtWidgets.QWidget()
    layout = QtWidgets.QVBoxLayout(content)
    layout.setContentsMargins(20, 20, 20, 20)
    layout.setSpacing(10)

    subject_exams = [
        exam for exam in exams_list if exam["subject_id"] == subject["id"]
    ]

    if subject_exams:
        for exam in subject_exams:
            layout.addWidget(create_exam_row(exam))
    else:
        empty = QtWidgets.QLabel("Todavía no hay exámenes para esta materia.")
        empty.setStyleSheet("color: white; font-size: 20px; font-weight: bold;")
        empty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(empty)

    layout.addStretch(1)
    scroll_area.setWidget(content)
    return scroll_area
