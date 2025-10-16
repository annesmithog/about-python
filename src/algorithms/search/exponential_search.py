def exponential_search(items: list[int], target: int) -> int:
    n = len(items)
    
    if n == 0: 
        return -1
    if items[0] == target:
        return 0
    
    i = 1
    while i < n and items[i] <= target:
        i *= 2

    return binary_search_in_range(items, target, (i // 2), min(i, n - 1))

def binary_search_in_range(items: list[int], target: int, left: int, right: int) -> int:
    while left <= right:
        mid = (left + right) // 2
        if items[mid] == target:
            return mid
        elif items[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1