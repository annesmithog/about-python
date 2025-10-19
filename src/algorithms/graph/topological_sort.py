from collections import deque

class CycleError(Exception):
    """閉路検出時にスローされる"""
    pass

Graph = dict[str, list[str]]

def topological_sort(graph: Graph) -> list[str]:
    """有向非巡回グラフのノードを依存関係に従って並べて返します。
    Args:
        graph (Graph): グラフ
    Raises:
        CycleError: 閉路検出時にスローされる
    Returns:
        list[str]: グラフ
    """
    in_degree: dict[str, int] = {u: 0 for u in graph}
    for u, neighbors in graph.items():
        for v in neighbors:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue: deque[str] = deque([node for node, deg in in_degree.items() if deg == 0])
    order: list[str] = []

    while queue:
        u = queue.popleft()
        order.append(u)

        for v in graph.get(u, []):
            in_degree[v] -= 1
            if in_degree[v] == 0:
                queue.append(v)

    if len(order) != len(in_degree):
        raise CycleError("閉路あり")

    return order
