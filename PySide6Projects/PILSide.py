from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

from PySide6.QtWidgets import QApplication, QMainWindow, QLabel
from PySide6.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contrast Enhancer")

        img = Image.open("Yahu.jpg")

        img = ImageEnhance.Contrast(img).enhance(2)
        img = img.resize((400,400))

        qimg = ImageQt(img)
        pixmap = QPixmap.fromImage(qimg)

        label = QLabel()
        label.setPixmap(pixmap)
        self.setCentralWidget(label)

app = QApplication()

window = MainWindow()
window.show()

app.exec()