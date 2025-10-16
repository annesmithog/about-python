from src.algorithms.search.exponential_search import exponential_search
import unittest

class TestExponentialSearch(unittest.TestCase):
    def test_found_element(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(2, exponential_search(arr, 30))
    
    def test_not_found_element(self):
        arr = [10, 20, 30, 40, 50]
        self.assertEqual(-1, exponential_search(arr, 31))

    def test_first_element(self):
        arr = [10, 20, 30]
        self.assertEqual(0, exponential_search(arr, 10))

    def test_last_element(self):
        arr = [10, 20, 30]
        self.assertEqual(2, exponential_search(arr, 30))

    def test_empty_array(self):
        arr = []
        self.assertEqual(-1, exponential_search(arr, 10)) # type: ignore
