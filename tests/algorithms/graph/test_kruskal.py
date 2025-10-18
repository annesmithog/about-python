from src.algorithms.graph.kruskal import kruskal
import unittest

class TestKruskal(unittest.TestCase):
    def test_simple_graph(self):
        edges = [
            (1, "A", "B"),
            (3, "A", "C"),
            (1, "B", "C"),
            (6, "B", "D"),
            (4, "C", "D")
        ]
        vertices = ["A", "B", "C", "D"]
        mst = kruskal(edges, vertices)
        self.assertEqual(len(mst), 3)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 6)

    def test_graph_with_extra_edges(self):
        edges = [
            (10, "A", "B"),
            (1, "B", "C"),
            (2, "C", "D"),
            (50, "A", "D"),
        ]
        vertices = ["A", "B", "C", "D"]
        mst = kruskal(edges, vertices)
        self.assertEqual(len(mst), 3)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 13)

    def test_graph_with_isolated_vertex(self):
        edges = [
            (1, "A", "B"),
            (2, "B", "C"),
        ]
        vertices = ["A", "B", "C", "D"]
        mst = kruskal(edges, vertices)
        self.assertEqual(len(mst), 2)
        total_weight = sum(edge[2] for edge in mst)
        self.assertEqual(total_weight, 3)