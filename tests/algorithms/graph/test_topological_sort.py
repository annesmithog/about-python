from src.algorithms.graph.topological_sort import topological_sort, CycleError, Graph
import unittest

class TestTopologicalSort(unittest.TestCase):
    def test_simple_dag(self):
        graph: Graph = {
            "A": ["B", "C"],
            "B": ["D"],
            "C": ["D"],
            "D": [],
        }
        order = topological_sort(graph)
        self.assertEqual(len(order), 4)
        self.assertLess(order.index("A"), order.index("B"))
        self.assertLess(order.index("A"), order.index("C"))
        self.assertLess(order.index("B"), order.index("D"))
        self.assertLess(order.index("C"), order.index("D"))

    def test_independent_nodes(self):
        graph: Graph = {
            "A": [],
            "B": [],
            "C": [],
        }
        order = topological_sort(graph)
        self.assertEqual(sorted(order), ["A", "B", "C"])

    def test_chain_graph(self):
        graph: Graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["D"],
            "D": [],
        }
        order = topological_sort(graph)
        self.assertEqual(order, ["A", "B", "C", "D"])

    def test_graph_with_cycle_throws_exception(self):
        graph: Graph = {
            "A": ["B"],
            "B": ["C"],
            "C": ["A"],
        }
        with self.assertRaises(CycleError) as context:
            topological_sort(graph)
        self.assertEqual(str(context.exception), "閉路あり")
