from dataclasses import dataclass

from maze.maze import Direction, Maze, Position


@dataclass
class MazeEnvState:
    maze: Maze
    position: Position
    direction: Direction
