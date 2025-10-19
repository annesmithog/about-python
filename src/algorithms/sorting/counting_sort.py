Item = list[int]

def counting_sort(items: Item) -> Item:
    """値の範囲が限られている場合に有効な非比較ソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    if not items:
        return []

    min_val = min(items)
    max_val = max(items)
    range_val = max_val - min_val + 1

    count = [0] * range_val
    for num in items:
        count[num - min_val] += 1

    output: Item = []
    for i in range(range_val):
        while 0 < count[i]:
            output.append(i + min_val)
            count[i] -= 1

    return output
