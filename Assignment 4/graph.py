from typing import Union, List

from vertex import Vertex
from edge import Edge


class Graph:
    """Implements an undirected, weighted graph without loops using an edge list."""

    def __init__(self) -> None:
        """
        Initializes a new graph with no vertices and no edges.

        :return: None
        """
        self.vertices: List[Vertex] = []  # list of vertices in the graph
        self.edges: List[Edge] = []  # list of edges in the graph
        self.num_vertices = 0
        self.num_edges = 0
        self.undirected_graph = True

    def get_number_of_vertices(self) -> int:
        """
        :return: the number of vertices in the graph
        """
        return self.num_vertices

    def get_number_of_edges(self) -> int:
        """
        :return: the number of edges in the graph
        """
        return self.num_edges

    def get_vertices(self):
        """
        :return: list of length get_number_of_vertices() with the vertices of the graph
        """
        return self.vertices

    def get_edges(self):
        """
        :return: list of length get_number_of_edges() with the edges of the graph
        """
        return self.edges

    def insert_vertex(self, vertex_name: str) -> Union[Vertex, None]:
        """
        Inserts a new vertex with the given name into the graph.
        Returns None if the graph already contains a vertex with the same name.
        The newly added vertex should store the index at which it has been added.

        :param vertex_name: The name of vertex to be inserted
        :return: The newly added vertex, or None if the vertex was already part of the graph
        :raises: ValueError if vertex_name is None
        """
        if vertex_name is None:
            raise ValueError("Vertex name cannot be None")
        if self.find_vertex(vertex_name) is not None:
            return None

        new_vertex = Vertex(index=self.num_vertices, name=vertex_name)
        self.vertices.append(new_vertex)
        self.num_vertices += 1
        return new_vertex

    def find_vertex(self, vertex_name: str) -> Union[Vertex, None]:
        """
        Returns the respective vertex for a given name, or None if no matching vertex is found.

        :param vertex_name: the name of the vertex to find
        :return: the found vertex, or None if no matching vertex has been found.
        :raises: ValueError if vertex_name is None.
        """
        if vertex_name is None:
            raise ValueError("Vertex name cannot be None")

        for vertex in self.vertices:
            if vertex.name == vertex_name:
                return vertex
        return None  # no matching vertex found

    def insert_edge_by_vertex_names(
        self, v1_name: str, v2_name: str, weight: int
    ) -> Union[Edge, None]:
        """
        Inserts an edge between two vertices with the names v1_name and v2_name and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).

        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        if v1_name is None or v2_name is None:
            raise ValueError("Vertex name cannot be None")
        if v1_name == v2_name:
            raise ValueError("Cannot create loop")

        v1 = self.find_vertex(v1_name)
        v2 = self.find_vertex(v2_name)
        if (
            v1 is None or v2 is None
        ):  # at least one of the vertices is not part of the graph
            return None
        if self.find_edge(v1, v2) is not None:  # edge already exists
            return None
        new_edge = Edge(v1, v2, weight)
        self.edges.append(new_edge)
        self.num_edges += 1
        return new_edge

    def insert_edge(self, v1: Vertex, v2: Vertex, weight: int) -> Union[Edge, None]:
        """
        Inserts an edge between two vertices v1 and v2 and returns the newly added edge.
        None is returned if the edge already existed, or if at least one of the vertices is not found in the graph.
        A ValueError shall be thrown if v1 equals v2 (=loop).

        :param v1: vertex 1
        :param v2: vertex 2
        :param weight: weight of the edge
        :return: Returns None if the edge already exists or at least one of the two given vertices is not part of the
                 graph, otherwise returns the newly added edge.
        :raises: ValueError if v1 is equal to v2 or if v1 or v2 is None.
        """
        if v1 is None or v2 is None:
            raise ValueError("Vertex cannot be None")
        if v1 == v2:
            raise ValueError("Cannot create loop")

        if self.find_edge(v1, v2) is not None:  # edge already exists
            return None
        new_edge = Edge(v1, v2, weight)
        self.edges.append(new_edge)
        self.num_edges += 1
        return new_edge

    def find_edge_by_vertex_names(
        self, v1_name: str, v2_name: str
    ) -> Union[Edge, None]:
        """
        Returns the edge if there is an edge between the vertices with the name v1_name and v2_name, otherwise None.
        In case both names are identical a ValueError shall be raised.

        :param v1_name: name (string) of vertex 1
        :param v2_name: name (string) of vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1_name equals v2_name or if v1_name or v2_name is None.
        """
        if v1_name is None or v2_name is None:
            raise ValueError("Vertex name cannot be None")
        if v1_name == v2_name:
            raise ValueError("Cannot create loop")

        v1 = self.find_vertex(v1_name)
        v2 = self.find_vertex(v2_name)
        if (
            v1 is None or v2 is None
        ):  # at least one of the vertices is not part of the graph
            return None
        return self.find_edge(v1, v2)

    def find_edge(self, v1: Vertex, v2: Vertex) -> Union[Edge, None]:
        """
        Returns the edge if there is an edge between the vertices v1 and v2, otherwise None.
        In case v1 equals v2 a ValueError shall be raised.
        :param v1: vertex 1
        :param v2: vertex 2
        :return: Returns the found edge or None if there is no edge.
        :raises: ValueError if v1 equals v2 or if v1 or v2 are None.
        """
        if v1 is None or v2 is None:
            raise ValueError("Vertex cannot be None")
        if v1 == v2:
            raise ValueError("Cannot create loop")

        for edge in self.edges:
            if (edge.first_vertex == v1 and edge.second_vertex == v2) or (
                edge.first_vertex == v2 and edge.second_vertex == v1
            ):  # edge found
                return edge
        return None

    def get_adjacency_matrix(self) -> List[List[int]]:
        """
        Returns the NxN adjacency matrix for the graph, where N = get_number_of_vertices().
        The matrix contains the edge weight if there is an edge at the corresponding index position, otherwise -1.

        :return: adjacency matrix, as a list of lists.
        """
        # N x N matrix of -1 entries
        matrix = [
            [-1 for _ in range(self.num_vertices)] for _ in range(self.num_vertices)
        ]

        for edge in self.edges:
            # undirected graph --> symmetric
            matrix[edge.first_vertex.idx][edge.second_vertex.idx] = edge.weight
            matrix[edge.second_vertex.idx][edge.first_vertex.idx] = edge.weight
        return matrix

    def get_adjacent_vertices_by_vertex_name(self, vertex_name: str) -> List[Vertex]:
        """
        Returns a list of vertices which are adjacent to the vertex with name vertex_name.

        :param vertex_name: The name of the vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex with name vertex_name.
        :raises: ValueError if vertex_name is None
        """
        if vertex_name is None:
            raise ValueError("Vertex name cannot be None")
        vertex = self.find_vertex(vertex_name)

        if vertex is None:  # vertex not part of the graph
            return []
        return self.get_adjacent_vertices(vertex)

    def get_adjacent_vertices(self, vertex: Vertex) -> List[Vertex]:
        """
        Returns a list of vertices which are adjacent to the given vertex.

        :param vertex: The vertex to which adjacent vertices are searched.
        :return: list of vertices that are adjacent to the vertex.
        :raises: ValueError if vertex is None
        """
        if vertex is None:
            raise ValueError("Vertex cannot be None")

        adjacent_vertices = []
        for edge in self.edges:
            if edge.first_vertex == vertex:  # edge.first_vertex is vertex
                adjacent_vertices.append(edge.second_vertex)
            elif edge.second_vertex == vertex:  # edge.second_vertex is vertex
                adjacent_vertices.append(edge.first_vertex)
        return adjacent_vertices
