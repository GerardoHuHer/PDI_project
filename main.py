import sys
import cv2
import numpy as np
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QComboBox, QSlider, QLabel, QVBoxLayout, QWidget, QHBoxLayout, QPushButton, QFileDialog
)
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtGui import QImage, QPixmap
from modules.filter_registry import apply_filter_by_name, filter_registry


class FilterApp(QMainWindow):
    def __init__(self):
        super().__init__()

        # Initialize video capture and image storage
        self.cap = cv2.VideoCapture(0)
        self.image = None
        self.mode = "Camera"  # Default mode

        self.selected_filter = list(filter_registry.keys())[0]
        self.filter_params = {"threshold1": 50, "threshold2": 100, "ksize": 3}

        # Setup UI
        self.setWindowTitle("Real-Time Filter Application")
        self.setGeometry(100, 100, 800, 600)

        # Video or image display
        self.display_label = QLabel(self)
        self.display_label.setAlignment(Qt.AlignCenter)
        self.display_label.setStyleSheet("background-color: black;")
        self.display_label.setMinimumSize(640, 480)

        # Filter dropdown
        self.filter_dropdown = QComboBox(self)
        self.filter_dropdown.addItems(filter_registry.keys())
        self.filter_dropdown.currentIndexChanged.connect(self.update_filter)

        # Sliders for parameters
        self.slider_param1 = self.create_slider("Param 1", 0, 100, 50)
        self.slider_param2 = self.create_slider("Param 2", 0, 100, 100)
        self.slider_ksize = self.create_slider("Kernel Size", 1, 20, 3)

        # Main layout
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.display_label)
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

        # Add sliders to a container widget
        sliders_widget = QWidget()
        sliders_widget.setLayout(self.sliders_layout)

        # Add sliders widget to the main layout
        self.layout.addWidget(sliders_widget)

        # Mode buttons
        self.camera_button = QPushButton("Use Camera")
        self.camera_button.clicked.connect(self.switch_to_camera)

        self.image_button = QPushButton("Open Image")
        self.image_button.clicked.connect(self.open_image)

        self.quit_button = QPushButton("Quit")
        self.quit_button.clicked.connect(self.close)

        self.button_layout = QHBoxLayout()
        self.button_layout.addWidget(self.camera_button)
        self.button_layout.addWidget(self.image_button)
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
        label.setMinimumHeight(20)
        slider = QSlider(Qt.Horizontal)
        slider.setMinimum(min_val)
        slider.setMaximum(max_val)
        slider.setValue(init_val)
        slider.valueChanged.connect(lambda val, l=label, n=name: self.update_slider_value(l, n, val))
        slider.setMinimumHeight(30)  # Ensure sliders have enough height
        return {"label": label, "slider": slider}

    def update_slider_value(self, label, name, value):
        """
        Update slider value and corresponding label.
        """
        label.setText(f"{name}: {value}")
        if name == "Param 1":
            if self.selected_filter == "Erosion" or self.selected_filter == "Dilatation":
                self.filter_params["kernel_size"] = value if value > 0 else 1
            elif self.selected_filter == "Hue Adjustment":
                self.filter_params["hue_shift"] = value
            else:
                self.filter_params["threshold1"] = value
        elif name == "Param 2":
            self.filter_params["threshold2"] = value
        elif name == "Kernel Size":
            self.filter_params["ksize"] = value if value % 2 != 0 else value + 1

    def update_filter(self):
        """
        Update the selected filter when dropdown changes.
        """
        self.selected_filter = self.filter_dropdown.currentText()

    def switch_to_camera(self):
        """
        Switch to camera mode.
        """
        self.mode = "Camera"
        self.image = None  # Clear any loaded image
        self.timer.start(30)  # Start real-time video capture

    def open_image(self):
        """
        Open an image file and switch to image mode.
        """
        self.timer.stop()  # Stop real-time video capture
        file_path, _ = QFileDialog.getOpenFileName(self, "Open Image", "", "Image Files (*.png *.jpg *.jpeg *.bmp)")
        if file_path:
            self.image = cv2.imread(file_path)
            self.mode = "Image"
            self.update_image_display()

    def update_frame(self):
        """
        Update the display frame based on the selected mode.
        """
        if self.mode == "Camera":
            ret, frame = self.cap.read()
            if not ret:
                return

            # Apply the selected filter
            processed_frame = apply_filter_by_name(frame, self.selected_filter, **self.filter_params)
            self.display_processed_frame(processed_frame)

    def update_image_display(self):
        """
        Apply the selected filter to the loaded image and update the display.
        """
        if self.image is not None and self.mode == "Image":
            processed_frame = apply_filter_by_name(self.image, self.selected_filter, **self.filter_params)
            self.display_processed_frame(processed_frame)

    def display_processed_frame(self, frame):
        """
        Convert the frame to QImage and display it in the QLabel.
        """
        height, width, _ = frame.shape
        bytes_per_line = 3 * width
        q_img = QImage(frame.data, width, height, bytes_per_line, QImage.Format_BGR888)
        pixmap = QPixmap.fromImage(q_img)
        self.display_label.setPixmap(
            pixmap.scaled(self.display_label.width(), self.display_label.height(), Qt.KeepAspectRatio))

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
