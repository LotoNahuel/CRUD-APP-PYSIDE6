import os
import sys
from PySide6 import QtWidgets
from backend.auth.encrypt.session import authSession
from frontend.dashboard.session.login.index import Login
from frontend.dashboard.index import IndexApp
from frontend.dashboard.session.register.index import Register
from frontend.dashboard.dialog.email_verification import verification

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

class app_init:
    def __init__(self):
        super().__init__()
        self.app = None
        self.widget = None
        
        if __name__ == "__main__":
            self.run()

    def _resolve_widget(self):
        session_path = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            "auth",
            "session.json",
        )

        if os.path.exists(session_path) and authSession():
            return IndexApp()
        # return IndexApp()
        # return Register()
        return verification()

    def run(self):
        self.app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
        self.widget = self._resolve_widget()
        self.widget.resize(1280, 720)
        self.widget.setContentsMargins(0,0,0,0)
        self.widget.show()
        self.widget.setWindowTitle("SCHOOL APP")
        sys.exit(self.app.exec())


if __name__ == "__main__":
    app = app_init()