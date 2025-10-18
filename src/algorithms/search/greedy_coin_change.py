from typing import Any

def greedy_coin_change(amount: int, coins: list[int]) -> list[Any]:
    """その場で最適な選択を繰り返し、解を求めます。コイン問題では、用意されたコインの種類と求める合計をもとに必要なコインの種類を返します。
    Args:
        amount (int): 求める合計
        coins (list[int]): コインの種類を格納した配列
    Returns:
        list[Any]: 使用したコインの配列
    """
    coins = sorted(coins, reverse=True)
    result: list[int] = []

    for coin in coins:
        while amount >= coin:
            amount -= coin
            result.append(coin)

    if amount == 0:
        return result

    return []
