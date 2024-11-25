import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QSlider, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from modules.filter_registry import apply_filter_by_name, filter_registry


class FilterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize video capture
        self.cap = cv2.VideoCapture(0)
        self.selected_filter = list(filter_registry.keys())[0]
        self.filter_params = {"threshold1": 50, "threshold2": 100, "ksize": 3}

        # Setup UI
        self.setWindowTitle("Real-Time Filter Application")
        self.setGeometry(100, 100, 800, 600)

        # Video display
        self.video_label = QLabel(self)
        self.video_label.setAlignment(Qt.AlignCenter)
        self.video_label.setStyleSheet("background-color: black;")
        self.video_label.setMinimumSize(640, 480)  # Default video feed size

        # Filter dropdown
        self.filter_dropdown = QComboBox(self)
        self.filter_dropdown.addItems(filter_registry.keys())
        self.filter_dropdown.currentIndexChanged.connect(self.update_filter)

        # Sliders for parameters
        self.slider_param1 = self.create_slider("Param 1", 0, 100, 50)
        self.slider_param2 = self.create_slider("Param 2", 0, 100, 100)
        self.slider_ksize = self.create_slider("Kernel Size", 1, 20, 3)

        # Layouts
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.video_label)
        self.layout.addWidget(QLabel("Select Filter:"))
        self.layout.addWidget(self.filter_dropdown)

        # Sliders layout
        self.sliders_layout = QVBoxLayout()
        self.sliders_layout.addWidget(self.slider_param1["label"])
        self.sliders_layout.addWidget(self.slider_param1["slider"])
        self.sliders_layout.addWidget(self.slider_param2["label"])
        self.sliders_layout.addWidget(self.slider_param2["slider"])
        self.sliders_layout.addWidget(self.slider_ksize["label"])
        self.sliders_layout.addWidget(self.slider_ksize["slider"])

        self.layout.addLayout(self.sliders_layout)

        # Start and Quit buttons
        self.start_button = QPushButton("Start")
        self.start_button.clicked.connect(self.start_video)
        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.start_button)
        self.button_layout.addWidget(self.quit_button)
        self.layout.addLayout(self.button_layout)

        # Set the central widget
        central_widget = QWidget()
        central_widget.setLayout(self.layout)
        self.setCentralWidget(central_widget)

        # Timer for real-time video processing
        self.timer = QTimer()
        self.timer.timeout.connect(self.update_frame)

    def create_slider(self, name, min_val, max_val, init_val):
        """
        Create a slider with a label.
        """
        label = QLabel(f"{name}: {init_val}")
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(init_val)
        slider.valueChanged.connect(lambda val, l=label, n=name: self.update_slider_value(l, n, val))
        return {"label": label, "slider": slider}

    def update_slider_value(self, label, name, value):
        """
        Update slider value and corresponding label.
        """
        label.setText(f"{name}: {value}")
        if name == "Param 1":
            self.filter_params["threshold1"] = value
        elif name == "Param 2":
            self.filter_params["threshold2"] = value
        elif name == "Kernel Size":
            self.filter_params["ksize"] = value if value % 2 != 0 else value + 1  # Ensure odd for kernel size

    def update_filter(self):
        """
        Update the selected filter when dropdown changes.
        """
        self.selected_filter = self.filter_dropdown.currentText()

    def start_video(self):
        """
        Start the video capture loop.
        """
        self.timer.start(30)  # Trigger `update_frame` every 30 ms (~33 FPS)

    def update_frame(self):
        """
        Update the video frame with the selected filter and parameters.
        """
        ret, frame = self.cap.read()
        if not ret:
            return

        # Apply the selected filter
        processed_frame = apply_filter_by_name(frame, self.selected_filter, **self.filter_params)

        # Resize the frame to fit the QLabel
        height, width = self.video_label.height(), self.video_label.width()
        processed_frame = cv2.resize(processed_frame, (width, height), interpolation=cv2.INTER_AREA)

        # Convert frame to QImage for display
        height, width, channel = processed_frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(processed_frame.data, width, height, bytes_per_line, QImage.Format_BGR888)

        # Update the QLabel
        self.video_label.setPixmap(QPixmap.fromImage(q_img))

    def closeEvent(self, event):
        """
        Handle application close event.
        """
        self.cap.release()
        self.timer.stop()
        cv2.destroyAllWindows()
        event.accept()


def main():
    app = QApplication(sys.argv)
    main_window = FilterApp()
    main_window.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
