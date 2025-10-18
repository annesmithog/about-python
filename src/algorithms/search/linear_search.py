def linear_search(items: list[int], target: int) -> int:
    """配列を先頭から順番に調べ、目的の要素の位置を探します。
    Args:
        items (list[int]): 調査する配列
        target (int): 目的の要素
    Returns:
        int: 目的の要素の位置
    """
    for index, value in enumerate(items):
        if value == target:
            return index
    return -1
