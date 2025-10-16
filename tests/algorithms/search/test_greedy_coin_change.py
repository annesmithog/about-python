from src.algorithms.search.greedy_coin_change import greedy_coin_change
import unittest

class TestGreedyCoinChange(unittest.TestCase):
    def test_exact_amount(self):
        coins = [500, 100, 50, 10, 5, 1]
        result = greedy_coin_change(888, coins)
        expected = [500, 100, 100, 100, 50, 10, 10, 10, 5, 1, 1, 1]
        self.assertListEqual(expected, result)

    def test_single_coin(self):
        coins = [100, 50, 10]
        result = greedy_coin_change(50, coins)
        self.assertListEqual([50], result)

    def test_no_solution(self):
        coins = [50, 10]
        result = greedy_coin_change(16, coins)
        self.assertListEqual([], result)

    def test_zero_amount(self):
        coins = [500, 100, 50, 10, 5, 1]
        result = greedy_coin_change(0, coins)
        self.assertListEqual([], result)
