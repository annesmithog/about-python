Item = list[int]

def merge_sort(items: Item) -> Item:
    """分割統治法を利用した安定したソートです。
    Args:
        items (Item): 配列
    Returns:
        Item: ソートした配列
    """
    if len(items) <= 1:
        return items

    mid = len(items) // 2
    left = merge_sort(items[:mid])
    right = merge_sort(items[mid:])
    return merge(left, right)

def merge(left: Item, right: Item) -> Item:
    result: Item = []
    i = 0
    j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result
