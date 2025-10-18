from collections import deque

def bfs(graph: dict[str, list[str]], start: str) -> list[str]:
    """キューを使い、根から近い順に探索する"""
    visited: set[str] = set()
    queue: deque[str] = deque([start])
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
