from src.algorithms.search.linear_search import linear_search
import unittest

class TestLinearSearch(unittest.TestCase):
    def test_found_element(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(2, linear_search(arr, 30))

    def test_not_found_element(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(-1, linear_search(arr, 31))

    def test_first_element(self):
        arr = [10, 20, 30]
        self.assertEqual(0, linear_search(arr, 10))

    def test_last_element(self):
        arr = [10, 20, 30]
        self.assertEqual(2, linear_search(arr, 30))

    def test_empty_array(self):
        arr = []
        self.assertEqual(-1, linear_search(arr, 10)) # type: ignore
