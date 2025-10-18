from typing import TypedDict
import math

class Edge(TypedDict):
    u: str
    v: str
    w: float

class NegativeCycleError(Exception):
    """負閉路検出時にスローされる"""
    pass

def bellman_ford(edges: list[Edge], vertices: list[str], start: str) -> dict[str, float]:
    """単一の始点から各頂点への最短経路を求める (負の辺があっても問題ないが、負閉路は不可)"""
    dist: dict[str, float] = {v: math.inf for v in vertices}
    dist[start] = 0.0

    n = len(vertices)

    for _ in range(n - 1):
        for edge in edges:
            u, v, w = edge["u"], edge["v"], edge["w"]
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w

    for edge in edges:
        u, v, w = edge["u"], edge["v"], edge["w"]
        if dist[u] + w < dist[v]:
            raise NegativeCycleError("負閉路が検出されました。")
    
    return dist
