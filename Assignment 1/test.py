# create class that takes in 3 spatial variables and 2 temporal variables
class Point:
    def __init__(self, x, y, z, t):
        self.x = x
        self.y = y
        self.z = z
        self.t = t

    def __str__(self):
        return (
            "("
            + str(self.x)
            + ", "
            + str(self.y)
            + ", "
            + str(self.z)
            + ", "
            + str(self.t)
            + ")"
        )

    def __repr__(self):
        return (
            "("
            + str(self.x)
            + ", "
            + str(self.y)
            + ", "
            + str(self.z)
            + ", "
            + str(self.t)
            + ")"
        )
