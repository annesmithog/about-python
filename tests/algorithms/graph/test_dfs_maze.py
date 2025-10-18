from src.algorithms.graph.dfs_maze import dfs_maze
import unittest

class TestDfsMaze(unittest.TestCase):
    def test_no_path(self):
        maze = [
            list("S#G"),
            list("###")
        ]
        result = dfs_maze(maze, 2, 3)
        self.assertEqual(-1, result)

    def test_start_not_exists(self):
        maze = [
            list("G..."),
            list("...."),
            list("...#")
        ]
        with self.assertRaises(ValueError):
            dfs_maze(maze, 3, 4)

    def test_goal_not_exists(self):
        maze = [
            list("S.....")
        ]
        with self.assertRaises(ValueError):
            dfs_maze(maze, 1, 6)

    def test_empty_maze(self):
        maze = [list("")]
        with self.assertRaises(ValueError):
            dfs_maze(maze, 0, 0)

    def test_simple_maze(self):
        maze = [
            list("S..#."),
            list(".#..."),
            list(".#G#."),
            list(".###."),
            list(".....")
        ]
        result = dfs_maze(maze, 5, 5)
        self.assertLessEqual(4, result)

    def test_normal_maze(self):
        maze = [
            list("S#.#."),
            list(".#..."),
            list(".#G#."),
            list(".###."),
            list(".....")
        ]
        result = dfs_maze(maze, 5, 5)
        self.assertLessEqual(14, result)

    def test_complicated_maze(self):
        maze = [
            list(".......#............"),
            list("....#######.....#.#."),
            list("....#.....#.#####..#"),
            list("....#G###.#.#......."),
            list("...######...#......."),
            list(".........##.#....##."),
            list(".....#......#......."),
            list(".#..#########......."),
            list("##................S."),
            list(".#..................")
        ]
        result = dfs_maze(maze, 10, 20)
        self.assertLessEqual(30, result)
