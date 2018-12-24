"""
--- Part Two ---

After a very long time, the water spring will run dry. How much water will be
retained?

In the example above, water that won't eventually drain out is shown as ~, a
total of 29 tiles.

How many water tiles are left after the water spring stops producing water and
all remaining water not at rest has drained?
"""
from part1 import create_grid, fill_water
from typing import List


def count_retained_water(grid: List[List[str]]) -> int:

    prev_count = 0
    while True:
        fill_water(grid)

        retained_water_count = spring_water_count = 0
        for row in grid:
            for char in row:
                if char == '~':
                    retained_water_count += 1
                if char == '|':
                    spring_water_count += 1

        if prev_count == retained_water_count + spring_water_count:
            break

        prev_count = retained_water_count + spring_water_count

    return retained_water_count


def test_fill_water():

    grid = [
        "......+.......",
        "............#.",
        ".#..#.......#.",
        ".#..#..#......",
        ".#..#..#......",
        ".#.....#......",
        ".#.....#......",
        ".#######......",
        "..............",
        "..............",
        "....#.....#...",
        "....#.....#...",
        "....#.....#...",
        "....#######..."
    ]
    grid = [list(row) for row in grid]

    assert count_retained_water(grid) == 29


if __name__ == "__main__":

    test_fill_water()
    print("all tests passed.")

    grid = create_grid([line.strip() for line in open("input.txt")])
    answer = count_retained_water(grid)
    print("answer:", answer)
