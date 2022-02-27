import unittest

from montecarlo import MonteCarlo
from rectangle import Rectangle


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_x(self):
        return self.x

    def get_y(self):
        return self.y


class TestAssignment01ex01Student(unittest.TestCase):
    def testMCwith3rects(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rect2 = Rectangle(6.0, 3.0, 6.0, 4.0)
        rect3 = Rectangle(10.0, 5.0, 4.0, 4.0)
        rects = [rect1, rect2, rect3]

        mc = MonteCarlo(15, 10, rects)

        area = mc.area(1000000)
        self.assertTrue(
            (97.5 <= area <= 98.5),
            "MonteCarlo.area(1000000) with the enclosing rectangle 15.0x10.0 "
            + "and the following embedded rectangles failed (area should be +/- 0.5 to the result 98 but your result is: "
            + str(area)
            + " "
            + self.printRectanglesData(rects),
        )

    def testMCwith2Rects(self):
        # area of enclosing rectangle is 50
        # area of embedded rectangles is 2+12=14
        # result is: 50-14=36
        #
        # embedded rectangle 1 is at position (0,0) with a size of 1x2
        rect1 = Rectangle(0.0, 0.0, 1.0, 2.0)
        # embedded rectangle 2 is at position (7,1) with a size of 3x4
        rect2 = Rectangle(7.0, 1.0, 3.0, 4.0)
        rects = [rect1, rect2]

        mc = MonteCarlo(10.0, 5.0, rects)

        area = mc.area(10000)
        # for 10k random points the estimated area should already be close to correct result of 36
        self.assertTrue(
            (area > 30 and area < 40),
            "MonteCarlo.area() according to the provided unit test failed! Area should be between 30 and 40 but was "
            + str(area),
        )

    def testInsideRectBorderline1Y(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(1.0, 4.0)

        self.assertTrue(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned False but should be True!",
        )

    def testInsideRectBorderline2Y(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(1.0, 0.0)

        self.assertTrue(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned False but should be True!",
        )

    def testInsideRectBorderline3Y(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(1.0, 4.01)

        self.assertFalse(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned True but should be False!",
        )

    def testInsideRectBorderline4Y(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(1.0, -0.01)

        self.assertFalse(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned True but should be False!",
        )

    def testInsideRectBorderline1X(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(0.0, 3.0)

        self.assertTrue(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned False but should be True!",
        )

    def testInsideRectBorderline2X(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(4.0, 3.0)

        self.assertTrue(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned False but should be True!",
        )

    def testInsideRectBorderline3X(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(4.01, 3.0)

        self.assertFalse(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned True but should be False!",
        )

    def testInsideRectBorderline4X(self):
        rect1 = Rectangle(0.0, 0.0, 4.0, 4.0)
        rects = []

        mc = MonteCarlo(15.0, 10.0, rects)

        pt = Point(-0.01, 3.0)

        self.assertFalse(
            mc.inside(pt.get_x(), pt.get_y(), rect1),
            "MonteCarlo.inside() with point (x="
            + str(pt.get_x())
            + "/y="
            + str(pt.get_y())
            + ") and the rectangle "
            + self.printRectangleData(rect1)
            + " returned True but should be False!",
        )

    def testMCwith0Rects1Shot(self):
        # // area of enclosing rectangle is 50
        # // area of embedded rectangles is 0

        rects = []

        mc = MonteCarlo(10.0, 5.0, rects)

        area = mc.area(1)
        self.assertEqual(
            50,
            int(area),
            "MonteCarlo.area(1) with area 10.0x5.0 and NO embedded rectangles returned wrong result. Should be 50 but was "
            + str(area),
        )

    def testMCwith0Rects100Shot(self):
        # // area of enclosing rectangle is 50
        # // area of embedded rectangles is 0

        rects = []

        mc = MonteCarlo(10.0, 5.0, rects)

        area = mc.area(100)
        self.assertEqual(
            50,
            int(area),
            "MonteCarlo.area(100) with area 10.0x5.0 and NO embedded rectangles returned wrong result. Should be 50 but was "
            + str(area),
        )

    def testMCwithMaxEmbeddedRects(self):
        # // area of enclosing rectangle is 150
        # // area of embedded rectangles is 150

        rect1 = Rectangle(6.0, 3.0, 6.0, 4.0)
        rect2 = Rectangle(10.0, 5.0, 4.0, 4.0)
        rect3 = Rectangle(0.0, 0.0, 15.0, 10.0)
        rects = [rect1, rect2, rect3]

        mc = MonteCarlo(15.0, 10.0, rects)

        area = mc.area(10000000)

        self.assertTrue(
            (area <= 0.5),
            "MonteCarlo.area(10000000) with the enclosing rectangle 15.0x10.0 "
            + "and the following \n embedded rectangles failed (area should be <=0.5 but your result is "
            + str(area)
            + "): "
            + self.printRectanglesData(rects),
        )

    # /*************************************
    #  *
    #  * private methods
    #  *
    #  */

    def printRectanglesData(self, rects):
        i = 0
        sb = ""
        while i < len(rects):
            sb += "\n{} Rectangle ".format(i + 1) + "(x="
            sb += str(rects[i].origin_x) + " y=" + str(rects[i].origin_y)
            sb += " length="
            sb += str(rects[i].length) + " width=" + str(rects[i].width) + ")"
            i += 1
        return sb

    def printRectangleData(self, rect):
        sb = " (x="
        sb += str(rect.origin_x) + " y=" + str(rect.origin_y)
        sb += " length="
        sb += str(rect.length) + " width=" + str(rect.width) + ")"

        return sb


if __name__ == "__main__":
    unittest.main()
