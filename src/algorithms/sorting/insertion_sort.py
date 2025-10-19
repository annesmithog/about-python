Item = list[int]

def insertion_sort(items: Item) -> Item:
    """適切な位置を見つけて要素を挿入し、部分的に整列させるソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    n = len(items)

    for i in range(1, n):
        key = items[i]
        j = i - 1
        while(0 <= j and key < items[j]):
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = key

    return items
