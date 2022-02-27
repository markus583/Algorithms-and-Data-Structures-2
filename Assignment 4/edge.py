from vertex import Vertex


class Edge:
    def __init__(
        self, first_vertex: Vertex, second_vertex: Vertex, weight: int
    ) -> None:
        """Initialize an edge object.

        :param first_vertex: The first vertex of the edge.
        :param second_vertex: The second vertex of the edge.
        :param weight: weight of the edge.
        """
        self.first_vertex = first_vertex  # reference to a vertex
        self.second_vertex = second_vertex  # reference to a vertex
        self.weight = weight  # weight of the edge
