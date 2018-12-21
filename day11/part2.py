"""
--- Part Two ---

You discover a dial on the side of the device; it seems to let you select a
square of any size, not just 3x3. Sizes from 1x1 to 300x300 are supported.

Realizing this, you now must find the square of any size with the largest total
power. Identify this square by including its size as a third parameter after
the top-left coordinate: a 9x9 square with a top-left corner of 3,5 is
identified as 3,5,9.

For example:

  - For grid serial number 18, the largest total square (with a total power of
    113) is 16x16 and has a top-left corner of 90,269, so its identifier is
    90,269,16.
  - For grid serial number 42, the largest total square (with a total power of
    119) is 12x12 and has a top-left corner of 232,251, so its identifier is
    232,251,12.

What is the X,Y,size identifier of the square with the largest total power?
"""
from typing import List, Tuple
from part1 import create_grid, fill_grid


def get_prefix_sum(grid: List[List[int]]) -> List[List[int]]:

    table = [[0] * len(grid[0]) for _ in range(len(grid))]

    for y in range(1, len(grid)):
        for x in range(1, len(grid[0])):
            table[y][x] = (
                grid[y][x]
                + table[y - 1][x]
                + table[y][x - 1]
                - table[y - 1][x - 1]
            )

    return table


def get_sum(table: List[List[int]], x: int, y: int, size: int) -> int:

    return (
        table[y + size - 1][x + size - 1]
        - table[y + size - 1][x - 1]
        - table[y - 1][x + size - 1]
        + table[y - 1][x - 1]
    )


def process(n: int) -> Tuple[int, int, int]:

    grid = create_grid()
    grid = fill_grid(grid, n)
    table = get_prefix_sum(grid)

    max_power = 0
    result = (0, 0, 0)
    for size in range(1, 301):
        for y in range(1, 301 - size):
            for x in range(1, 301 - size):
                power = get_sum(table, x, y, size)
                if power > max_power:
                    max_power = power
                    result = (x, y, size)

    return result


def test_prefix_sum():

    grid = [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 4, 5, 6],
        [0, 7, 8, 9]
    ]

    prefix_sum = [
        [0, 0, 0, 0],
        [0, 1, 3, 6],
        [0, 5, 12, 21],
        [0, 12, 27, 45]
    ]

    assert get_prefix_sum(grid) == prefix_sum


def test_get_sum():

    grid = [
        [0, 0, 0, 0],
        [0, 1, 2, 3],
        [0, 4, 5, 6],
        [0, 7, 8, 9]
    ]

    prefix_sum = get_prefix_sum(grid)
    assert get_sum(prefix_sum, 1, 1, 1) == 1
    assert get_sum(prefix_sum, 1, 1, 2) == 1 + 2 + 4 + 5
    assert get_sum(prefix_sum, 2, 2, 2) == 5 + 6 + 8 + 9
    assert get_sum(prefix_sum, 1, 2, 2) == 4 + 5 + 7 + 8
    assert get_sum(prefix_sum, 1, 1, 3) == sum(range(1, 10))

    grid = create_grid()
    grid = fill_grid(grid, 18)
    table = get_prefix_sum(grid)

    assert get_sum(table, 90, 269, 16) == 113

    grid = create_grid()
    grid = fill_grid(grid, 42)
    table = get_prefix_sum(grid)

    assert get_sum(table, 232, 251, 12) == 119


def test_process():

    assert process(18) == (90, 269, 16)
    assert process(42) == (232, 251, 12)


if __name__ == "__main__":

    test_prefix_sum()
    test_get_sum()
    test_process()
    print("all tests passed.")

    serial_number = input("Enter your puzzle input: ")
    answer = process(int(serial_number))
    print("answer:", ','.join(str(x) for x in answer))
