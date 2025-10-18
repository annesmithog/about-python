def dfs_maze(maze: list[list[str]], height: int, width: int) -> int:
    """DFSを使い、到達可能な経路を見つける"""
    start = None
    goal = None

    for i in range(height):
        for j in range(width):
            if maze[i][j] == "S":
                start = (i, j)
            if maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        raise ValueError("スタート(S)またはゴール(G)が存在しません。")
    
    visited = [[False] * width for _ in range(height)]
    visited[start[0]][start[1]] = True

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    found_distance = [-1]
    def dfs(y: int, x: int, d: int) -> bool:
        if (y, x) == goal:
            found_distance[0] = d
            return True
        
        visited[y][x] = True

        for dy, dx in directions:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < height and 0 <= nx < width:
                if not visited[ny][nx] and maze[ny][nx] != "#":
                    if dfs(ny, nx, d + 1):
                        return True
        return False
    
    dfs(start[0], start[1], 0)
    return found_distance[0]
