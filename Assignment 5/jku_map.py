from typing import Dict, List, Tuple, Mapping, Union

from graph import Graph
from vertex import Vertex
from step import Step


class JKUMap(Graph):
    """
    A class representing a map of the JKU campus.
    """

    def __init__(self):
        super().__init__()
        self._insert_jku_map()
        # initialize distances and paths
        self.distances, self.paths = self._initialize_dijkstra()
        # call dijkstra now - this not make a difference whether we do it now or on-demand
        # assignment gives us enough freedom to do it now - given way of testing, probably even faster
        for vertex, _ in zip(self.distances, self.paths):
            self.distances[vertex], self.paths[vertex] = self._dijkstra(
                vertex, set(), self.distances[vertex], self.paths[vertex]
            )

    def _initialize_dijkstra(
        self,
    ) -> Tuple[
        Mapping[Vertex, Dict[Vertex, float]], Mapping[Vertex, Dict[Vertex, List]]
    ]:
        """
        This method initializes the distances and paths maps for dijkstra algorithm.
        :return: A tuple of two dictionaries, containing the distances and paths maps.
        """
        distances = {
            vertex: {
                inner_vertex: float("inf")
                if vertex != inner_vertex
                else 0  # 0 distance to itself
                for inner_vertex in self.vertices
            }
            for vertex in self.vertices
        }
        paths = {
            vertex: {inner_vertex: [] for inner_vertex in self.vertices}  # empty paths
            for vertex in self.vertices
        }
        return distances, paths

    def get_shortest_path_from_to(
        self, from_vertex: Vertex, to_vertex: Vertex
    ) -> List[Step]:
        """
        This method determines the shortest path between two POIs "from_vertex" and "to_vertex".
        It returns the list of intermediate steps of the route that have been found
        using the dijkstra algorithm.

        :param from_vertex: Start vertex
        :param to_vertex:   Destination vertex
        :return:
           The path, with all intermediate steps, returned as a list. This list
           sequentially contains each vertex along the shortest path, together with
           the already covered distance (see example on the assignment sheet).
           Returns None if there is no path between the two given vertices.
        :raises ValueError: If from_vertex or to_vertex is None, or if from_vertex equals to_vertex
        """
        if from_vertex is None or to_vertex is None:
            raise ValueError("from_vertex or to_vertex is None")
        if from_vertex == to_vertex:
            raise ValueError("from_vertex equals to_vertex")

        result = self.paths[from_vertex][to_vertex]
        return result if len(result) > 0 else None

    def get_steps_for_shortest_paths_from(self, from_vertex: Vertex) -> Dict[str, int]:
        """
        This method determines the amount of "steps" needed on the shortest paths
        from a given "from" vertex to all other vertices.
        The number of steps (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and number of steps as value.
        E.g., the "from" vertex has a step count of 0 to itself and 1 to all adjacent vertices.

        :param from_vertex: start vertex
        :return:
          A map containing the number of steps (or -1 if no path exists) on the
          shortest path to each vertex, using the vertex name as key and the number of steps as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError("from_vertex is None")

        lengths = {
            vertex.name: len(self.paths[from_vertex][vertex])
            - 1  # -1 because we do not count from_vertex
            for vertex in self.vertices
        }
        return lengths

    def get_shortest_distances_from(self, from_vertex: Vertex) -> Dict[Vertex, float]:
        """
        This method determines the shortest paths from a given "from" vertex to all other vertices.
        The shortest distance (or -1 if no path exists) to each vertex is returned
        as a dictionary, using the vertex name as key and the distance as value.

        :param from_vertex: Start vertex
        :return
           A dictionary containing the shortest distance (or -1 if no path exists) to each vertex,
           using the vertex name as key and the distance as value.
        :raises ValueError: If from_vertex is None.
        """
        if from_vertex is None:
            raise ValueError("from_vertex is None")

        return {
            key.name: value if value != float("inf") else -1  # -1 if no path exists
            for key, value in self.distances[from_vertex].items()
        }

    def _dijkstra(
        self,
        cur: Vertex,
        visited: set,
        distances: Dict[Vertex, Union[float, int]],
        paths: Dict[Vertex, List],
    ) -> Tuple[Dict[Vertex, Union[float, int]], Dict[Vertex, List]]:

        """
        This method is expected to be called with correctly initialized data structures and recursively calls itself.

        :param cur: Current vertex being processed
        :param visited: Set which stores already visited vertices.
        :param distances: Dict (nVertices entries) which stores the min. distance to each vertex.
        :param paths: Dict (nVertices entries) which stores the shortest path to each vertex.
        """
        visited.add(cur)  # Mark current vertex as visited. It is not visited anymore.
        for vertex in self.get_adjacent_vertices(cur):
            if vertex not in visited:
                if (
                    distances[vertex]
                    > distances[cur] + self.find_edge(cur, vertex).weight
                ):  # new shortest path found, update distances and paths
                    distances[vertex] = (
                        distances[cur] + self.find_edge(cur, vertex).weight
                    )

                    if len(paths[cur]) == 0:  # if cur is the first vertex in the path
                        paths[cur] = [Step(cur, distances[cur])]
                    paths[vertex] = paths[cur] + [
                        Step(vertex, distances[vertex])
                    ]  # update path to vertex

        # Find the next vertex with the smallest distance, which is not yet visited.
        for neighbor in sorted(distances, key=distances.get):
            if neighbor not in visited:
                # Recursively call this method for all vertices which are not yet visited.
                return self._dijkstra(neighbor, visited, distances, paths)
        return distances, paths

    def _insert_jku_map(self) -> None:
        """
        This method inserts all vertices and edges of the JKU campus map into the graph.
        """
        locations = [
            "Spar",
            "LIT",
            "Porter",
            "Open Lab",
            "Bank",
            "KHG",
            "Parking",
            "Chat",
            "Bella Casa",
            "Teichwerk",
            "Library",
            "LUI",
            "SP1",
            "SP3",
            "Castle",
            "Papaya",
            "JKH",
        ]
        for location in locations:
            self.insert_vertex(location)
        edges = [
            ["Open Lab", "Porter", 70],
            ["LIT", "Porter", 80],
            ["LIT", "Spar", 50],
            ["Spar", "Porter", 103],
            ["Bank", "Porter", 100],
            ["Spar", "KHG", 165],
            ["KHG", "Bank", 150],
            ["KHG", "Parking", 190],
            ["Parking", "Bella Casa", 145],
            ["Parking", "SP1", 240],
            ["SP1", "SP3", 130],
            ["SP1", "LUI", 175],
            ["Teichwerk", "LUI", 135],
            ["LUI", "Library", 90],
            ["LUI", "Chat", 240],
            ["Chat", "Library", 160],
            ["Chat", "Bank", 115],
            ["Papaya", "Castle", 85],
            ["Papaya", "JKH", 80],
        ]
        for edge in edges:
            self.insert_edge_by_vertex_names(edge[0], edge[1], edge[2])


if __name__ == "__main__":
    # You can use this main function to test your implementation.
    # Feel free to change the vertex names to test your implementation.

    # Create a new graph
    g = JKUMap()
    print(g.get_adjacency_matrix())
