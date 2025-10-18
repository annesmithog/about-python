from src.algorithms.graph.floyd_warshall import floyd_warshall, DistanceMatrix
import unittest
import math

class TestFloydWarshall(unittest.TestCase):
    def test_simple_graph(self):
        INF = math.inf
        d: DistanceMatrix = {
            "A": {"A": 0, "B": 3, "C": INF},
            "B": {"A": INF, "B": 0, "C": 1},
            "C": {"A": 2, "B": INF, "C": 0},
        }
        expected: DistanceMatrix = {
            "A": {"A": 0, "B": 3, "C": 4},
            "B": {"A": 3, "B": 0, "C": 1},
            "C": {"A": 2, "B": 5, "C": 0},
        }
        result = floyd_warshall(d)
        self.assertEqual(result, expected)

    def test_already_optimal_graph(self):
        d: DistanceMatrix = {
            "X": {"X": 0, "Y": 5},
            "Y": {"X": math.inf, "Y": 0}
        }
        self.assertEqual(floyd_warshall(d), d)

    def test_isolated_node(self):
        INF = math.inf
        d: DistanceMatrix = {
            "A": {"A": 0, "B": 2, "C": INF},
            "B": {"A": 2, "B": 0, "C": INF},
            "C": {"A": INF, "B": INF, "C": 0},
        }
        expected: DistanceMatrix = {
            "A": {"A": 0, "B": 2, "C": INF},
            "B": {"A": 2, "B": 0, "C": INF},
            "C": {"A": INF, "B": INF, "C": 0},
        }
        result = floyd_warshall(d)
        self.assertEqual(result, expected)
