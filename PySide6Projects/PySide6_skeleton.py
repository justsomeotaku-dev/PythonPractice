#https://www.pythonguis.com/tutorials/pyside6-creating-your-first-window/

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PySide Window")
        button = QPushButton("Press Me!")
        button.clicked.connect(self.close)
        self.setCentralWidget(button)

app = QApplication()

window = MainWindow()
window.show()

app.exec()