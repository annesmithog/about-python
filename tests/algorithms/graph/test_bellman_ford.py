from src.algorithms.graph.bellman_ford import bellman_ford, Edges, NegativeCycleError
import unittest

class TestBellmanFord(unittest.TestCase):
    def test_simple_graph(self):
        vertices = ["Tokyo", "Shinagawa", "Yokohama", "Omiya"]
        edges: Edges = [
            {"u": "Tokyo",     "v": "Shinagawa", "w": 5},
            {"u": "Tokyo",     "v": "Omiya",     "w": 20},
            {"u": "Shinagawa", "v": "Yokohama",  "w": 8},
            {"u": "Omiya",     "v": "Yokohama",  "w": 5},
        ]
        dist = bellman_ford(edges, vertices, "Tokyo")
        self.assertEqual(dist["Shinagawa"], 5)
        self.assertEqual(dist["Yokohama"], 13)
        self.assertEqual(dist["Omiya"], 20)

    def test_negative_edge(self):
        vertices = ["A", "B", "C"]
        edges: Edges = [
            {"u": "A", "v": "B", "w": 6},
            {"u": "A", "v": "C", "w": 5},
            {"u": "B", "v": "C", "w": -2},
        ]
        dist = bellman_ford(edges, vertices, "A")
        self.assertEqual(dist["B"], 6)
        self.assertEqual(dist["C"], 4)

    def test_negative_cycle(self):
        vertices = ["X", "Y"]
        edges: Edges = [
            {"u": "X", "v": "Y", "w": 1},
            {"u": "Y", "v": "X", "w": -2},
        ]
        with self.assertRaises(NegativeCycleError):
            bellman_ford(edges, vertices, "X")
