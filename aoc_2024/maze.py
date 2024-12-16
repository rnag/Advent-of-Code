from enum import Enum, auto

import numpy as np
import matplotlib.pyplot as plt

from .utils import Grid, Point


class State(Enum):
    WALL = auto()
    PATH = auto()
    DEAD_END = auto()
    START = auto()
    END = auto()


class Maze(Grid):

    def __init__(self, _map: str):
        grid_array: list = _map.strip().split('\n')
        super().__init__(grid_array)

        point_to_state = {}
        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                p = Point(x, y)
                if value == '#':
                    point_to_state[p] = State.WALL
                elif value == '.':
                    point_to_state[p] = State.PATH
                elif value == 'S':
                    point_to_state[p] = State.START
                elif value == 'E':
                    point_to_state[p] = State.END
        self.point_to_state = point_to_state

    def visualize(self):
        """Visualizes the maze using Matplotlib."""
        # Create a color mapping
        color_map = {
            State.WALL: (0, 0, 0),  # Wall - black
            State.PATH: (1, 1, 1),  # Path - white
            State.START: (0, 1, 0),  # Start - green
            State.END: (1, 0, 0),  # End - red
        }

        # Convert the maze into a NumPy array of colors
        height, width, pt_to_state = self.height, self.width, self.point_to_state
        colored_maze = np.zeros((height, width, 3))  # 3 channels for RGB

        for y, row in enumerate(self._array):
            for x, cell in enumerate(row):
                state = pt_to_state[Point(x, y)]
                colored_maze[y, x] = color_map[state]

        # Plot the maze
        plt.figure(figsize=(8, 8))
        plt.imshow(colored_maze, interpolation="nearest")
        plt.axis("off")  # Turn off the axes
        plt.show()
