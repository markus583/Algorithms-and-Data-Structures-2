from typing import Union

from vertex import Vertex


class Step:
    def __init__(self, point: Vertex, covered_distance: Union[int, float]):
        self.point = point
        self.covered_distance = covered_distance
