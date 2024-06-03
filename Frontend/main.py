
import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from Python_UI_Scripts.home_page import Ui_WelcomeWindow  # here you need to correct the names

app = QApplication(sys.argv)
window = QMainWindow()

ui = Ui_WelcomeWindow()
ui.setupUi(window)

window.show()
sys.exit(app.exec())