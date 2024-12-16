"""
--- Day 16: Reindeer Maze ---

Link:
    https://adventofcode.com/2024/day/16

"""
import math
from collections import defaultdict
from enum import Enum, auto
from pathlib import Path
from sys import argv

from aoc_2024.maze import Maze
from aoc_2024.utils import Grid, Point


DEMO_INPUT = """
###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############
"""


def remap(_map: str) -> Maze:
    """
    Remap example list input provided in "Advent of Code"
    format.
    """
    return Maze(_map)


def part_1(maze: Maze):
    maze.visualize()


def part_2(maze: Maze):
    ...


def solve(input_file=None):
    if input_file:
        demo = False
        default = ' '
        print(f"Solving with input file {input_file}")
        try:
            INPUT = open(input_file).read()
        except FileNotFoundError:
            print('File not found, using default ...')
            INPUT = open(Path(__file__).parent.parent / 'Inputs' / '14').read()
        _width = 101
        _height = 103

    else:
        demo = True
        default = '.'
        INPUT = DEMO_INPUT

    print("Solving Day 16 Problem! 🎄")

    maze = remap(INPUT)

    # Part 1
    _result = part_1(maze)
    print('Part 1:', _result)

    # Part 2
    # _result = part_2(maze)
    # print('Part 2:', _result)


if __name__ == '__main__':
    solve()
