from typing import Any

def greedy_coin_change(amount: int, coins: list[int]) -> list[Any]:
    """その場で最適な選択を繰り返し解を求める"""
    coins = sorted(coins, reverse=True)
    result: list[int] = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    if amount == 0:
        return result

    return []