DistanceMatrix = dict[str, dict[str, float]]

def floyd_warshall(dist: DistanceMatrix) -> DistanceMatrix:
    """全ての頂点間の最短経路を求める"""
    vertices = list(dist.keys())

    for k in vertices:
        for i in vertices:
            for j in vertices:
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]
    
    return dist
