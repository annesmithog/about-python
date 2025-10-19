Item = list[int]

def selection_sort(items: Item) -> Item:
    """未ソート部分から最小または最大の要素を選び先頭と交換するソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    n = len(items)

    for i in range(n - 1):
        min_index = i
        for j in range(i + 1, n):
            if items[j] < items[min_index]:
                min_index = j
        items[i], items[min_index] = items[min_index], items[i]

    return items
