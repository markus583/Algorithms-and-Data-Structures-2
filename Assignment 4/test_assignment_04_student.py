import unittest

from graph import Graph
from vertex import Vertex


class TestAssignment04Student(unittest.TestCase):
    undirected_graph_flag = True

    _expected_matrix_undirected_graph = [
        [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 10, -1, -1, -1, -1, -1, -1, -1, -1],
        [1, -1, -1, -1, -1, 2, 3, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, 5, -1, -1, 6, 7, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 5, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 2, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, 3, -1, -1, -1, -1, 4, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 6, -1, -1, 4, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 7, -1, -1, -1, -1, -1, -1, 8, -1, -1, -1, -1, -1, -1, -1],
        [-1, 10, -1, -1, -1, -1, -1, -1, -1, -1, 11, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, 8, 11, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 9, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 12, -1, 13, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 13, -1, 14, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 15, -1, -1, 14, -1, 16],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 16, -1]
    ]

    _expected_matrix_directed_graph = [
        [-1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, 1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, 1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 1, -1, -1, -1, -1, 1],
        [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]
    ]

    def test_insert_vertex(self):
        try:
            g = Graph()
            vertex_linz = g.insert_vertex("Linz")

            self.assertEqual(vertex_linz.idx, 0,
                             ".insert_vertex() returned wrong vertex index after inserting vertex \"Linz\" into an "
                             "empty graph: ")
            self.assertEqual(vertex_linz.name, "Linz",
                             ".insert_vertex() returned wrong vertex name after inserting vertex \"Linz\" into an "
                             "empty graph: ")
            self.assertEqual(vertex_linz, g.vertices[vertex_linz.idx],
                             ".insertVertex(): wrong vertex at index 0 after inserting vertices \"Linz\" into an "
                             "empty graph: ")

        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_insert_vertex_twice(self):
        try:
            g = Graph()
            vertex_linz = g.insert_vertex("Linz")
            vertex_linz2 = g.insert_vertex("Linz")
            self.assertIsNone(vertex_linz2, ".insert_vertex() returned not None when trying to insert an already "
                                            "existing vertex: ")
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_insert_multiple_vertices(self):
        try:
            g = Graph()
            v_linz = g.insert_vertex("Linz")

            self.assertEqual(0, v_linz.idx, ".insert_vertex() returned wrong index after inserting vertex \"Linz\" "
                                            "into an empty graph: ")
            self.assertEqual(v_linz, g.get_vertices()[v_linz.idx], ".insert_vertex(): wrong vertex at index 0 after "
                                                                   "inserting vertex \"Linz\" into an empty graph: ")

            v_wien = g.insert_vertex("Wien")
            self.assertEqual(1, v_wien.idx,
                             ".insert_vertex() returned wrong index for \"Wien\" after inserting vertex \"Linz\" and "
                             "\"Wien\" into an empty graph: ")
            self.assertEqual(v_linz, g.get_vertices()[v_linz.idx],
                             ".insert_vertex(): wrong vertex at index 0 after inserting vertices \"Linz\" and "
                             "\"Wien\" into an empty graph: ")
            self.assertEqual(v_wien, g.get_vertices()[v_wien.idx],
                             ".insert_vertex(): wrong vertex at index 1 after inserting vertices \"Linz\" and "
                             "\"Wien\" into an empty graph: ")

            v_graz = g.insert_vertex("Graz")
            self.assertEqual(2, v_graz.idx,
                             ".insert_vertex() returned wrong index for \"Graz\" after inserting vertex \"Linz\", "
                             "\"Wien\" and \"Graz\" into an empty graph: ")
            self.assertEqual(v_linz, g.get_vertices()[v_linz.idx],
                             ".insert_vertex(): wrong vertex at index 0 after inserting vertices \"Linz\", \"Wien\" "
                             "and \"Graz\" into an empty graph: ")
            self.assertEqual(v_wien, g.get_vertices()[v_wien.idx],
                             ".insert_vertex(): wrong vertex at index 1 after inserting vertices \"Linz\", \"Wien\" "
                             "and \"Graz\" into an empty graph: ")
            self.assertEqual(v_graz, g.get_vertices()[v_graz.idx],
                             ".insert_vertex(): wrong vertex at index 2 after inserting vertices \"Linz\", \"Wien\" "
                             "and \"Graz\" into an empty graph: ")



        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_number_of_vertices_simple(self):
        try:
            g = Graph()
            v_linz = Vertex("Linz")
            v_wien = Vertex("Wien")
            v_graz = Vertex("Graz")

            g.insert_vertex(v_linz)
            g.insert_vertex(v_wien)
            g.insert_vertex(v_graz)

            self.assertEqual(3, g.get_number_of_vertices(),
                             ".get_number_of_vertices() returned wrong value for a graph with 3 vertices: ")
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_number_of_vertices_large(self):
        try:
            g = self._initialize_large_graph()
            self.assertEqual(18, g.get_number_of_vertices(),
                             ".get_number_of_vertices() returned wrong value for a graph with 18 vertices: ")
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_insert_not_yet_existing_edges(self):
        try:
            g = Graph()
            v_linz = g.insert_vertex("Linz")
            v_wien = g.insert_vertex("Wien")
            v_graz = g.insert_vertex("Graz")
            str_graph = "[\"Linz\",\"Wien\",\"Graz\"]"

            self.assertIsNotNone(g.insert_edge_by_vertex_names("Linz", "Wien", 100),
                                 ".insert_edge(): inserting a not existing edge between \"Linz\" and \"Wien\" in a "
                                 "graph with vertices " + str_graph + " returned None.")
            self.assertIsNotNone(g.insert_edge_by_vertex_names("Graz", "Wien", 10),
                                 ".insert_edge(): inserting a not existing edge between \"Graz\" and \"Wien\" in a "
                                 "graph with vertices " + str_graph + " returned None.")
            self.assertIsNotNone(g.insert_edge_by_vertex_names("Linz", "Graz", 1),
                                 ".insert_edge(): inserting a not existing edge between \"Linz\" and \"Graz\" in a "
                                 "graph with vertices " + str_graph + " returned None.")
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_insert_existing_edge(self):
        try:
            g = Graph()
            v_linz = g.insert_vertex("Linz")
            v_wien = g.insert_vertex("Wien")
            v_graz = g.insert_vertex("Graz")

            str_graph = "[\"Linz\",\"Wien\",\"Graz\"]"

            self.assertIsNotNone(g.insert_edge(v_linz, v_wien, 100),
                                 ".insert_edge(): inserting a not existing edge between \"Linz\" and \"Wien\" in a "
                                 "graph with vertices " + str_graph + " returned false.")
            self.assertIsNotNone(g.insert_edge(v_graz, v_wien, 10),
                                 ".insert_edge(): inserting a not existing edge between \"Graz\" and \"Wien\" in a "
                                 "graph with vertices " + str_graph + " returned false.")
            self.assertIsNotNone(g.insert_edge(v_linz, v_graz, 1),
                                 ".insert_edge(): inserting a not existing edge between \"Linz\" and \"Graz\" in a "
                                 "graph with vertices " + str_graph + " returned false.")
            self.assertIsNone(g.insert_edge(v_linz, v_graz, 2),
                              ".insert_edge(): inserting an already existing edge between \"Linz\" and \"Graz\" in a "
                              "graph with vertices " + str_graph + " returned true.")
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_insert_edge_between_not_existing_vertex(self):
        try:
            g = Graph()
            v_linz = g.insert_vertex("Linz")

            self.assertIsNone(g.insert_edge_by_vertex_names("Linz", "Hupfingatsch", 100),
                              ".insert_edge_by_vertex_names(): inserting an edge in a graph a single vertex did not "
                              "return None.")
            self.assertIsNone(g.insert_edge_by_vertex_names("Hupfingatsch", "Linz", 10),
                              ".insert_edge_by_vertex_names(): inserting an edge in a graph a single vertex did not "
                              "return None.")
            self.assertIsNone(g.insert_edge_by_vertex_names("Hupfingatsch", "Christkindl", 1),
                              ".insert_edge_by_vertex_names(): inserting an edge in a graph a single vertex did not "
                              "return None.")

        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_edges(self):
        try:
            g = Graph()
            v_linz = g.insert_vertex("Linz")
            v_wien = g.insert_vertex("Wien")
            v_graz = g.insert_vertex("Graz")

            str_graph = "[\"Linz\",\"Wien\",\"Graz\"]"
            g.insert_edge_by_vertex_names("Linz", "Wien", 100)
            edges = g.get_edges()
            self.assertEqual(1, len(edges),
                             ".get_edges() returns list with wrong size for the graph " + str_graph +
                             " and 1 inserted edge.")

            # as we have an undirected graph, we also have to test for a possible edge in opposite direction
            self.assertTrue((v_wien == edges[0].first_vertex and v_linz == edges[0].second_vertex) or
                            (v_wien == edges[0].second_vertex and v_linz == edges[0].first_vertex),
                            ".get_edges(): Did not find correct edge at index 0 after inserting the first edge ("
                            "\"Wien\",\"Linz\",100) in the graph " + str_graph + ".")
            self.assertEqual(100, edges[0].weight,
                             ".get_edges(): The first inserted edge (\"Wien\",\"Linz\",100) in the graph " + str_graph +
                             " has wrong weight: ")

            g.insert_edge_by_vertex_names("Wien", "Graz", 50)
            edges = g.get_edges()
            self.assertEqual(2, len(edges),
                             ".get_edges() returns array with wrong size for the graph " + str_graph +
                             " and 2 inserted edges.")

            # as we have an undirected graph, we also have to test for a possible edge in opposite direction
            self.assertTrue((v_wien == edges[0].first_vertex and v_linz == edges[0].second_vertex) or
                            (v_wien == edges[0].second_vertex and v_linz == edges[0].first_vertex),
                            ".get_edges(): Did not find correct edge at index 0 after inserting the first edge ("
                            "\"Wien\",\"Linz\",100) in the graph " + str_graph + ".")
            self.assertEqual(100, edges[0].weight,
                             ".get_edges(): The first inserted edge (\"Wien\",\"Linz\",100) in the graph " + str_graph +
                             " has wrong weight: ")

            self.assertTrue((v_graz == edges[1].first_vertex and v_wien == edges[1].second_vertex) or
                            (v_graz == edges[1].second_vertex and v_wien == edges[1].first_vertex),
                            ".get_edges(): Did not find correct edge at index 1 after inserting the 2nd edge ("
                            "\"Wien\",\"Graz\",50) in the graph " + str_graph + ".")
            self.assertEqual(50, edges[1].weight,
                             ".get_edges(): The 2nd inserted edge (\"Wien\",\"Graz\",50) in the graph " + str_graph +
                             " has wrong weight: ")



        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_number_of_vertices(self):
        try:
            g = self._initialize_large_graph()
            self.assertEqual(18, g.get_number_of_vertices())
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_vertices_large(self):
        try:
            g = self._initialize_large_graph()
            v = g.get_vertices()
            str_graph = "[\"Linz\",\"St.Poelten\",\"Wien\",\"Innsbruck\",\"Bregenz\",\"Eisenstadt\",\"Graz\"," \
                        "\"Klagenfurt\",\"Salzburg\",\"A\",\"B\",\"C\",\"D\",\"E\",\"F\",\"G\",\"H\",\"I\"] "
            self.assertEqual(18, len(v),
                             ".get_vertices() returned array of wrong size for the graph with vertices " + str_graph)

            self.assertTrue(v[0].name == "Linz",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Linz\" should be at index 0.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[1].name == "St.Poelten",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"St.Poelten\" should be at index 1.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[2].name == "Wien",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Wien\" should be at index 2.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[3].name == "Innsbruck",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Innsbruck\" should be at index 3.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[4].name == "Bregenz",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Bregenz\" should be at index 4.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[5].name == "Eisenstadt",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Eisenstadt\" should be at index 5.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[6].name == "Graz",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Graz\" should be at index 6.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[7].name == "Klagenfurt",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Klagenfurt\" should be at index 7.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[8].name == "Salzburg",
                            ".get_vertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"Salzburg\" should be at index 8.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[9].name == "A",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"A\" should be at index 9.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[10].name == "B",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"B\" should be at index 10.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[11].name == "C",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"C\" should be at index 11.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[12].name == "D",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"D\" should be at index 12.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[13].name == "E",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"E\" should be at index 13.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[14].name == "F",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"F\" should be at index 14.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[15].name == "G",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"G\" should be at index 15.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[16].name == "H",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"H\" should be at index 16.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
            self.assertTrue(v[17].name == "I",
                            ".getVertices(): For the graph with the vertices " + str_graph
                            + " the vertex \"I\" should be at index 17.\n"
                            + "\tYour vertices array is: " + self._print_vertices_array(g))
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_has_edge_for_undirected_graph(self):
        try:
            g = self._initialize_large_graph()
            str_edges = "(v1,v2,weight) [(0,2,1),(2,5,2),(2,6,3),(6,7,4),(4,3,5),(7,3,6),(8,3,7),(8,10,8),(7,11,9)," \
                        "(1,9,10),(10,9,11),(13,14,12),(14,15,13),(15,16,14),(16,12,15),(16,17,16)] "

            self.assertEqual(1, g.find_edge(g.vertices[0], g.vertices[2]).weight,
                             ".find_edge() returned a wrong weight for the edge (0,2) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)

            self.assertEqual(2, g.find_edge(g.vertices[2], g.vertices[5]).weight,
                             ".find_edge() returned a wrong weight for the edge (2,5) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(3, g.find_edge(g.vertices[2], g.vertices[6]).weight,
                             ".find_edge() returned a wrong weight for the edge (2,6) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(4, g.find_edge(g.vertices[6], g.vertices[7]).weight,
                             ".find_edge() returned a wrong weight for the edge (6,7) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(5, g.find_edge(g.vertices[4], g.vertices[3]).weight,
                             ".find_edge() returned a wrong weight for the edge (4,3) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(7, g.find_edge(g.vertices[8], g.vertices[3]).weight,
                             ".find_edge() returned a wrong weight for the edge (8,3) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(8, g.find_edge(g.vertices[8], g.vertices[10]).weight,
                             ".find_edge() returned a wrong weight for the edge (8,10) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(11, g.find_edge(g.vertices[10], g.vertices[9]).weight,
                             ".find_edge() returned a wrong weight for the edge (10,9) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(9, g.find_edge(g.vertices[7], g.vertices[11]).weight,
                             ".find_edge() returned a wrong weight for the edge (7,11) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(15, g.find_edge(g.vertices[16], g.vertices[12]).weight,
                             ".find_edge() returned a wrong weight for the edge (16,12) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_has_edge_for_undirected_graph_with_opposites(self):
        try:
            g = self._initialize_large_graph()
            str_edges = "(v1,v2,weight) [(0,2,1),(2,5,2),(2,6,3),(6,7,4),(4,3,5),(7,3,6),(8,3,7),(8,10,8),(7,11,9)," \
                        "(1,9,10),(10,9,11),(13,14,12),(14,15,13),(15,16,14),(16,12,15),(16,17,16)] "

            self.assertEqual(1, g.find_edge(g.vertices[2], g.vertices[0]).weight,
                             ".find_edge() returned a wrong weight for the edge (0,2) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)

            self.assertEqual(2, g.find_edge(g.vertices[5], g.vertices[2]).weight,
                             ".find_edge() returned a wrong weight for the edge (2,5) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(3, g.find_edge(g.vertices[6], g.vertices[2]).weight,
                             ".find_edge() returned a wrong weight for the edge (2,6) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(4, g.find_edge(g.vertices[7], g.vertices[6]).weight,
                             ".find_edge() returned a wrong weight for the edge (6,7) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(5, g.find_edge(g.vertices[3], g.vertices[4]).weight,
                             ".find_edge() returned a wrong weight for the edge (4,3) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(7, g.find_edge(g.vertices[3], g.vertices[8]).weight,
                             ".find_edge() returned a wrong weight for the edge (8,3) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(8, g.find_edge(g.vertices[10], g.vertices[8]).weight,
                             ".find_edge() returned a wrong weight for the edge (8,10) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(11, g.find_edge(g.vertices[9], g.vertices[10]).weight,
                             ".find_edge() returned a wrong weight for the edge (10,9) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(9, g.find_edge(g.vertices[11], g.vertices[7]).weight,
                             ".find_edge() returned a wrong weight for the edge (7,11) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
            self.assertEqual(15, g.find_edge(g.vertices[12], g.vertices[16]).weight,
                             ".find_edge() returned a wrong weight for the edge (16,12) \n\t of the graph "
                             + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_has_edge_for_undirected_graph_with_not_existing_edges(self):
        try:
            g = self._initialize_large_graph()
            str_edges = "(v1,v2,weight) [(0,2,1),(2,5,2),(2,6,3),(6,7,4),(4,3,5),(7,3,6),(8,3,7),(8,10,8),(7,11,9)," \
                        "(1,9,10),(10,9,11),(13,14,12),(14,15,13),(15,16,14),(16,12,15),(16,17,16)] "

            self.assertIsNone(g.find_edge(g.vertices[2], g.vertices[10]),
                              ".find_edge() returned a wrong weight for the not existing edge (2,10) \n\t of the graph "
                              + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)

            self.assertIsNone(g.find_edge(g.vertices[5], g.vertices[0]),
                              ".find_edge() returned a wrong weight for the not existing edge (5,0) \n\t of the graph "
                              + self._print_vertices_array(g) + "\n\t with the edges " + str_edges)
        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_get_adjacency_matrix(self):
        try:
            g = self._initialize_large_graph()
            str_edges = "(v1,v2,weight) [(0,2,1),(2,5,2),(2,6,3),(6,7,4),(4,3,5),(7,3,6),(8,3,7),(8,10,8),(7,11,9)," \
                        "(1,9,10),(10,9,11),(13,14,12),(14,15,13),(15,16,14),(16,12,15),(16,17,16)] "
            expected_matrix = None

            if self.undirected_graph_flag:
                expected_matrix = self._expected_matrix_undirected_graph
            else:
                expected_matrix = self._expected_matrix_directed_graph

            matrix = g.get_adjacency_matrix()
            sb = ""
            print("\n[test_get_adjacency_matrix]")
            for i in range(0, len(matrix)):
                for j in range(0, len(matrix)):
                    if matrix[i][j] != expected_matrix[i][j]:
                        sb += "\tError @ matrix position: " + str(i) + "," + str(j) + "\n"

            self.assertTrue(len(sb) == 0,
                            ".get_adjacency_matrix() failed \n\tfor the graph " + self._print_vertices_array(g) +
                            "\n\twith the edges " + str_edges + "\n\tat the following positions:\n" + sb)

        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    def test_num_len_vertices_of_undirected_graph(self):
        try:
            g = self._initialize_large_graph()
            str_edges = "(v1,v2,weight) [(0,2,1),(2,5,2),(2,6,3),(6,7,4),(4,3,5),(7,3,6),(8,3,7),(8,10,8),(7,11,9)," \
                        "(1,9,10),(10,9,11),(13,14,12),(14,15,13),(15,16,14),(16,12,15),(16,17,16)] "

            v0 = g.get_adjacent_vertices(g.vertices[0])
            self.assertEqual(1, len(v0), ".get_adjacent_vertices() failed for vertex with index 0 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")

            v1 = g.get_adjacent_vertices(g.vertices[1])
            self.assertEqual(1, len(v1), ".get_adjacent_vertices() failed for vertex with index 1 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v2 = g.get_adjacent_vertices(g.vertices[2])
            self.assertEqual(3, len(v2), ".get_adjacent_vertices() failed for vertex with index 2 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v3 = g.get_adjacent_vertices(g.vertices[3])
            self.assertEqual(3, len(v3), ".get_adjacent_vertices() failed for vertex with index 3 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v4 = g.get_adjacent_vertices(g.vertices[4])
            self.assertEqual(1, len(v4), ".get_adjacent_vertices() failed for vertex with index 4 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v5 = g.get_adjacent_vertices(g.vertices[5])
            self.assertEqual(1, len(v5), ".get_adjacent_vertices() failed for vertex with index 5 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v6 = g.get_adjacent_vertices(g.vertices[6])
            self.assertEqual(2, len(v6), ".get_adjacent_vertices() failed for vertex with index 6 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v7 = g.get_adjacent_vertices(g.vertices[7])
            self.assertEqual(3, len(v7), ".get_adjacent_vertices() failed for vertex with index 7 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v8 = g.get_adjacent_vertices(g.vertices[8])
            self.assertEqual(2, len(v8), ".get_adjacent_vertices() failed for vertex with index 8 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")

            v9 = g.get_adjacent_vertices(g.vertices[9])
            self.assertEqual(2, len(v9), ".get_adjacent_vertices() failed for vertex with index 9 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v10 = g.get_adjacent_vertices(g.vertices[10])
            self.assertEqual(2, len(v10), ".get_adjacent_vertices() failed for vertex with index 10 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v11 = g.get_adjacent_vertices(g.vertices[11])
            self.assertEqual(1, len(v11), ".get_adjacent_vertices() failed for vertex with index 11 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v12 = g.get_adjacent_vertices(g.vertices[12])
            self.assertEqual(1, len(v12), ".get_adjacent_vertices() failed for vertex with index 12 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v13 = g.get_adjacent_vertices(g.vertices[13])
            self.assertEqual(1, len(v13), ".get_adjacent_vertices() failed for vertex with index 13 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v14 = g.get_adjacent_vertices(g.vertices[14])
            self.assertEqual(2, len(v14), ".get_adjacent_vertices() failed for vertex with index 14 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v15 = g.get_adjacent_vertices(g.vertices[15])
            self.assertEqual(2, len(v15), ".get_adjacent_vertices() failed for vertex with index 15 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v16 = g.get_adjacent_vertices(g.vertices[16])
            self.assertEqual(3, len(v16), ".get_adjacent_vertices() failed for vertex with index 16 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")
            v17 = g.get_adjacent_vertices(g.vertices[17])
            self.assertEqual(1, len(v17), ".get_adjacent_vertices() failed for vertex with index 17 " +
                             "\n\tof the graph " + self._print_vertices_array(g) +
                             "\n\twith the edges " + str_edges + "\n\n\t")



        except Exception as e:
            if not isinstance(e, AssertionError):
                self.fail("Could not test as an exception has been thrown: " + str(e))
            else:
                self.fail("The following error occurred during testing: " + str(e))

    """ValueError tests"""

    def test_insert_vertex_with_none_parameter(self):
        try:
            g = Graph()
            g.insert_vertex(None)
        except Exception as e:
            self.assertTrue(isinstance(e, ValueError), ".insert_vertex() did not throw a ValueError in case of "
                                                       "passing None as parameter.")

    def test_find_vertex_with_none_parameter(self):
        try:
            g = Graph()
            g.find_vertex(None)

        except Exception as e:
            self.assertTrue(isinstance(e, ValueError), ".find_vertex() did not throw a ValueError in case of "
                                                       "passing None as parameter.")

    def test_insert_edge_with_none_parameter(self):
        g = Graph()
        v_linz = g.insert_vertex("Linz")
        with self.assertRaises(ValueError) as cm:
            g.insert_edge(None, v_linz, 1)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.insert_edge(v_linz, None, 1)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.insert_edge_by_vertex_names(None, "Linz", 1)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge_by_vertex_names() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.insert_edge_by_vertex_names("Linz", None, 1)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge_by_vertex_names() did not throw a ValueError in case of "
                        "passing None as parameter.")

    def test_find_edge_none_parameter(self):
        g = Graph()
        v_linz = g.insert_vertex("Linz")
        with self.assertRaises(ValueError) as cm:
            g.find_edge(None, v_linz)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".find_edge() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.find_edge(v_linz, None)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".find_edge() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.find_edge_by_vertex_names(None, "Linz")
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".find_edge_by_vertex_names() did not throw a ValueError in case of "
                        "passing None as parameter.")

        with self.assertRaises(ValueError) as cm:
            g.find_edge_by_vertex_names("Linz", None)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".find_edge_by_vertex_names() did not throw a ValueError in case of "
                        "passing None as parameter.")

    def test_insert_edge_loop(self):
        g = Graph()
        v_linz = g.insert_vertex("Linz")

        with self.assertRaises(ValueError) as cm:
            g.insert_edge_by_vertex_names("Linz", "Linz", 0)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge_by_vertex_names() did not throw a ValueError in case of "
                        "inserting a loop.")

        with self.assertRaises(ValueError) as cm:
            g.insert_edge(v_linz, v_linz, 0)
        self.assertTrue(isinstance(cm.exception, ValueError),
                        ".insert_edge() did not throw a ValueError in case of "
                        "inserting a loop.")



    """Helper functions"""

    def _initialize_large_graph(self):
        g = Graph()
        v_linz = g.insert_vertex("Linz")
        v_stpoelten = g.insert_vertex("St.Poelten")
        v_wien = g.insert_vertex("Wien")
        v_innsbruck = g.insert_vertex("Innsbruck")
        v_bregenz = g.insert_vertex("Bregenz")
        v_eisenstadt = g.insert_vertex("Eisenstadt")
        v_graz = g.insert_vertex("Graz")
        v_klagenfurt = g.insert_vertex("Klagenfurt")
        v_salzburg = g.insert_vertex("Salzburg")
        g.insert_edge(v_linz, v_wien, 1)
        g.insert_edge(v_wien, v_eisenstadt, 2)
        g.insert_edge(v_wien, v_graz, 3)
        g.insert_edge(v_graz, v_klagenfurt, 4)
        g.insert_edge(v_bregenz, v_innsbruck, 5)
        g.insert_edge(v_klagenfurt, v_innsbruck, 6)
        g.insert_edge(v_salzburg, v_innsbruck, 7)
        v_a = g.insert_vertex("A")
        v_b = g.insert_vertex("B")
        v_c = g.insert_vertex("C")
        v_d = g.insert_vertex("D")
        v_e = g.insert_vertex("E")
        v_f = g.insert_vertex("F")
        v_g = g.insert_vertex("G")
        v_h = g.insert_vertex("H")
        v_i = g.insert_vertex("I")
        g.insert_edge(v_salzburg, v_b, 8)
        g.insert_edge(v_klagenfurt, v_c, 9)
        g.insert_edge(v_stpoelten, v_a, 10)
        g.insert_edge(v_b, v_a, 11)
        g.insert_edge(v_e, v_f, 12)
        g.insert_edge(v_f, v_g, 13)
        g.insert_edge(v_g, v_h, 14)
        g.insert_edge(v_h, v_d, 15)
        g.insert_edge(v_h, v_i, 16)

        try:
            g.insert_edge(v_i, v_i, 1)
        except Exception as ve:
            self.assertTrue(isinstance(ve, ValueError))

        return g

    def _initialize_graph_2_components(self):
        g = Graph()
        linz = g.insert_vertex("Linz")
        stpoelten = g.insert_vertex("St.Poelten")
        wien = g.insert_vertex("Wien")
        innsbruck = g.insert_vertex("Innsbruck")
        bregenz = g.insert_vertex("Bregenz")
        eisenstadt = g.insert_vertex("Eisenstadt")
        graz = g.insert_vertex("Graz")
        klagenfurt = g.insert_vertex("Klagenfurt")
        salzburg = g.insert_vertex("Salzburg")
        g.insert_edge(linz, wien, 1)
        g.insert_edge(wien, eisenstadt, 2)
        g.insert_edge(wien, graz, 3)
        g.insert_edge(graz, klagenfurt, 4)
        g.insert_edge(bregenz, innsbruck, 5)
        g.insert_edge(klagenfurt, innsbruck, 6)
        g.insert_edge(salzburg, innsbruck, 7)
        london = g.insert_vertex("London")
        g.insert_edge(stpoelten, london, 10)
        return g

    def _print_vertices_array(self, g):
        sb = ""
        v = g.get_vertices()
        sb += "["
        for i in range(0, len(v)):
            sb = str(i) + "=\"" + v[i].name + "\","
        return sb + "]"


if __name__ == '__main__':
    unittest.main()
