import heapq

Graph = dict[str, dict[str, float]]
Edge = tuple[float, str, str]
Visited = set[str]
Mst = list[tuple[str, str, float]]
Pq = list[Edge]

def prim(graph: Graph, start: str) -> Mst:
    """貪欲法で最小全域木を求めて返します。
    Args:
        graph (Graph): グラフ
        start (str): スタート地点
    Returns:
        Mst: 最小全域木
    """
    mst: Mst = []
    visited: Visited = {start}
    pq: Pq = []

    for v, w in graph[start].items():
        heapq.heappush(pq, (w, start, v))

    while pq:
        w, u, v = heapq.heappop(pq)
        if v in visited:
            continue

        visited.add(v)
        mst.append((u, v, w))

        for to, weight in graph[v].items():
            if to not in visited:
                heapq.heappush(pq, (weight, v, to))

    return mst
