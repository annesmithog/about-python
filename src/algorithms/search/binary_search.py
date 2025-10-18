def binary_search(items: list[int], target: int) -> int:
    """ソート済みの配列を二分しながら、効率的に要素を探し目的の要素の位置を返します。
    Args:
        items (list[int]): 調査する配列
        target (int): 目的の要素
    Returns:
        int: 目的の要素の位置
    """
    left: int = 0
    right: int = len(items) - 1

    while left <= right:
        mid: int = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1
