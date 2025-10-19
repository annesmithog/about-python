Item = list[int]

def heap_sort(items: Item) -> Item:
    """ヒープ構造を利用する効率的なソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    n = len(items)
    for i in range(n // 2 - 1, -1, -1):
        heapify(items, n, i)

    for i in range(n - 1, 0, -1):
        items[0], items[i] = items[i], items[0]
        heapify(items, i, 0)

    return items

def heapify(items: Item, n: int, i: int) -> None:
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and items[largest] < items[left]:
        largest = left
    if right < n and items[largest] < items[right]:
        largest = right
    if largest != i:
        items[i], items[largest] = items[largest], items[i]
        heapify(items, n, largest)
