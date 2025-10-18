Edge = tuple[float, str, str]

def kruskal(edges: list[Edge], vertices: list[str]) -> list[tuple[str, str, float]]:
    """辺が小さい順に選び最小全域木を求める"""
    edges = sorted(edges, key=lambda e: e[0])
    parent: dict[str, str] = {v: v for v in vertices}

    def find(v: str) -> str:
        if parent[v] != v:
            parent[v] = find(parent[v])
        return parent[v]
    
    def union(a: str, b: str) -> None:
        root_a = find(a)
        root_b = find(b)
        parent[root_a] = root_b

    mst: list[tuple[str, str, float]] = []

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst
