"""
--- Day 23: Experimental Emergency Teleportation ---

Using your torch to search the darkness of the rocky cavern, you finally locate
the man's friend: a small reindeer.

You're not sure how it got so far in this cave. It looks sick - too sick to
walk - and too heavy for you to carry all the way back. Sleighs won't be
invented for another 1500 years, of course.

The only option is experimental emergency teleportation.

You hit the "experimental emergency teleportation" button on the device and
push I accept the risk on no fewer than 18 different warning messages.
Immediately, the device deploys hundreds of tiny nanobots which fly around the
cavern, apparently assembling themselves into a very specific formation. The
device lists the X,Y,Z position (pos) for each nanobot as well as its signal
radius (r) on its tiny screen (your puzzle input).

Each nanobot can transmit signals to any integer coordinate which is a distance
away from it less than or equal to its signal radius (as measured by Manhattan
distance). Coordinates a distance away of less than or equal to a nanobot's
signal radius are said to be in range of that nanobot.

Before you start the teleportation process, you should determine which nanobot
is the strongest (that is, which has the largest signal radius) and then, for
that nanobot, the total number of nanobots that are in range of it, including
itself.

For example, given the following nanobots:

pos=<0,0,0>, r=4
pos=<1,0,0>, r=1
pos=<4,0,0>, r=3
pos=<0,2,0>, r=1
pos=<0,5,0>, r=3
pos=<0,0,3>, r=1
pos=<1,1,1>, r=1
pos=<1,1,2>, r=1
pos=<1,3,1>, r=1

The strongest nanobot is the first one (position 0,0,0) because its signal
radius, 4 is the largest. Using that nanobot's location and signal radius, the
following nanobots are in or out of range:

The nanobot at 0,0,0 is distance 0 away, and so it is in range.
The nanobot at 1,0,0 is distance 1 away, and so it is in range.
The nanobot at 4,0,0 is distance 4 away, and so it is in range.
The nanobot at 0,2,0 is distance 2 away, and so it is in range.
The nanobot at 0,5,0 is distance 5 away, and so it is not in range.
The nanobot at 0,0,3 is distance 3 away, and so it is in range.
The nanobot at 1,1,1 is distance 3 away, and so it is in range.
The nanobot at 1,1,2 is distance 4 away, and so it is in range.
The nanobot at 1,3,1 is distance 5 away, and so it is not in range.

In this example, in total, 7 nanobots are in range of the nanobot with the
largest signal radius.

Find the nanobot with the largest signal radius. How many nanobots are in range
of its signals?
"""
from typing import List, Tuple


def read_input(filename: str) -> List[Tuple[int, int, int, int]]:

    result = []
    with open(filename) as f:
        for line in f:
            splitted = line.split(',')
            pos0 = splitted[0].lstrip('pos=<')
            pos1 = splitted[1]
            pos2 = splitted[2].rstrip('>')
            r = splitted[3].strip().split('=')[1]
            result.append((int(pos0), int(pos1), int(pos2), int(r)))

    return result


def strongest(
    data: List[Tuple[int, int, int, int]]
    ) -> Tuple[int, int, int, int]:

    return max(data, key=lambda x: x[3])


def distance(
    x: int, y: int, z: int,
    a: int = 0, b: int = 0, c: int = 0
    ) -> int:

    return abs(x - a) + abs(y - b) + abs(z - c)


def how_many_in_range(
    data: List[Tuple[int, int, int, int]],
    target: Tuple[int, int, int, int]) -> int:

    x0, y0, z0, r0 = target

    return sum(
        1
        if distance(x, y, z, x0, y0, z0) <= r0
        else 0
        for x, y, z, r in data
    )


def test_strongest():

    data = read_input("test1.txt")
    assert strongest(data) == (0, 0, 0, 4)


def test_distance():

    assert distance(0, 0, 0) == 0
    assert distance(1, 0, 0) == 1
    assert distance(4, 0, 0) == 4
    assert distance(0, 2, 0) == 2
    assert distance(0, 5, 0) == 5
    assert distance(0, 0, 3) == 3
    assert distance(1, 1, 1) == 3
    assert distance(1, 1, 2) == 4
    assert distance(1, 3, 1) == 5


def test_how_many_in_range():

    data = read_input("test1.txt")
    assert how_many_in_range(data, strongest(data)) == 7


if __name__ == "__main__":

    test_strongest()
    test_distance()
    test_how_many_in_range()
    print("all tests passed.")

    data = read_input("input.txt")
    answer = how_many_in_range(data, strongest(data))
    print("answer:", answer)
