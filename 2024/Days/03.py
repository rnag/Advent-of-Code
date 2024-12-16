"""
--- Day 3: Mull It Over ---

Link:
    https://adventofcode.com/2024/day/3

"""
import re
from pathlib import Path


_MUL_RE = re.compile(r'mul\(([-+]?\d{1,3}),([-+]?\d{1,3})\)')

# Input: `mul` instructions
INPUT = """
xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))
"""

# TODO: Update filename `input` and uncomment once ready!
# INPUT = open(Path(__file__).parent / "input").read()


def sum_of_mul_instructions(mul_instructions: str) -> int:
    """
    Solution to Day 3 [Part 1]

    *What do you get if you add up all the results of the multiplications?*
    """
    return sum([int(n1) * int(n2) for (n1, n2) in _MUL_RE.findall(mul_instructions)])



def sum_of_mul_instructions_with_do_and_dont(mul_instructions: str) -> int:
    """
    Solution to Day 3 [Part 2]

    *what do you get if you add up all the results of just the enabled multiplications?*
    """
    total = 0
    first_instruction, *instructions = mul_instructions.split('don\'t()')

    for n1, n2 in _MUL_RE.findall(first_instruction):
        total += int(n1) * int(n2)

    for instruction in instructions:
        try:
            do = instruction.split('do()', 1)[1]
        except IndexError:
            continue
        else:
            for n1, n2 in _MUL_RE.findall(do):
                total += int(n1) * int(n2)

    return total


if __name__ == '__main__':
    # Part 1
    print('Part 1:  ', sum_of_mul_instructions(INPUT))
    # Part 2
    print('Part 2:  ', sum_of_mul_instructions_with_do_and_dont(INPUT))
