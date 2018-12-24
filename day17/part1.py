"""
--- Day 17: Reservoir Research ---

You arrive in the year 18. If it weren't for the coat you got in 1018, you 
would be very cold: the North Pole base hasn't even been constructed.

Rather, it hasn't been constructed yet. The Elves are making a little progress, 
but there's not a lot of liquid water in this climate, so they're getting very 
dehydrated. Maybe there's more underground?

You scan a two-dimensional vertical slice of the ground nearby and discover 
that it is mostly sand with veins of clay. The scan only provides data with a 
granularity of square meters, but it should be good enough to determine how 
much water is trapped there. In the scan, x represents the distance to the 
right, and y represents the distance down. There is also a spring of water near 
the surface at x=500, y=0. The scan identifies which square meters are clay 
(your puzzle input).

For example, suppose your scan shows the following veins of clay:

x=495, y=2..7
y=7, x=495..501
x=501, y=3..7
x=498, y=2..4
x=506, y=1..2
x=498, y=10..13
x=504, y=10..13
y=13, x=498..504

Rendering clay as #, sand as ., and the water spring as +, and with x 
increasing to the right and y increasing downward, this becomes:

   44444455555555
   99999900000000
   45678901234567
 0 ......+.......
 1 ............#.
 2 .#..#.......#.
 3 .#..#..#......
 4 .#..#..#......
 5 .#.....#......
 6 .#.....#......
 7 .#######......
 8 ..............
 9 ..............
10 ....#.....#...
11 ....#.....#...
12 ....#.....#...
13 ....#######...

The spring of water will produce water forever. Water can move through sand, 
but is blocked by clay. Water always moves down when possible, and spreads to 
the left and right otherwise, filling space that has clay on both sides and 
falling out otherwise.

For example, if five squares of water are created, they will flow downward 
until they reach the clay and settle there. Water that has come to rest is 
shown here as ~, while sand through which water has passed (but which is now 
dry again) is shown as |:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#....|#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

Two squares of water can't occupy the same location. If another five squares of 
water are created, they will settle on the first five, filling the clay 
reservoir a little more:

......+.......
......|.....#.
.#..#.|.....#.
.#..#.|#......
.#..#.|#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

Water pressure does not apply in this scenario. If another four squares of 
water are created, they will stay on the right side of the barrier, and no 
water will reach the left side:

......+.......
......|.....#.
.#..#.|.....#.
.#..#~~#......
.#..#~~#......
.#~~~~~#......
.#~~~~~#......
.#######......
..............
..............
....#.....#...
....#.....#...
....#.....#...
....#######...

At this point, the top reservoir overflows. While water can reach the tiles 
above the surface of the water, it cannot settle there, and so the next five 
squares of water settle like this:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#...|.#...
....#...|.#...
....#~~~~~#...
....#######...

Note especially the leftmost |: the new squares of water can reach this tile, 
but cannot stop there. Instead, eventually, they all fall to the right and 
settle in the reservoir below.

After 10 more squares of water, the bottom reservoir is also full:

......+.......
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
........|.....
....#~~~~~#...
....#~~~~~#...
....#~~~~~#...
....#######...

Finally, while there is nowhere left for the water to settle, it can reach a 
few more tiles before overflowing beyond the bottom of the scanned data:

......+.......    (line not counted: above minimum y value)
......|.....#.
.#..#||||...#.
.#..#~~#|.....
.#..#~~#|.....
.#~~~~~#|.....
.#~~~~~#|.....
.#######|.....
........|.....
...|||||||||..
...|#~~~~~#|..
...|#~~~~~#|..
...|#~~~~~#|..
...|#######|..
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)
...|.......|..    (line not counted: below maximum y value)

How many tiles can be reached by the water? To prevent counting forever, ignore 
tiles with a y coordinate smaller than the smallest y coordinate in your scan 
data or larger than the largest one. Any x coordinate is valid. In this 
example, the lowest y coordinate given is 1, and the highest is 13, causing the 
water spring (in row 0) and the water falling off the bottom of the render (in 
rows 14 through infinity) to be ignored.

So, in the example above, counting both water at rest (~) and other sand tiles 
the water can hypothetically reach (|), the total number of tiles the water can 
reach is 57.

How many tiles can the water reach within the range of y values in your scan?
"""
from typing import List, Tuple


def create_grid(scan: List[str]) -> List[List[str]]:

    coord = []
    for line in scan:
        first, second = line.split(',')
        first_axis, first_coord = first.split('=')
        second_axis, second_range = second.split('=')
        start, end = map(int, second_range.split('..'))
        if first_axis == 'y':
            y = int(first_coord)
            for x in range(start, end + 1):
                coord.append((x, y))
        elif first_axis == 'x':
            x = int(first_coord)
            for y in range(start, end + 1):
                 coord.append((x, y))

    min_y = 0
    max_y = max(y for x, y in coord)
    min_x = min(x for x, y in coord)
    max_x = max(x for x, y in coord)

    grid = [['.'] * (max_x - min_x + 3) for _ in range(max_y - min_y + 1)]

    grid[0][500 - min_x + 1] = '+'

    for x, y in coord:
        grid[y][x - min_x + 1] = '#'

    return grid


def fill_water(grid: List[List[str]]) -> None:

    x, y = 0, 0

    for i in range(len(grid) - 1):
        for j in range(len(grid[i])):
            if ((grid[i][j] == '+' and grid[i + 1][j] == '.') or
                (grid[i][j] == '|' and grid[i + 1][j] == '.')):
                x, y = j, i + 1
                break

    if x == y == 0:
        return

    while 0 < y < len(grid):

        while y < len(grid) and grid[y][x] == '.':
            grid[y][x] = '|'
            y += 1

        left = right = x
        while (0 <= y < len(grid) and left >= 0
            and grid[y][left] in '#~' and grid[y - 1][left] in '.|'):
            left -= 1

        while (0 <= y < len(grid) and right < len(grid[y])
            and grid[y][right] in '#~' and grid[y - 1][right] in '.|'):
            right += 1

        if grid[y - 1][left] == '#' and grid[y - 1][right] == '#':
            for i in range(left + 1, right):
                grid[y - 1][i] = '~'
            y -= 1
        elif grid[y - 1][left] == '#':
            for i in range(left + 1, right + 1):
                grid[y - 1][i] = '|'
            return
        elif grid[y - 1][right] == '#':
            for i in range(left, right):
                grid[y - 1][i] = '|'
            return
        else:
            for i in range(left, right + 1):
                grid[y - 1][i] = '|'
            return


def count_tiles(grid: List[List[str]]) -> int:

    prev_count = 0
    while True:
        fill_water(grid)
        curr_count = sum(sum(x.count(c) for x in grid) for c in '~|')
        if curr_count == prev_count:
            break
        prev_count = curr_count

    first_clay_line = next(i for i, x in enumerate(grid) if '#' in x)
    ignore_tiles = sum(x.count('|') for x in grid[:first_clay_line])

    return curr_count - ignore_tiles


def test_create_grid():

    example = [
        "x=495, y=2..7",
        "y=7, x=495..501",
        "x=501, y=3..7",
        "x=498, y=2..4",
        "x=506, y=1..2",
        "x=498, y=10..13",
        "x=504, y=10..13",
        "y=13, x=498..504"
    ]

    initial_grid = [
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

    grid = create_grid(example)

    assert initial_grid == [''.join(row) for row in grid]


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

    assert count_tiles(grid) == 57


if __name__ == "__main__":

    test_create_grid()
    test_fill_water()
    print("all tests passed.")

    grid = create_grid([line.strip() for line in open("input.txt")])
    answer = count_tiles(grid)
    print("answer:", answer)
