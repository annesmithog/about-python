Item = list[int]

def shell_sort(items: Item) -> Item:
    """挿入ソートを改良し、間隔を縮めながら整列させるソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    n = len(items)
    gap = n // 2

    while 0 < gap:
        for i in range(gap, n):
            temp = items[i]
            j = i
            while gap <= j and temp < items[j - gap]:
                items[j] = items[j - gap]
                j -= gap
            items[j] = temp
        gap //= 2

    return items
