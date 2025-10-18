from typing import TypedDict
import math

Dist = dict[str, float]

class Edge(TypedDict):
    u: str
    v: str
    w: float

Edges = list[Edge]

class NegativeCycleError(Exception):
    """負閉路検出時にスローされる"""
    pass

def bellman_ford(edges: list[Edge], vertices: list[str], start: str) -> Dist:
    """負の辺があっても問題ないが負閉路の場合以外に限り、単一の始点から各頂点への最短経路を求めて、
        各地点への最短距離を返します。
    Args:
        edges (list[Edge]): エッジを含むグラフ
        vertices (list[str]): 各頂点
        start (str): スタート地点
    Raises:
        NegativeCycleError: 負閉路検出時にスローされる
    Returns:
        Dist: 各地点とその地点への最短経路
    """
    dist: Dist = {v: math.inf for v in vertices}
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
