from typing import Any

def greedy_coin_change(amount: int, coins: list[int]) -> list[Any]:
    coins = sorted(coins, reverse=True)
    result: list[int] = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    if amount == 0:
        return result

    return []