DistanceMatrix = dict[str, dict[str, float]]

def floyd_warshall(dist: DistanceMatrix) -> DistanceMatrix:
    """全ての頂点間の最短経路を求めて返します。
    Args:
        dist (DistanceMatrix): 各地点と各地点への経路
    Returns:
        DistanceMatrix: 各地点と各地点への最短経路
    """
    vertices: list[str] = list(dist.keys())

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
