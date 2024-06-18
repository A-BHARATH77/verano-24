import sys
from PyQt6 import QtWidgets
from PyQt6.QtGui import QIntValidator
from resources import *
from MainWindow import Ui_MainWindow
from Utils import *


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, *args, obj=None, **kwargs) -> None:

        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.bentUpButton.clicked.connect(self.test_click)

        self.joints: JointSpace = JointSpace(0, 0, 0, 0, 0, 0)
        self.cartesian: Vec3 = self.joints.toCartesian()

        # self.cartesian.toJointSpace()

        self.setTicksOnSliders()
        self.setSliderPositions()
        self.setSliderValues()
        self.connectSliders()
        self.setToolPosition()
        self.connectSliderButtons()
        self.connectToolLineEdits()

    def test_click(self) -> None:
        print("Hello world!")

    def setTicksOnSliders(self) -> None:
        self.baseJointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.baseJointSlider.setTickInterval(100 // 8)

        self.elbowJointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.elbowJointSlider.setTickInterval(100 // 8)

        self.shulderJointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.shulderJointSlider.setTickInterval(100 // 8)

        self.wrist1JointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.wrist1JointSlider.setTickInterval(100 // 8)

        self.wrist2JointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.wrist2JointSlider.setTickInterval(100 // 8)

        self.wrist3JointSlider.setTickPosition(
            QtWidgets.QSlider.TickPosition.TicksBothSides
        )
        self.wrist3JointSlider.setTickInterval(100 // 8)

    def setSliderPositions(self) -> None:
        self.baseJointSlider.setRange(-360, 360)
        self.elbowJointSlider.setRange(-360, 360)
        self.shulderJointSlider.setRange(-360, 360)
        self.wrist1JointSlider.setRange(-360, 360)
        self.wrist2JointSlider.setRange(-360, 360)
        self.wrist3JointSlider.setRange(-360, 360)

        self.baseJointSlider.setValue(0)
        self.elbowJointSlider.setValue(0)
        self.shulderJointSlider.setValue(0)
        self.wrist1JointSlider.setValue(0)
        self.wrist2JointSlider.setValue(0)
        self.wrist3JointSlider.setValue(0)

    def setSliderValues(self) -> None:
        self.bLineEdit.setReadOnly(True)
        self.eLineEdit.setReadOnly(True)
        self.sLineEdit.setReadOnly(True)
        self.w1LineEdit.setReadOnly(True)
        self.w2LineEdit.setReadOnly(True)
        self.w3LIneEdit.setReadOnly(True)

        self.bLineEdit.setText(str(self.joints.base))
        self.eLineEdit.setText(str(self.joints.elbow))
        self.sLineEdit.setText(str(self.joints.shoulder))
        self.w1LineEdit.setText(str(self.joints.wrist1))
        self.w2LineEdit.setText(str(self.joints.wrist2))
        self.w3LIneEdit.setText(str(self.joints.wrist3))

    def connectSliders(self) -> None:
        # self.baseJointSlider.valueChanged.connect(lambda x : self.bLineEdit.setText(str(Utils.percentToDegrees(x)) ))
        # self.baseJointSlider.valueChanged.connect(lambda x : self.setJoints(base = self.bLineEdit.text, ))
        self.baseJointSlider.valueChanged.connect(
            lambda x: self.setJoint(base=x, updateCartesian=True)
        )
        self.elbowJointSlider.valueChanged.connect(
            lambda x: self.setJoint(elbow=x, updateCartesian=True)
        )
        self.shulderJointSlider.valueChanged.connect(
            lambda x: self.setJoint(shoulder=x, updateCartesian=True)
        )

        self.wrist1JointSlider.valueChanged.connect(
            lambda x: self.setJoint(wrist1=x, updateCartesian=True)
        )

        self.wrist2JointSlider.valueChanged.connect(
            lambda x: self.setJoint(wrist2=x, updateCartesian=True)
        )

        self.wrist3JointSlider.valueChanged.connect(
            lambda x: self.setJoint(wrist3=x, updateCartesian=True)
        )

        # self.baseJointSlider.valueChanged.connect(lambda x : print(x))
        # self.elbowJointSlider.valueChanged.connect(lambda x : self.eLineEdit.setText(str(Utils.percentToDegrees(x)) ))
        # self.shulderJointSlider.valueChanged.connect(lambda x : self.sLineEdit.setText(str(Utils.percentToDegrees(x)) ))
        # self.wrist1JointSlider.valueChanged.connect(lambda x : self.w1LineEdit.setText(str(Utils.percentToDegrees(x)) ))
        # self.wrist2JointSlider.valueChanged.connect(lambda x : self.w2LineEdit.setText(str(Utils.percentToDegrees(x)) ))
        # self.wrist3JointSlider.valueChanged.connect(lambda x : self.w3LIneEdit.setText(str(Utils.percentToDegrees(x)) ))

    def setToolPosition(self) -> None:
        self.xToolLineEdit.setText("0")
        self.yToolLIneEdit.setText("0")
        self.zToolLIneEdit.setText("0")
        self.rxToolLineEdit.setText("0")
        self.ryToolLineEdit.setText("0")
        self.rzToolLineEdit.setText("0")

    def setJoint(
        self,
        base: float | None = None,
        shoulder: float | None = None,
        elbow: float | None = None,
        wrist1: float | None = None,
        wrist2: float | None = None,
        wrist3: float | None = None,
        updateCartesian: bool = False,
        cartesian: bool = False,
    ):

        if cartesian:
            self.joints = self.cartesian.toJointSpace()

            self.bLineEdit.setText(str(self.joints.base))
            self.eLineEdit.setText(str(self.joints.elbow))
            self.sLineEdit.setText(str(self.joints.shoulder))
            self.w1LineEdit.setText(str(self.joints.wrist1))
            self.w2LineEdit.setText(str(self.joints.wrist2))
            self.w3LIneEdit.setText(str(self.joints.wrist3))

            self.baseJointSlider.setValue(self.joints.base)
            self.elbowJointSlider.setValue(self.joints.elbow)
            self.shulderJointSlider.setValue(self.joints.shoulder)
            self.wrist1JointSlider.setValue(self.joints.wrist1)
            self.wrist2JointSlider.setValue(self.joints.wrist2)
            self.wrist3JointSlider.setValue(self.joints.wrist3)

        if base:
            self.bLineEdit.setText(str(base))
            self.joints.base = base
        if elbow:
            self.eLineEdit.setText(str(elbow))
            self.joints.elbow = elbow
        if shoulder:
            self.sLineEdit.setText(str(shoulder))
            self.joints.shoulder = shoulder
        if wrist1:
            self.w1LineEdit.setText(str(wrist1))
            self.joints.wrist1 = wrist1
        if wrist2:
            self.w2LineEdit.setText(str(wrist2))
            self.joints.wrist2 = wrist2
        if wrist3:
            self.w3LIneEdit.setText(str(wrist3))
            self.joints.wrist3 = wrist3
        if updateCartesian:
            print("Update cartesian")
            self.setCartesian(joint=True)

    def connectSliderButtons(self):
        self.baseLeftButton.clicked.connect(
            lambda: self.baseJointSlider.setValue(
                self.baseJointSlider.value() - self.stepSpinBox.value()
                if ((self.baseJointSlider.value() - self.stepSpinBox.value()) >= -360)
                else -360
            )
        )

        self.baseRightButton.clicked.connect(
            lambda: self.baseJointSlider.setValue(
                round(self.baseJointSlider.value() + self.stepSpinBox.value())
                if ((self.baseJointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

        self.elbowLeftButton.clicked.connect(
            lambda: self.elbowJointSlider.setValue(
                self.elbowJointSlider.value() - self.stepSpinBox.value()
                if ((self.elbowJointSlider.value() - self.stepSpinBox.value()) >= -360)
                else -360
            )
        )

        self.elbowRightButton.clicked.connect(
            lambda: self.elbowJointSlider.setValue(
                round(self.elbowJointSlider.value() + self.stepSpinBox.value())
                if ((self.elbowJointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

        self.shoulderLeftButton.clicked.connect(
            lambda: self.shulderJointSlider.setValue(
                self.shulderJointSlider.value() - self.stepSpinBox.value()
                if (
                    (self.shulderJointSlider.value() - self.stepSpinBox.value()) >= -360
                )
                else -360
            )
        )

        self.shoulderRightButton.clicked.connect(
            lambda: self.shulderJointSlider.setValue(
                round(self.shulderJointSlider.value() + self.stepSpinBox.value())
                if ((self.shulderJointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

        self.w1LeftButton.clicked.connect(
            lambda: self.wrist1JointSlider.setValue(
                self.wrist1JointSlider.value() - self.stepSpinBox.value()
                if ((self.wrist1JointSlider.value() - self.stepSpinBox.value()) >= -360)
                else -360
            )
        )

        self.w1RightButton.clicked.connect(
            lambda: self.wrist1JointSlider.setValue(
                round(self.wrist1JointSlider.value() + self.stepSpinBox.value())
                if ((self.wrist1JointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

        self.w2LeftButton.clicked.connect(
            lambda: self.wrist2JointSlider.setValue(
                self.wrist2JointSlider.value() - self.stepSpinBox.value()
                if ((self.wrist2JointSlider.value() - self.stepSpinBox.value()) >= -360)
                else -360
            )
        )

        self.w2RightButton.clicked.connect(
            lambda: self.wrist2JointSlider.setValue(
                round(self.wrist2JointSlider.value() + self.stepSpinBox.value())
                if ((self.wrist2JointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

        self.w3LeftButton.clicked.connect(
            lambda: self.wrist3JointSlider.setValue(
                self.wrist3JointSlider.value() - self.stepSpinBox.value()
                if ((self.wrist3JointSlider.value() - self.stepSpinBox.value()) >= -360)
                else -360
            )
        )

        self.w3RIghtButton.clicked.connect(
            lambda: self.wrist3JointSlider.setValue(
                round(self.wrist3JointSlider.value() + self.stepSpinBox.value())
                if ((self.wrist3JointSlider.value() + self.stepSpinBox.value()) <= 360)
                else 360
            )
        )

    def setCartesian(
        self,
        x: None | float = None,
        y: None | float = None,
        z: None | float = None,
        rx: None | float = None,
        ry: None | float = None,
        rz: None | float = None,
        updateJoint: bool = False,
        joint: bool = False,
    ):
        # raise NotImplementedError
        if joint:
            self.cartesian = self.joints.toCartesian()
            self.xToolLineEdit.setText(str(self.cartesian.x))
            self.yToolLIneEdit.setText(str(self.cartesian.y))
            self.zToolLIneEdit.setText(str(self.cartesian.z))
            self.rxToolLineEdit.setText(str(self.cartesian.rx))
            self.ryToolLineEdit.setText(str(self.cartesian.ry))
            self.rzToolLineEdit.setText(str(self.cartesian.rz))
        if x:
            self.xToolLineEdit.setText(str(x))
            self.cartesian.x = x
        if y:
            self.yToolLIneEdit.setText(str(y))
            self.cartesian.y = y
        if z:
            self.zToolLIneEdit.setText(str(z))
            self.cartesian.z = z
        if rx:
            self.rxToolLineEdit.setText(str(rx))
            self.cartesian.rx = rx
        if ry:
            self.ryToolLineEdit.setText(str(ry))
            self.cartesian.ry = ry
        if rz:
            self.rzToolLineEdit.setText(str(rz))
            self.cartesian.rz = rz
        if updateJoint:
            print("Update joint")
            self.setJoint(cartesian=True)

    def connectToolLineEdits(self):

        # self.xToolLineEdit.setValidator(QIntValidator(0,500,self))
        # self.yToolLIneEdit.setValidator(QIntValidator(0,500,self))
        # self.zToolLIneEdit.setValidator(QIntValidator(0,500,self))
        # self.rxToolLineEdit.setValidator(QIntValidator(0,500,self))
        # self.ryToolLineEdit.setValidator(QIntValidator(0, 500, self))
        # self.rzToolLineEdit.setValidator(QIntValidator(0, 500, self))

        self.xToolLineEdit.editingFinished.connect(
            lambda: self.setCartesian(
                x=int(self.xToolLineEdit.text()), updateJoint=True
            )
        )
        self.yToolLIneEdit.editingFinished.connect(
            lambda: self.setCartesian(
                y=int(self.yToolLIneEdit.text()), updateJoint=True
            )
        )
        self.zToolLIneEdit.editingFinished.connect(
            lambda: self.setCartesian(
                z=int(self.zToolLIneEdit.text()), updateJoint=True
            )
        )
        self.rxToolLineEdit.editingFinished.connect(
            lambda: self.setCartesian(
                rx=int(self.rxToolLineEdit.text()), updateJoint=True
            )
        )
        self.ryToolLineEdit.editingFinished.connect(
            lambda: self.setCartesian(
                ry=int(self.ryToolLineEdit.text()), updateJoint=True
            )
        )
        self.rzToolLineEdit.editingFinished.connect(
            lambda: self.setCartesian(
                rz=int(self.rzToolLineEdit.text()), updateJoint=True
            )
        )


def main() -> None:
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
