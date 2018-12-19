"""
--- Day 3: No Matter How You Slice It ---

The Elves managed to locate the chimney-squeeze prototype fabric for Santa's
suit (thanks to someone who helpfully wrote its box IDs on the wall of the
warehouse in the middle of the night). Unfortunately, anomalies are still
affecting them - nobody can even agree on how to cut the fabric.

The whole piece of fabric they're working on is a very large square - at least
1000 inches on each side.

Each Elf has made a claim about which area of fabric would be ideal for Santa's
suit. All claims have an ID and consist of a single rectangle with edges
parallel to the edges of the fabric. Each claim's rectangle is defined as
follows:

  - The number of inches between the left edge of the fabric and the left edge
    of the rectangle.
  - The number of inches between the top edge of the fabric and the top edge of
    the rectangle.
  - The width of the rectangle in inches.
  - The height of the rectangle in inches.

A claim like #123 @ 3,2: 5x4 means that claim ID 123 specifies a rectangle 3
inches from the left edge, 2 inches from the top edge, 5 inches wide, and 4
inches tall. Visually, it claims the square inches of fabric represented by #
(and ignores the square inches of fabric represented by .) in the diagram
below:

...........
...........
...#####...
...#####...
...#####...
...#####...
...........
...........
...........

The problem is that many of the claims overlap, causing two or more claims to
cover part of the same areas. For example, consider the following claims:

#1 @ 1,3: 4x4
#2 @ 3,1: 4x4
#3 @ 5,5: 2x2

Visually, these claim the following areas:

........
...2222.
...2222.
.11XX22.
.11XX22.
.111133.
.111133.
........

The four square inches marked with X are claimed by both 1 and 2. (Claim 3,
while adjacent to the others, does not overlap either of them.)

If the Elves all proceed with their own plans, none of them will have enough
fabric. How many square inches of fabric are within two or more claims?
"""
from typing import List, Tuple


def max_width_height(
    claims: List[Tuple[int, int, int, int]]
    ) -> Tuple[int, int]:

    max_width = max(left + width for left, _, width, _ in claims)
    max_height = max(top + height for _, top, _, height in claims)

    return max_width, max_height


def create_fabric(
    claims: List[Tuple[int, int, int, int]]
    ) -> List[List[int]]:

    width, height = max_width_height(claims)

    return [[0] * width for _ in range(height)]


def cover_fabric_with_claims(
    claims: List[Tuple[int, int, int, int]]
    ) -> List[List[int]]:

    fabric = create_fabric(claims)

    for claim in claims:
        left, top, width, height = claim
        for i in range(top, top + height):
            for j in range(left, left + width):
                fabric[i][j] += 1

    return fabric


def count_squares_with_two_or_more_claims(
    claims: List[Tuple[int, int, int, int]]
    ) -> int:

    fabric = cover_fabric_with_claims(claims)

    return sum(x >= 2 for row in fabric for x in row)


def test_max_width_height():

    claims = [
        (1, 3, 4, 4),
        (3, 1, 4, 4),
        (5, 5, 2, 2)
    ]

    assert max_width_height(claims) == (7, 7)


def test_create_fabric():

    claims = [
        (1, 3, 4, 4),
        (3, 1, 4, 4),
        (5, 5, 2, 2)
    ]

    fabric = create_fabric(claims)
    assert len(fabric) == 7
    assert all(len(row) == 7 for row in fabric)
    assert all(all(col == 0 for col in row) for row in fabric)


def test_cover_fabric_with_claims():

    claims = [
        (1, 3, 4, 4),
        (3, 1, 4, 4),
        (5, 5, 2, 2)
    ]

    example = """
        .......
        ...2222
        ...2222
        .11XX22
        .11XX22
        .111133
        .111133
    """

    fabric = cover_fabric_with_claims(claims)
    assert sum(x == 0 for row in fabric for x in row) == example.count('.')
    assert sum(x == 2 for row in fabric for x in row) == example.count('X')


def test_count_squares_with_two_or_more_claims():

    claims = [
        (1, 3, 4, 4),
        (3, 1, 4, 4),
        (5, 5, 2, 2)
    ]

    example = """
        .......
        ...2222
        ...2222
        .11XX22
        .11XX22
        .111133
        .111133
    """

    assert count_squares_with_two_or_more_claims(claims) == 4


def read_input(filename: str) -> List[Tuple[int, int, int, int]]:

    result = []
    with open(filename) as f:
        for line in f:
            idx, value = line.strip().split('@')
            offset, area = value.split(':')
            left, top = offset.split(',')
            width, height = area.split('x')
            result.append((int(left), int(top), int(width), int(height)))
    return result


if __name__ == "__main__":

    test_max_width_height()
    test_create_fabric()
    test_cover_fabric_with_claims()
    test_count_squares_with_two_or_more_claims()
    print("all tests passed.")

    answer = count_squares_with_two_or_more_claims(read_input("input.txt"))
    print("answer:", answer)
