import sys
import time
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QComboBox, QPushButton, QVBoxLayout, QFileDialog, QDateTimeEdit
from PyQt5.QtCore import Qt, QTimer


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Dark Theme GUI")
        self.setGeometry(100, 100, 800, 500)
        self.setStyleSheet("background-color: #333; color: #FFF;")

        self.folder1_label = QLabel("Select Folder 1", self)
        self.folder1_label.move(20, 20)
        self.folder1_combo = QComboBox(self)
        self.folder1_combo.move(20, 40)

        self.folder2_label = QLabel("Select Folder 2", self)
        self.folder2_label.move(20, 80)
        self.folder2_combo = QComboBox(self)
        self.folder2_combo.move(20, 100)

        self.run_capture_btn = QPushButton("Run Screen Capturing", self)
        self.run_capture_btn.move(20, 140)
        self.run_capture_btn.clicked.connect(self.run_capture)

        self.elapsed_time_label = QLabel("Elapsed Session Time: 0 seconds", self)
        self.elapsed_time_label.move(20, 180)

        self.run_detection_btn = QPushButton("Run Change Detection", self)
        self.run_detection_btn.move(20, 220)
        self.run_detection_btn.clicked.connect(self.run_detection)

        self.start_date_label = QLabel("Start Date:", self)
        self.start_date_label.move(20, 260)
        self.start_date_edit = QDateTimeEdit(self)
        self.start_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.start_date_edit.move(20, 280)

        self.end_date_label = QLabel("End Date:", self)
        self.end_date_label.move(20, 320)
        self.end_date_edit = QDateTimeEdit(self)
        self.end_date_edit.setDisplayFormat("yyyy-MM-dd")
        self.end_date_edit.move(20, 340)

        self.timer = QTimer()
        self.timer.timeout.connect(self.update_elapsed_time)
        self.elapsed_time = 0

    def run_capture(self):
        folder1 = QFileDialog.getExistingDirectory(self, "Select Folder 1")
        if folder1:
            self.folder1_combo.addItem(folder1)

        folder2 = QFileDialog.getExistingDirectory(self, "Select Folder 2")
        if folder2:
            self.folder2_combo.addItem(folder2)

    def run_detection(self):
        start_date = self.start_date_edit.date().toString("yyyy-MM-dd")
        end_date = self.end_date_edit.date().toString("yyyy-MM-dd")
        print("Start Date:", start_date)
        print("End Date:", end_date)

    def update_elapsed_time(self):
        self.elapsed_time += 1
        self.elapsed_time_label.setText(f"Elapsed Session Time: {self.elapsed_time} seconds")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
