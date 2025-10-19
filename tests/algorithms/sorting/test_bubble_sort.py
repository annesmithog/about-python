from src.algorithms.sorting.bubble_sort import bubble_sort, Item
import unittest

class TestBubbleSort(unittest.TestCase):
    def test_sort_random_array(self):
        items: Item = [2, 5, 10, 4, 3, 9, 8, 1, 7, 6]
        result = bubble_sort(items)
        expected    = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertListEqual(result, expected)

    def test_already_sorted_array(self):
        items: Item    = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        result = bubble_sort(items)
        expected: Item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        self.assertListEqual(result, expected)

    def test_reverse_sorted_array(self):
        items: Item    = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = bubble_sort(items)
        expected: Item = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        self.assertListEqual(result, expected)

    def test_empty_array(self):
        items: Item = []
        result = bubble_sort(items)
        self.assertListEqual(result, [])

    def test_single_element_array(self):
        items: Item = [256]
        result = bubble_sort(items)
        self.assertListEqual(result, [256])

    def test_array_with_duplicates(self):
        items: Item    = [5, 4, 2, 2, 6, 1]
        result = bubble_sort(items)
        expected: Item = [1, 2, 2, 4, 5, 6]
        self.assertListEqual(result, expected)
