"""
--- Day 6: Chronal Coordinates ---

The device on your wrist beeps several times, and once again you feel like
you're falling.

"Situation critical," the device announces. "Destination indeterminate. Chronal
interference detected. Please specify new target coordinates."

The device then produces a list of coordinates (your puzzle input). Are they
places it thinks are safe or dangerous? It recommends you check manual page
729. The Elves did not give you a manual.

If they're dangerous, maybe you can minimize the danger by finding the
coordinate that gives the largest distance from the other points.

Using only the Manhattan distance, determine the area around each coordinate by
counting the number of integer X,Y locations that are closest to that
coordinate (and aren't tied in distance to any other coordinate).

Your goal is to find the size of the largest area that isn't infinite. For
example, consider the following list of coordinates:

1, 1
1, 6
8, 3
3, 4
5, 5
8, 9

If we name these coordinates A through F, we can draw them on a grid, putting
0,0 at the top left:

..........
.A........
..........
........C.
...D......
.....E....
.B........
..........
..........
........F.

This view is partial - the actual grid extends infinitely in all directions.
Using the Manhattan distance, each location's closest coordinate can be
determined, shown here in lowercase:

aaaaa.cccc
aAaaa.cccc
aaaddecccc
aadddeccCc
..dDdeeccc
bb.deEeecc
bBb.eeee..
bbb.eeefff
bbb.eeffff
bbb.ffffFf

Locations shown as . are equally far from two or more coordinates, and so they
don't count as being closest to any.

In this example, the areas of coordinates A, B, C, and F are infinite - while
not shown here, their areas extend forever outside the visible grid. However,
the areas of coordinates D and E are finite: D is closest to 9 locations, and E
is closest to 17 (both including the coordinate's location itself). Therefore,
in this example, the size of the largest area is 17.

What is the size of the largest area that isn't infinite?
"""
from collections import defaultdict
from typing import List, Tuple, Dict, Set


def read_input(filename: str) -> List[Tuple[int, int]]:

    result = []
    with open(filename) as f:
        for line in f:
            x, y = line.strip().split(',')
            result.append((int(x), int(y)))
    return result


def create_grid(
    coordinates: List[Tuple[int, int]]
    ) -> Tuple[int, int, int, int]:

    top = min(x for x, y in coordinates)
    bottom = max(x for x, y in coordinates)
    left = min(y for x, y in coordinates)
    right = max(y for x, y in coordinates)

    return top, bottom, left, right


def closest_point(
    x: int,
    y: int,
    coordinates: List[Tuple[int, int]]
    ) -> int:

    dist = []
    for i, (a, b) in enumerate(coordinates):
        dist.append((i, abs(x - a) + abs(y - b)))

    dist.sort(key=lambda x: x[1])

    if dist[0][1] != dist[1][1]:
        return dist[0][0]

    return -1


def fill_grid(coordinates: List[Tuple[int, int]]) -> Dict[int, int]:

    top, bottom, left, right = create_grid(coordinates)

    d: Dict[int, int] = defaultdict(int)
    for i in range(top, bottom + 1):
        for j in range(left, right + 1):
            k = closest_point(i, j, coordinates)
            d[k] += 1

    return d


def infinite_points(coordinates: List[Tuple[int, int]]) -> Set[int]:

    top, bottom, left, right = create_grid(coordinates)

    points: Set[int] = set()

    for i in range(top, bottom + 1):
        points.add(closest_point(i, left, coordinates))
        points.add(closest_point(i, right, coordinates))

    for j in range(left, right + 1):
        points.add(closest_point(top, j, coordinates))
        points.add(closest_point(bottom, j, coordinates))

    points.remove(-1)

    return points


def largest_area(coordinates: List[Tuple[int, int]]) -> int:

    grid = fill_grid(coordinates)

    points = set(range(len(coordinates)))
    finite_points = points - infinite_points(coordinates)

    return max(grid[point] for point in finite_points)


def test_create_grid():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    top, bottom, left, right = create_grid(example)

    assert top == 1
    assert bottom == 8
    assert left == 1
    assert right == 9


def test_closest_point():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    grid = """
        aaaaa.cccc
        aAaaa.cccc
        aaaddecccc
        aadddeccCc
        ..dDdeeccc
        bb.deEeecc
        bBb.eeee..
        bbb.eeefff
        bbb.eeffff
        bbb.ffffFf"""

    grid = [list(row) for row in grid.strip().replace(' ', '').split('\n')]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            point = closest_point(i, j, example)
            char = chr(point + ord('a')) if point != -1 else '.'
            assert grid[j][i].lower() == char


def test_infinite_points():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    assert infinite_points(example) == set([0, 1, 2, 5])


def test_largest_area():

    example = [
        (1, 1),
        (1, 6),
        (8, 3),
        (3, 4),
        (5, 5),
        (8, 9)
    ]

    assert largest_area(example) == 17


if __name__ == "__main__":

    test_create_grid()
    test_closest_point()
    test_infinite_points()
    test_largest_area()
    print("all tests passed.")

    answer = largest_area(read_input("input.txt"))
    print("answer:", answer)
