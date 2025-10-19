Item = list[int]

def radix_sort(items: Item) -> Item:
    """整数の各桁ごとに処理する安定したソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    if not items:
        return []

    max_val = max(items)
    exp = 1
    while 0 < max_val // exp:
        items = counting_sort_by_digit(items, exp)
        exp *= 10
    return items

def counting_sort_by_digit(items: Item, exp: int) -> Item:
    n = len(items)
    output = [0] * n
    count = [0] * 10

    for i in range(n):
        index = (items[i] // exp) % 10
        count[index]  += 1

    for i in range(1, 10):
        count[i] += count[i - 1]

    for i in range(n - 1, -1, -1):
        index = (items[i] // exp) % 10
        output[count[index] - 1] = items[i]
        count[index] -= 1

    return output
