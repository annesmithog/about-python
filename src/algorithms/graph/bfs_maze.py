from collections import deque

def bfs_maze(maze: list[list[str]], height: int, width: int) -> int:
    """BFSを使い、最短経路を見つける"""
    start = None
    goal = None

    for i in range(height):
        for j in range(width):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        raise ValueError("スタート(S)またはゴール(G)が存在しません。")
    
    queue = deque([(start[0], start[1], 0)])    # y, x, distance
    visited = [[False] * width for _ in range(height)]
    visited[start[0]][start[1]] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while queue:
        y, x, d = queue.popleft()

        if (y, x) == goal:
            return d
        
        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < height and 0 <= nx < width:
                if not visited[ny][nx] and maze[ny][nx] != "#":
                    visited[ny][nx] = True
                    queue.append((ny, nx, d + 1))

    return -1
