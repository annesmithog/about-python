import math
import heapq

Graph = dict[str, dict[str, int]]
Dist = dict[str, float]
Pq = list[tuple[float, str]]

def dijkstra(graph: Graph, start: str) -> Dist:
    """負の辺がない場合のみ、単一の始点から各頂点への最短経路を求めて、各地点への最短距離を返します。
    Args:
        graph (Graph): 調査するグラフ
        start (str): スタート地点
    Returns:
        Dist: 各地点とその地点への最短距離
    """
    dist: Dist = {node: math.inf for node in graph}
    dist[start] = 0.0
    pq: Pq = [(0.0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue

        for v, weight in graph[u].items():
            alt: float = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))

    return dist
