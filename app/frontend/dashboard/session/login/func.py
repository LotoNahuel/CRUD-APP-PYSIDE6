RED_STYLE = (
    "color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; "
    "border: 1px solid red; border-radius: 6px; min-width: 220px;"
)
NORMAL_STYLE = (
    "color: white; font-size: 14px; padding: 10px; background-color: #2f2f2f; "
    "border: 1px solid #5a5a5a; border-radius: 6px; min-width: 220px;"
)

def set_input_style(input_widget, is_valid):
    if input_widget is None:
        return
    input_widget.setStyleSheet(NORMAL_STYLE if is_valid else RED_STYLE)


def verify_data(data):
    c = 0
    email = ""
    password = ""
    fields = {}

    try:
        for label_widget, input_widget in data:
            label = label_widget.text()
            fields[label] = input_widget
            text = input_widget.text()

            if label == "Email":
                email = text
            elif label == "Password":
                password = text

            if text == "":
                set_input_style(input_widget, False)
                c += 1
            else:
                set_input_style(input_widget, True)
        return c == 0
    except Exception as e:
        print(f"Error al verificar los datos: {e}")
        return False