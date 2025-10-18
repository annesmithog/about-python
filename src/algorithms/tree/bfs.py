from collections import deque

Graph = dict[str, list[str]]
Queue = deque[str]

def bfs(graph: Graph, start: str) -> list[str]:
    """キューを使用して与えられたノードから近いノードを順に探索し、最短経路を返します。
    Args:
        graph (dict[str, list[str]]): 調査するグラフ
        start (str): スタート地点
    Returns:
        list[str]: 最短経路
    """
    visited: set[str] = set()
    queue: Queue = deque([start])
    order: list[str] = []

    visited.add(start)

    while queue:
        node: str = queue.popleft()
        order.append(node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return order
