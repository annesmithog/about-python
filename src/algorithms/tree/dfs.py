def dfs(graph: dict[str, list[str]], start: str, visited: set[str] | None,order: list[str] | None) -> list[str]:
    """スタックや再帰を使い、できる限り深く探索する"""
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
