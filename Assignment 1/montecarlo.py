from random import random
from rectangle import Rectangle
from typing import List


class MonteCarlo:
    def __init__(self, length: int, width: int, rectangles: List[Rectangle]):
        """constructor

        Keyword arguments:
        :param length -- length of the enclosing rectangle
        :param width -- width of the enclosing rectangle
        :param rectangles -- array that contains the embedded rectangles
        """
        self.length = length
        self.width = width
        self.rectangles = rectangles

    def area(self, num_of_shots: int):
        """Method to estimate the area of the enclosing rectangle that is not covered by the embedded rectangles

        Keyword arguments:
        :param num_of_shots -- Number of generated random points whose location (inside/outside) is analyzed
        :return float -- the area of the enclosing rectangle not covered.
        :raises ValueError if any of the parameters is None
        """
        if num_of_shots is None:
            raise ValueError("num_of_shots is None!")

        hits = 0  # number of hits in embedded rectangles
        total_area = self.width * self.length
        for shot in range(num_of_shots):
            # get point with random coordinates
            r_x = random()
            r_y = random()
            rnd = (r_x * self.length, r_y * self.width)

            # check if point is in any rectangle
            is_inside = False
            for rectangle in self.rectangles:
                is_inside = self.inside(x=rnd[0], y=rnd[1], rect=rectangle)
                if is_inside:  # point is in some rectangle
                    break

            if is_inside:
                hits += 1
        return total_area * (1 - hits / num_of_shots)

    @staticmethod
    def inside(x: float, y: float, rect: Rectangle):
        """Method to determine if a given point (x,y) is inside a given rectangle

        Keyword arguments:
        :param x -- first coordinates of the point to check
        :param y: second coordinates of the point to check
        :param rect -- given rectangle
        :return bool
        :raises ValueError if any of the parameters is None
        """
        if x is None or y is None:
            raise ValueError("One of x, y is None!")

        # get corners for intuition. Not needed, but helpful.
        left_bottom = (rect.origin_x, rect.origin_y)
        right_bottom = (rect.origin_x + rect.length, rect.origin_y)
        left_top = (rect.origin_x, rect.origin_y + rect.width)
        right_top = (rect.origin_x + rect.length, rect.origin_y + rect.width)

        # check if point is inside rectangle: first in x-range, then in y-range
        if left_bottom[0] <= x <= right_bottom[0]:
            if right_bottom[1] <= y <= right_top[1]:
                return True
        else:
            return False


def main():
    mc = MonteCarlo(
        length=100, width=30, rectangles=[Rectangle(5.0, 5.0, 75.0, 20.0)]
    )  # 75*20 = 1500 = 3000/2 = 30*100
    print("The actual area is 3000")
    print(f"Estimated area with 10 random points: {mc.area(10)}")
    print(f"Estimated area with 100 random points: {mc.area(100)}")
    print(f"Estimated area with 1000 random points: {mc.area(1000)}")
    print(f"Estimated area with 100000 random points: {mc.area(100000)}")


if __name__ == "__main__":
    main()
