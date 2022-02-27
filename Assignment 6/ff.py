"""Ford-Fulkerson algorithm in Python."""
from typing import List


class Graph:
    """Graph class to perform Ford-Fulkerson algorithm."""

    def __init__(self, graph: List[List[int]]) -> None:
        """Initialize the graph.

        :param graph: the graph in adjacency matrix representation
            Numbers > 0 represent edges with positive capacity, i.e. edges that can be traversed.
            Their values are the capacities of the edges.
        """
        self.graph = graph  # original graph
        self.residual_graph = [list(row) for row in graph]  # cloned graph
        self.latest_augmenting_path = [
            [0 for _ in row] for row in graph
        ]  # empty graph with same dimension as graph
        self.current_flow = [
            [0 for _ in row] for row in graph
        ]  # empty graph with same dimension as graph

    def ff_step(self, source: int, sink: int) -> int:
        """Perform a single flow augmenting iteration from source to sink.

        Update the latest augmenting path, the residual graph and the current flow by the
            maximum possible amount according to your chosen path.
        The path must be chosen based on BFS.

        :param source the source's vertex idx
        :param sink the sink's vertex idx
        :return the amount by which the flow has increased.
        """
        result = self._bfs(source, sink)
        if not result:
            return 0

        old_flow = sum(self.current_flow[source])

        # how many flow can be added to the current flow
        flow = float("inf")
        for idx, row in enumerate(self.latest_augmenting_path):
            for idx2, col in enumerate(row):
                if col == 1:
                    flow = min(flow, self.residual_graph[idx][idx2])

        # update current flow
        for i, _ in enumerate(self.graph):
            for j, _ in enumerate(self.graph[i]):
                # backward edge
                if self.latest_augmenting_path[i][j] == 1 and self.graph[i][j] == 0:
                    self.current_flow[j][i] -= flow
                # forward edge
                elif self.latest_augmenting_path[i][j] == 1:
                    self.current_flow[i][j] += flow

        # update residual graph
        for i, _ in enumerate(self.residual_graph):
            for j, _ in enumerate(self.residual_graph[i]):
                if self.latest_augmenting_path[i][j] == 1:
                    self.residual_graph[i][j] -= flow
                    self.residual_graph[j][i] += flow

        new_flow = sum(self.current_flow[source])
        return new_flow - old_flow

    def ford_fulkerson(self, source: int, sink: int) -> int:
        """Execute the ford-fulkerson algorithm (i.e., repeated calls of ff_step()).

        :param source the source's vertex id
        :param sink the sink's vertex id
        :return the max flow from source to sink
        """
        # initialize the flow
        max_flow = 0

        # augment the flow until there is no augmenting path
        while True:
            flow = self.ff_step(source, sink)
            if flow == 0:
                break
            max_flow += flow
        return max_flow

    def _bfs(self, source, sink):
        """Perform BFS from source to sink.

        :param source the source's vertex id
        :param sink the sink's vertex id
        :return the parent of the sink
        """
        # reset the latest augmenting path
        self.latest_augmenting_path = [[0 for _ in row] for row in self.graph]
        # store the parent of each vertex
        parents = [None for _ in range(len(self.graph))]

        # mark all vertices as unvisited
        visited = [False for _ in range(len(self.graph))]
        visited[source] = True
        # create a queue for BFS
        queue = [source]

        # Perform BFS
        while queue:
            # get the first vertex from the queue
            vertex = queue.pop(0)
            # get the neighbours of the vertex
            for idx, neighbour in enumerate(self.residual_graph[vertex]):
                if not visited[idx] and neighbour != 0:
                    visited[idx] = True  # mark as visited
                    queue.append(idx)
                    parents[idx] = vertex

                    # check if the sink is reached --> BFS done
                    if idx == sink:
                        # store the path from source to sink
                        parent = parents[sink]
                        while True:
                            self.latest_augmenting_path[parent][idx] = 1
                            if parents[parent] is None:
                                break
                            idx = parent
                            parent = parents[idx]
                        self.latest_augmenting_path[source][idx] = 1
                        return parents
        return False
