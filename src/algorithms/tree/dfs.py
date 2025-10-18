Graph = dict[str, list[str]]
Visited = set[str] | None
Order = list[str] | None

def dfs(graph: Graph, start: str, visited: Visited, order: Order) -> list[str]:
    """スタックや再帰を使用してできる限り深く探索し、到達可能な経路を返します。
    Args:
        graph (dict[str, list[str]]): 調査するグラフ
        start (str): スタート地点
        visited (set[str] | None): 訪問済み
        order (list[str] | None): 到達可能な経路
    Returns:
        list[str]: 到達可能な経路
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []

    visited.add(start)
    order.append(start)

    for neighbor in graph[start]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)

    return order
