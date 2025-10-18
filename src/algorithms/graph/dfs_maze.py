Maze = list[list[str]]
Visited = list[list[bool]]
Direction = list[tuple[int, int]]

class MissingStartOrGoalError(ValueError):
    """スタートまたはゴールが存在しない場合にスローされる"""
    pass

def dfs_maze(maze: Maze, height: int, width: int) -> int:
    """DFSを使用して到達可能な経路を見つけ、その距離を返します。
    Args:
        maze (list[list[str]]): 迷路
        height (int): 高さ
        width (int): 幅
    Raises:
        MissingStartOrGoalError: スタートまたはゴールが存在しない場合にスローされる
    Returns:
        int: 到達可能な距離
    """
    start: tuple[int, int] | None = None
    goal: tuple[int, int] | None = None

    for i in range(height):
        for j in range(width):
            if maze[i][j] == "S":
                start = (i, j)
            if maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        raise MissingStartOrGoalError("スタート(S)またはゴール(G)が存在しません。")

    visited: Visited = [[False] * width for _ in range(height)]
    visited[start[0]][start[1]] = True
    directions: Direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]
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
