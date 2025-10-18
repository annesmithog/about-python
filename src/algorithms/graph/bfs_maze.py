from collections import deque

Maze = list[list[str]]
Queue = deque[tuple[int, int, int]] # y, x, distance
Visited = list[list[bool]]
Direction = list[tuple[int, int]]

class MissingStartOrGoalError(ValueError):
    """スタートまたはゴールが存在しない場合にスローされる"""
    pass

def bfs_maze(maze: Maze, height: int, width: int) -> int:
    """BFSを使用して最短経路を見つけ、最短距離を返します。
    Args:
        maze (list[list[str]]): 迷路
        height (int): 高さ
        width (int): 幅
    Raises:
        MissingStartOrGoalError: スタートまたはゴールが存在しない場合にスローされる
    Returns:
        int: 最短距離
    """
    start: tuple[int, int] | None = None
    goal: tuple[int, int] | None = None

    for i in range(height):
        for j in range(width):
            if maze[i][j] == "S":
                start = (i, j)
            elif maze[i][j] == "G":
                goal = (i, j)

    if start is None or goal is None:
        raise MissingStartOrGoalError("スタート(S)またはゴール(G)が存在しません。")

    queue: Queue = deque([(start[0], start[1], 0)])
    visited: Visited = [[False] * width for _ in range(height)]
    visited[start[0]][start[1]] = True
    directions: Direction = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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
