from PySide6.QtWidgets import QApplication, QCheckBox, QComboBox, QHBoxLayout, QMainWindow, QLabel, QSlider, QWidget, QVBoxLayout, QPushButton, QSpinBox 
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt, QTimer

from datetime import datetime
from zoneinfo import ZoneInfo, available_timezones

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("World Clock")

        self.active_zones = [
            "Europe/London",
            "Europe/Paris",
            "America/New_York",
            "America/Los_Angeles",
            "Asia/Tokyo",
        ]

        self.total_zones = sorted(
            zone for zone in available_timezones()
            if zone.startswith(("Europe/", "America/", "Asia/", "Australia/", "Pacific/"))
        )

        self.layout: QVBoxLayout = QVBoxLayout() # type annotation
        central = QWidget()

        self.rows = {}

        selector_spinbox = QComboBox()
        selector_spinbox.addItems(self.total_zones)
        self.layout.addWidget(selector_spinbox)

        selector_button = QPushButton("Add Timezone")
        selector_button.clicked.connect(lambda: self.add_zone(selector_spinbox.currentText()))
        self.layout.addWidget(selector_button)

        for zone in self.active_zones:
            self.add_zone(zone)

        central.setLayout(self.layout)
        self.setCentralWidget(central)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_clock)
        self.timer.start(1000)

        self.update_clock()
    
    def update_clock(self):
        for zone in self.active_zones:
            current_time = datetime.now(ZoneInfo(zone)).strftime("%d/%m/%Y, %H:%M:%S") # works after installing tzdata
            self.rows[zone]["zone"].setText(zone.split("/")[-1])
            self.rows[zone]["time"].setText(current_time)

    def add_zone(self, zone):
        if zone in self.rows:
            return

        row = QHBoxLayout()
        city_label = QLabel()
        city_label.setMidLineWidth(300)
        time_label = QLabel()
        time_label.setAlignment(Qt.AlignRight)
        remove_button = QPushButton("🔴")
        remove_button.setMaximumWidth(30)
        remove_button.clicked.connect(lambda checked, z=zone: self.remove_zone(z))

        row.addWidget(city_label)
        row.addWidget(time_label)
        row.addWidget(remove_button)
        self.layout.addLayout(row)

        if zone not in self.active_zones:
            self.active_zones.append(zone)
        self.rows[zone] = {
            "zone":city_label,
            "time":time_label,
            "row":row
        }
            
    def remove_zone(self, zone):
        while self.rows[zone]["row"].count():
            item = self.rows[zone]["row"].takeAt(0)
            widget = item.widget() # checks if there is a widget
            if widget:
                widget.deleteLater()
        self.rows[zone]["row"].deleteLater()
        self.active_zones.remove(zone)
        del self.rows[zone]

app = QApplication()
window = MainWindow()
window.show()
app.exec()