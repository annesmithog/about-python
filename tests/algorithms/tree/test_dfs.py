from src.algorithms.tree.dfs import dfs
import unittest

class TestDfs(unittest.TestCase):
    def test_simple_graph(self):
        graph: dict[str, list[str]] = {
            "A": ["B", "C"],
            "B": ["D", "E"],
            "C": ["F"],
            "D": [],
            "E": ["F"],
            "F": [],
        }
        result = dfs(graph, "A", None, None)
        expected = ["A", "B", "C", "D", "E", "F"]
        self.assertListEqual(sorted(expected), sorted(result))
