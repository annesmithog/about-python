def linear_search(items: list[int], target: int) -> int:
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
