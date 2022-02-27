class Vertex:
    def __init__(self, index: int, name: str = "") -> None:
        """
        Initialize a vertex with an index and optional name.
        :param index: Index of the vertex.
        :param name: Optional name of the vertex.
        """
        self.idx = index  # index at which the vertex has been added
        self.name = name  # name of the vertex
