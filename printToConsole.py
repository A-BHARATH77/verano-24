import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton
from PyQt6.QtGui import QIcon
from PyQt6.QtCore   import pyqtSlot

counter = 0

def incrementAndPrint():
    global counter
    counter += 1
    print(f"Clicked increment. Value = {counter}")


def decrementAndPrint():
    global counter
    counter -= 1
    print(f"Clicked decement. Value = {counter}")


def app():
    app = QApplication([])
    widget = QWidget()
    buttonIncrement = QPushButton(widget)
    buttonIncrement.setText("Click me to increment")
    buttonIncrement.move(64,32)
    buttonIncrement.clicked.connect(incrementAndPrint)

    buttonDecrement = QPushButton(widget)
    buttonDecrement.setText("Click me to decrement")
    buttonDecrement.move(64, 64)
    buttonDecrement.clicked.connect(decrementAndPrint)

    widget.show()
    sys.exit(app.exec())

def main():
    app()

if __name__ == "__main__":
    main()
