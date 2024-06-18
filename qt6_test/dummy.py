import sys
from PyQt6.QtWidgets import QApplication, QVBoxLayout, QWidget, QSlider, QLabel


class SliderExample(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.slider = QSlider(self)

        self.label = QLabel("Current value: 0", self)

        # Connect the valueChanged signal to the custom slot
        self.slider.valueChanged.connect(self.on_value_changed)

        # Set the value of the slider (this will trigger the valueChanged signal)
        self.slider.setValue(50)

        layout = QVBoxLayout()
        layout.addWidget(self.slider)
        layout.addWidget(self.label)

        self.setLayout(layout)

        self.setWindowTitle("QSlider Example")
        self.show()

    def on_value_changed(self, value):
        # Update the label when the slider value changes
        self.label.setText(f"Current value: {value}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = SliderExample()
    sys.exit(app.exec())
