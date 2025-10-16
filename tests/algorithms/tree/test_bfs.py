from src.algorithms.tree.bfs import bfs
import unittest

class TestBfs(unittest.TestCase):
    def test_simple_graph(self):
        graph: dict[str, list[str]] = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": ["F"],
            "F": [],
        }
        result = bfs(graph, "A")
        expected = ["A", "B", "C", "D", "E", "F"]
        self.assertEqual(expected, result)

    def test_disconnected_graph(self):
        graph: dict[str, list[str]] = {
            "A": ["B"],
            "B": [],
            "C": ["D"],
            "D": [],
        }
        result = bfs(graph, "A")
        expected = ["A", "B"]
        self.assertEqual(expected, result)

    def test_single_node(self):
        graph: dict[str, list[str]] = {
            "X": []
        }
        result = bfs(graph, "X")
        expected = ["X"]
        self.assertEqual(expected, result)
