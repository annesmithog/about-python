Edge = tuple[float, str, str]
Edges = list[Edge]
Mst = list[tuple[str, str, float]]

def kruskal(edges: Edges, vertices: list[str]) -> Mst:
    """辺が小さい順に選び、最小全域木を求めて返します。
    Args:
        edges (Edges): エッジを含むグラフ
        vertices (list[str]): 各頂点
    Returns:
        Mst: 最小全域木
    """
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

    mst: Mst = []

    for w, u, v in edges:
        if find(u) != find(v):
            union(u, v)
            mst.append((u, v, w))

    return mst
