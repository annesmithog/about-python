from src.algorithms.graph.prim import prim, Graph
import unittest

class TestPrim(unittest.TestCase):
    def test_simple_graph(self):
        graph: Graph = {
            "A": {"B": 1, "C": 3},
            "B": {"A": 1, "C": 1, "D": 6},
            "C": {"A": 3, "B": 1, "D": 4},
            "D": {"B": 6, "C": 4},
        }
        mst = prim(graph, "A")
        self.assertEqual(len(mst), 3)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 6)  # 1 + 1 + 4 = 6

    def test_graph_with_extra_edges(self):
        graph: Graph = {
            "A": {"B": 10, "D": 50},
            "B": {"A": 10, "C": 1},
            "C": {"B": 1, "D": 2},
            "D": {"A": 50, "C": 2},
        }
        mst = prim(graph, "A")
        self.assertEqual(len(mst), 3)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 13)

    def test_graph_with_isolated_vertex(self):
        graph: Graph = {
            "A": {"B": 1},
            "B": {"A": 1, "C": 2},
            "C": {"B": 2},
            "D": {}
        }
        mst = prim(graph, "A")
        self.assertEqual(len(mst), 2)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 3)
