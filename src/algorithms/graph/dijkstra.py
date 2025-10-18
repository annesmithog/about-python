from typing import Mapping, MutableMapping, Tuple
import heapq
import math

Graph = Mapping[str, Mapping[str, float]]

def dijkstra(graph: Graph, start: str) -> MutableMapping[str, float]:
    """単一の始点から各頂点への最短経路を求める (負の辺がない場合のみ)"""
    dist: MutableMapping[str, float] = {node: math.inf for node in graph}
    dist[start] = 0.0

    pq: list[Tuple[float, str]] = [(0.0, start)]

    while pq:
        current_dist, u = heapq.heappop(pq)

        if current_dist > dist[u]:
            continue

        for v, weight in graph[u].items():
            alt = dist[u] + weight
            if alt < dist[v]:
                dist[v] = alt
                heapq.heappush(pq, (alt, v))

    return dist
