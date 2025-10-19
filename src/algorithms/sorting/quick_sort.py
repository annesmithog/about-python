Item = list[int]

def quick_sort(items: Item) -> Item:
    """分割統治法を利用した不安定で高速なソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    if len(items) < 2:
        return items

    pivot = items[0]
    left = [x for x in items[1:] if x <= pivot]
    right = [x for x in items[1:] if pivot < x]
    return quick_sort(left) + [pivot] + quick_sort(right)
