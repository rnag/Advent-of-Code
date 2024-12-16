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
        start = end = Point(0, 0)

        for y, row in enumerate(self.rows):
            for x, value in enumerate(row):
                p = Point(x, y)
                if value == '#':
                    point_to_state[p] = State.WALL
                elif value == '.':
                    point_to_state[p] = State.PATH
                elif value == 'S':
                    start = p
                    point_to_state[p] = State.START
                elif value == 'E':
                    end = p
                    point_to_state[p] = State.END

        self.point_to_state = point_to_state
        self.current_loc = self.start_loc = start
        self.end_loc = end

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
        plt.imshow(colored_maze, interpolation="nearest", cmap="viridis")
        plt.axis("off")  # Turn off the axes

        # Annotate the current location
        plt.text(
            self.current_loc.x,  # X coordinate
            self.current_loc.y,  # Y coordinate
            "X",  # Label
            color="blue",  # Text color
            fontsize=16,  # Font size
            fontweight="bold",  # Font weight
            ha="center",  # Horizontal alignment
            va="center",  # Vertical alignment
            alpha=0.8,
            bbox=dict(facecolor="black", edgecolor="none", boxstyle="round,pad=0.4", alpha=0.6)
        )

        # Annotate the start location
        plt.text(
            self.start_loc.x,
            self.start_loc.y,
            "S",  # Label for Start
            color="white",
            fontsize=16,
            fontweight="bold",
            ha="center",
            va="center",
            alpha=0.9,
            # bbox=dict(facecolor="blue", edgecolor="none", boxstyle="round,pad=0.4",
            #           alpha=0.6)  # Transparent background for S
        )

        # Annotate the end location
        plt.text(
            self.end_loc.x,
            self.end_loc.y,
            "E",  # Label for End
            color="white",
            fontsize=16,
            fontweight="bold",
            ha="center",
            va="center",
        )

        plt.show()
