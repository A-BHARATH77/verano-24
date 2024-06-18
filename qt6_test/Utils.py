
class Utils:
    @classmethod
    def percentToDegrees(cls, percent: int | float) -> int:
        if percent > 100 or percent < 0:
            raise ValueError(f"Value of {percent} is invalid i.e., not within [0,100]")
        return round((720 / 99) * percent - 360, 1)

    @classmethod
    def degreesToPercent(cls,degree : int | float) -> float:
        if degree > 360 or degree < -360:
            raise ValueError(f"Value of {degree} is invalid i.e., not within [-360,360]")
        return round((degree + 360) * (99/720),2)


class Vec3:

    def __init__(
        self,
        x: int | float,
        y: int | float,
        z: int | float,
        rx: int | float,
        ry: int | float,
        rz: int | float,
    ) -> None:
        self.x = x
        self.y = y
        self.z = z
        self.rx = rx
        self.ry = ry
        self.rz = rz


class JointSpace:
    def __init__(self, base : float, shoulder : float, elbow : float, wrist1 : float, wrist2 : float, wrist3 : float) -> None:

        if any([ x== None for x in [base, shoulder, elbow , wrist1, wrist2, wrist3 ]]):
            raise ValueError("Missing arguements")

        if any([x<-360 or x > 360 for x in [base, shoulder, elbow , wrist1, wrist2, wrist3 ]]) :
            raise ValueError("Invalid set of joint angles")

        self.base = base
        self.shoulder = shoulder
        self.elbow = elbow
        self.wrist1 = wrist1
        self.wrist2 = wrist2 
        self.wrist3 = wrist3

    def toCartesian(self) -> Vec3:
        return Vec3(
            self.base + 10,
            self.shoulder + 10,
            self.elbow + 10,
            self.wrist1 + 10,
            self.wrist2 + 10,
            self.wrist3 + 10,
        )


def toJointSpace(self) -> JointSpace:
    return JointSpace(
        self.x - 10,
        self.y - 10,
        self.z - 10,
        self.rx - 10,
        self.ry - 10,
        self.rz - 10,
    )


Vec3.toJointSpace = toJointSpace
