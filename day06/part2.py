"""
--- Part Two ---

On the other hand, if the coordinates are safe, maybe the best you can do is
try to find a region near as many coordinates as possible.

For example, suppose you want the sum of the Manhattan distance to all of the
coordinates to be less than 32. For each location, add up the distances to all
of the given coordinates; if the total of those distances is less than 32, that
location is within the desired region. Using the same coordinates as above, the
resulting region looks like this:

..........
.A........
..........
...###..C.
..#D###...
..###E#...
.B.###....
..........
..........
........F.

In particular, consider the highlighted location 4,3 located at the top middle
of the region. Its calculation is as follows, where abs() is the absolute value
function:

  - Distance to coordinate A: abs(4-1) + abs(3-1) =  5
  - Distance to coordinate B: abs(4-1) + abs(3-6) =  6
  - Distance to coordinate C: abs(4-8) + abs(3-3) =  4
  - Distance to coordinate D: abs(4-3) + abs(3-4) =  2
  - Distance to coordinate E: abs(4-5) + abs(3-5) =  3
  - Distance to coordinate F: abs(4-8) + abs(3-9) = 10
  - Total distance: 5 + 6 + 4 + 2 + 3 + 10 = 30

Because the total distance to all coordinates (30) is less than 32, the
location is within the region.

This region, which also includes coordinates D and E, has a total size of 16.

Your actual region will need to be much larger than this example, though,
instead including all locations with a total distance of less than 10000.

What is the size of the region containing all locations which have a total
distance to all given coordinates of less than 10000?
"""
from part1 import read_input, create_grid
from typing import List, Tuple


def sum_of_distances(
    x: int,
    y: int,
    coordinates: List[Tuple[int, int]]
    ) -> int:

    dist = 0
    for a, b in coordinates:
        dist += abs(x - a) + abs(y - b)

    return dist


def size_of_region(
    coordinates: List[Tuple[int, int]],
    threshold: int = 10000
    ) -> int:

    top, bottom, left, right = create_grid(coordinates)

    count = 0
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            if sum_of_distances(i, j, coordinates) < threshold:
                count += 1

    return count


def test_sum_of_distances():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    assert sum_of_distances(4, 3, example) == 30


def test_size_of_region():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    assert size_of_region(example, 32) == 16


if __name__ == "__main__":

    test_sum_of_distances()
    test_size_of_region()
    print("all tests passed.")

    answer = size_of_region(read_input("input.txt"))
    print("answer:", answer)
