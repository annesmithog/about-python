def binary_search(items: list[int], target: int) -> int:
    """ソート済みの配列を二分しながら効率的に要素を探す"""
    left = 0
    right = len(items) - 1

    while left <= right:
        mid = (left + right) // 2

        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1