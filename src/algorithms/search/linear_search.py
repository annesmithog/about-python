def linear_search(items: list[int], target: int) -> int:
    """配列を先頭から順番に調べて目的の要素を探す"""
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
