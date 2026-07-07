from PIL import Image, ImageEnhance
from PIL.ImageQt import ImageQt

from PySide6.QtWidgets import QApplication, QCheckBox, QMainWindow, QLabel, QSlider, QWidget, QVBoxLayout, QPushButton, QSpinBox 
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Contrast Enhancer")

        self.timer = QTimer(self)
        self.timer.setInterval(1)
        self.timer.timeout.connect(self.timer_threshold)
        self.timer.start()

        self.threshold_value = 0
        self.threshold_up = True
        self.threshold = False

        self.original_image = Image.open("yahu.jpg")

        self.image = ImageEnhance.Contrast(self.original_image).enhance(20)

        max_width = 1920
        max_height = 1920
        scale = min(max_width / self.image.width, max_height / self.image.height)

        new_width = scale * self.image.width
        new_height = scale * self.image.height

        self.image = self.image.resize((int(new_width), int(new_height)))

        # Buttons
        self.square_button = QPushButton("Square")
        self.square_button.clicked.connect(self.square_image)

        self.multiply_button = QPushButton("Multiply")
        self.multiply_button.clicked.connect(self.multiply_image)

        self.half_vertical_button = QPushButton("Half Vertical")
        self.half_vertical_button.clicked.connect(self.half_image_v)

        self.half_horizontal_button = QPushButton("Half Horizontal")
        self.half_horizontal_button.clicked.connect(self.half_image_h)

        self.threshold_slider = QSlider(Qt.Horizontal)
        self.threshold_slider.setRange(0,255)
        self.threshold_slider.setValue(125)
        self.threshold_slider.valueChanged.connect(self.threshold_image)

        self.checkbox = QCheckBox("Threshold Wave")
        self.checkbox.setChecked(False)

        # Spinboxes
        self.width_spinbox = QSpinBox()
        self.width_spinbox.setRange(1,2000)
        self.width_spinbox.setValue(self.image.width)

        self.height_spinbox = QSpinBox()
        self.height_spinbox.setRange(1,2000)
        self.height_spinbox.setValue(self.image.height)

        self.width_spinbox.valueChanged.connect(self.update_image)
        self.height_spinbox.valueChanged.connect(self.update_image)

        # save button
        self.save_button = QPushButton("Save")
        self.save_button.clicked.connect(self.save_image)

        # Image display
        self.image_label = QLabel()

        # Layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        layout.addWidget(self.square_button)
        layout.addWidget(self.multiply_button)
        layout.addWidget(self.half_horizontal_button)
        layout.addWidget(self.half_vertical_button)
        layout.addWidget(self.threshold_slider),
        layout.addWidget(self.checkbox)
        layout.addWidget(self.width_spinbox)
        layout.addWidget(self.height_spinbox)
        layout.addWidget(self.image_label)
        layout.addWidget(self.save_button)

        self.setCentralWidget(central_widget)

        self.update_image()

    def update_image(self):
        self.img = self.image.copy()
        if self.threshold:
            self.img = self.image.convert('L') #Grayscale
            self.img = self.img.point(lambda p: 255 if p > self.threshold_value else 0)
            self.img = self.img.convert('RGB')

        self.img = self.img.resize((self.width_spinbox.value(),self.height_spinbox.value()))

        qt_image = ImageQt(self.img)
        pixmap = QPixmap.fromImage(qt_image)
        self.image_label.setPixmap(pixmap)

    def save_image(self):
        self.img.save("output.png")

    def timer_threshold(self):
        if self.checkbox.isChecked():
            if self.threshold_up:
                if self.threshold_value < 255:
                    self.threshold_value += 1
                else:
                    self.threshold_up = not self.threshold_up
            else:
                if self.threshold_value > 0:
                    self.threshold_value -= 1
                else:
                    self.threshold_up = not self.threshold_up
            self.update_image()

    def square_image(self):
        size = max(self.width_spinbox.value(), self.height_spinbox.value())
        self.width_spinbox.setValue(size)
        self.height_spinbox.setValue(size)
        self.update_image()

    def multiply_image(self):
        img = self.image
        width, height = img.size

        multiplied_image = Image.new('RGB', (width * 2, height * 2))

        multiplied_image.paste(img, (0, 0))
        multiplied_image.paste(img, (width, 0))
        multiplied_image.paste(img, (0, height))
        multiplied_image.paste(img, (width, height))

        self.image = multiplied_image.resize((width, height))
        self.update_image()

    def half_image_h(self):
        img = self.image
        width, height = img.size

        half_image = Image.new('RGB', (width, height))

        half_image.paste(img.resize((int(width / 2), height)), (0, 0))
        half_image.paste(img.resize((int(width / 2), height)), (int(width / 2), 0))

        self.image = half_image
        self.update_image()

    def half_image_v(self):
        img = self.image
        width, height = img.size

        half_image = Image.new('RGB', (width, height))

        half_image.paste(img.resize((width, int(height / 2))), (0, 0))
        half_image.paste(img.resize((width, int(height / 2))), (0, int(height / 2)))

        self.image = half_image
        self.update_image()

    def threshold_image(self):
        self.threshold = True
        self.threshold_value = self.threshold_slider.value()
        self.update_image()

app = QApplication()

window = MainWindow()
window.show()

app.exec()