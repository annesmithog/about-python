from src.algorithms.graph.dijkstra import dijkstra, Graph
import unittest
import math

class TestDijkstra(unittest.TestCase):
    def test_simple_graph(self):
        graph: Graph = {
            "Tokyo":     {"Shinagawa": 5, "Ueno": 7},
            "Shinagawa": {"Tokyo": 5, "Yokohama": 8},
            "Ueno":      {"Tokyo": 7, "Omiya": 6},
            "Yokohama":  {"Shinagawa": 8, "Omiya": 15},
            "Omiya":     {"Ueno": 6, "Yokohama": 15},
        }
        dist = dijkstra(graph, "Tokyo")
        self.assertEqual(dist["Shinagawa"], 5)
        self.assertEqual(dist["Ueno"], 7)
        self.assertEqual(dist["Yokohama"], 13)
        self.assertEqual(dist["Omiya"], 13)

    def test_unreachable_node(self):
        graph: Graph = {
            "A": {"B": 1},
            "B": {"A": 2},
            "C": {},
        }
        dist = dijkstra(graph, "A")
        self.assertEqual(dist["C"], math.inf)
