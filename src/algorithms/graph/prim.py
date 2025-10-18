import heapq

Graph = dict[str, dict[str, float]]
Edge = tuple[float, str, str]

def prim(graph: Graph, start: str) -> list[tuple[str, str, float]]:
    """貪欲方で最小全域木を求める"""
    mst: list[tuple[str, str, float]] = []
    visited: set[str] = {start}
    pq: list[Edge] = []

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
