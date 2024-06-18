from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QLineEdit,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
import requests as re
import sys
from typing import Dict


def getData(loc, date):
    loc = input("Enter location :")
    date = input("Enter date in yyyy-MM-dd format(atleast 14 days from today) : ")
    params: Dict[str, str] = {
        "q": loc,
        "dt": date,
        "key": "285082bc4c65416790392307242005",
    }

    res = re.get("https://api.weatherapi.com/v1/future.json", params=params)
    print(res.ok)
    data = res.json()
    if "error" in data.keys():
        if data["error"]["code"] == 1006:
            print("Invalid place")
        else:
            print(data["error"]["message"])
        return None
    return res.json()

    # curl -X 'GET' \
    #   'https://api.weatherapi.com/v1/future.jon?q=asdsdvasf23&dt=2024-06-13&key=285082bc4c65416790392307242005' \
    #   -H 'accept: application/json'


class MyWeather(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("What me sky says?")
        self.setFixedSize(1000, 1000)
        self.generalLayout = QVBoxLayout()
        centralWidget = QWidget(self)
        centralWidget.setLayout(self.generalLayout)
        self.setCentralWidget(centralWidget)
        self.createInputComponent()
        self.createOutputComponent()

    def createInputComponent(self): ...

    def createOutputComponent(self): ...


def main():
    weatherApp = QApplication([])
    myWeatherWindow = MyWeather()
    myWeatherWindow.show()
    sys.exit(weatherApp.exec())


if __name__ == "__main__":
    main()
