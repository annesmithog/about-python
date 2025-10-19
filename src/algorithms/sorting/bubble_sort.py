Item = list[int | float]

def bubble_sort(items: Item) -> Item:
    """隣り合う要素を比較しながら必要に応じて入れ替えを繰り返すソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    n = len(items)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if items[j] > items[j + 1]:
                items[j], items[j + 1] = items[j + 1], items[j]

    return items
