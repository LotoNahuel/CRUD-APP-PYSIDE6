from PySide6 import QtCore, QtWidgets


note_list = [
    {"id": 0, "subject_id": 0, "note_name": "1° Proyecto", "note": 7},
    {"id": 1, "subject_id": 0, "note_name": "2° Proyecto", "note": 5},
    {"id": 2, "subject_id": 0, "note_name": "3° Proyecto", "note": 3},
    {"id": 3, "subject_id": 0, "note_name": "1° Examen", "note": 9},
    {"id": 4, "subject_id": 0, "note_name": "2° Examen", "note": 10},
    {"id": 5, "subject_id": 0, "note_name": "3° Examen", "note": 6},
    {"id": 6, "subject_id": 0, "note_name": "Nota final", "note": 8},
]


def create_note_row(note, is_final=False):
    """Crea una fila de dos columnas: concepto y nota."""
    row = QtWidgets.QFrame()
    row.setObjectName("finalNoteRow" if is_final else "noteRow")
    row.setFixedHeight(58)
    row.setStyleSheet("""
        QFrame#noteRow {
            background: transparent;
            border-bottom: 1px solid rgba(237, 237, 237, 50);
        }
        QFrame#finalNoteRow {
            background: #363636;
            border-radius: 10px;
        }
    """)

    row_layout = QtWidgets.QHBoxLayout(row)
    row_layout.setContentsMargins(18, 0, 18, 0)
    row_layout.setSpacing(12)

    name = QtWidgets.QLabel(note["note_name"])
    grade = QtWidgets.QLabel(str(note["note"]))
    text_style = """
        color: white;
        background: transparent;
        border: none;
        font-size: 18px;
        font-weight: bold;
    """
    name.setStyleSheet(text_style)
    grade.setStyleSheet(text_style + "font-size: 22px;")
    grade.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    grade.setFixedWidth(110)

    if is_final:
        name.setStyleSheet(text_style + "font-size: 20px;")
        grade.setStyleSheet(text_style + "font-size: 26px;")

    row_layout.addWidget(name, 1)
    row_layout.addWidget(grade)
    return row


def notes(subject):
    """Muestra una tabla centrada con las notas de una materia."""
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
    content_layout = QtWidgets.QVBoxLayout(content)
    content_layout.setContentsMargins(20, 30, 20, 30)

    table = QtWidgets.QFrame()
    table.setObjectName("gradesTable")
    table.setFixedWidth(700)
    table.setStyleSheet("""
        QFrame#gradesTable {
            background: rgba(237, 237, 237, 20);
            border: 1px solid rgba(237, 237, 237, 80);
            border-radius: 14px;
        }
    """)
    table_layout = QtWidgets.QVBoxLayout(table)
    table_layout.setContentsMargins(16, 16, 16, 16)
    table_layout.setSpacing(0)

    title = QtWidgets.QLabel(f"Notas de {subject['name']}")
    title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    title.setStyleSheet("""
        color: white;
        background: transparent;
        border: none;
        font-size: 26px;
        font-weight: bold;
        padding-bottom: 12px;
    """)

    header = QtWidgets.QFrame()
    header.setObjectName("tableHeader")
    header.setFixedHeight(46)
    header.setStyleSheet("""
        QFrame#tableHeader {
            background: #363636;
            border-radius: 10px;
        }
    """)
    header_layout = QtWidgets.QHBoxLayout(header)
    header_layout.setContentsMargins(18, 0, 18, 0)
    concept_header = QtWidgets.QLabel("CONCEPTO")
    grade_header = QtWidgets.QLabel("NOTA")
    for label in (concept_header, grade_header):
        label.setStyleSheet("color: white; background: transparent; border: none; font-size: 16px; font-weight: bold;")
    grade_header.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    grade_header.setFixedWidth(110)
    header_layout.addWidget(concept_header, 1)
    header_layout.addWidget(grade_header)

    table_layout.addWidget(title)
    table_layout.addWidget(header)

    subject_notes = [
        note for note in note_list
        if note["subject_id"] == subject["id"]
    ]

    if subject_notes:
        for note in subject_notes:
            is_final = "final" in note["note_name"].lower()
            table_layout.addWidget(create_note_row(note, is_final))
    else:
        empty = QtWidgets.QLabel("Todavía no hay notas para esta materia.")
        empty.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        empty.setStyleSheet("color: #EDEDED; background: transparent; border: none; font-size: 18px; padding: 30px;")
        table_layout.addWidget(empty)

    content_layout.addWidget(
        table,
        alignment=QtCore.Qt.AlignmentFlag.AlignHCenter | QtCore.Qt.AlignmentFlag.AlignTop,
    )
    content_layout.addStretch(1)
    scroll_area.setWidget(content)
    return scroll_area