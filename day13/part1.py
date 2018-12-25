"""
--- Day 13: Mine Cart Madness ---

A crop of this size requires significant logistics to transport produce, soil,
fertilizer, and so on. The Elves are very busy pushing things around in carts
on some kind of rudimentary system of tracks they've come up with.

Seeing as how cart-and-track systems don't appear in recorded history for
another 1000 years, the Elves seem to be making this up as they go along. They
haven't even figured out how to avoid collisions yet.

You map out the tracks (your puzzle input) and see where you can help.

Tracks consist of straight paths (| and -), curves (/ and \), and intersections
(+). Curves connect exactly two perpendicular pieces of track; for example,
this is a closed loop:

/----\
|    |
|    |
\----/

Intersections occur when two perpendicular paths cross. At an intersection, a
cart is capable of turning left, turning right, or continuing straight. Here
are two loops connected by two intersections:

/-----\
|     |
|  /--+--\
|  |  |  |
\--+--/  |
   |     |
   \-----/

Several carts are also on the tracks. Carts always face either up (^), down
(v), left (<), or right (>). (On your initial map, the track under each cart is
a straight path matching the direction the cart is facing.)

Each time a cart has the option to turn (by arriving at any intersection), it
turns left the first time, goes straight the second time, turns right the third
time, and then repeats those directions starting again with left the fourth
time, straight the fifth time, and so on. This process is independent of the
particular intersection at which the cart has arrived - that is, the cart has
no per-intersection memory.

Carts all move at the same speed; they take turns moving a single step at a
time. They do this based on their current location: carts on the top row move
first (acting from left to right), then carts on the second row move (again
from left to right), then carts on the third row, and so on. Once each cart has
moved one step, the process repeats; each of these loops is called a tick.

For example, suppose there are two carts on a straight track:

|  |  |  |  |
v  |  |  |  |
|  v  v  |  |
|  |  |  v  X
|  |  ^  ^  |
^  ^  |  |  |
|  |  |  |  |

First, the top cart moves. It is facing down (v), so it moves down one square.
Second, the bottom cart moves. It is facing up (^), so it moves up one square.
Because all carts have moved, the first tick ends. Then, the process repeats,
starting with the first cart. The first cart moves down, then the second cart
moves up - right into the first cart, colliding with it! (The location of the
crash is marked with an X.) This ends the second and last tick.

Here is a longer example:

/->-\        
|   |  /----\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   

/-->\        
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \->--/
  \------/   

/---v        
|   |  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+>-/
  \------/   

/---\        
|   v  /----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-+->/
  \------/   

/---\        
|   |  /----\
| /->--+-\  |
| | |  | |  |
\-+-/  \-+--^
  \------/   

/---\        
|   |  /----\
| /-+>-+-\  |
| | |  | |  ^
\-+-/  \-+--/
  \------/   

/---\        
|   |  /----\
| /-+->+-\  ^
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /----<
| /-+-->-\  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /---<\
| /-+--+>\  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /--<-\
| /-+--+-v  |
| | |  | |  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /-<--\
| /-+--+-\  |
| | |  | v  |
\-+-/  \-+--/
  \------/   

/---\        
|   |  /<---\
| /-+--+-\  |
| | |  | |  |
\-+-/  \-<--/
  \------/   

/---\        
|   |  v----\
| /-+--+-\  |
| | |  | |  |
\-+-/  \<+--/
  \------/   

/---\        
|   |  /----\
| /-+--v-\  |
| | |  | |  |
\-+-/  ^-+--/
  \------/   

/---\        
|   |  /----\
| /-+--+-\  |
| | |  X |  |
\-+-/  \-+--/
  \------/   

After following their respective paths for a while, the carts eventually crash.
To help prevent crashes, you'd like to know the location of the first crash.
Locations are given in X,Y coordinates, where the furthest left column is X=0
and the furthest top row is Y=0:

           111
 0123456789012
0/---\        
1|   |  /----\
2| /-+--+-\  |
3| | |  X |  |
4\-+-/  \-+--/
5  \------/   

In this example, the location of the first crash is 7,3.
"""
import itertools
from typing import List, Dict, Tuple, Set


STATUS = {
    '>': (0, 1),
    '<': (0, -1),
    '^': (-1, 0),
    'v': (1, 0)
}


def cars(m: List[List[str]]) -> Dict[Tuple[int, int], Tuple[str, int]]:

    result = dict()
    for i, row in enumerate(m):
        for j, x in enumerate(row):
            if x in STATUS:
                result[i, j] = (x, 0)
    return result


def path(m: List[List[str]]) -> List[List[str]]:

    for i, row in enumerate(m):
        for j, x in enumerate(row):
            if m[i][j] in "><":
                m[i][j] = '-'
            if m[i][j] in "^v":
                m[i][j] = '|'
    return m


def move(
    cars: Dict[Tuple[int, int], Tuple[str, int]],
    path:List[List[str]]
    ) -> Dict[Tuple[int, int], Tuple[str, int]]:

    result: Dict[Tuple[int, int], Tuple[str, int]] = dict(cars)

    for row, col in sorted(cars):

        symbol, turn = cars[row, col]
        dr, dc = STATUS[symbol]

        if path[row + dr][col + dc] == '\\':
            if symbol == '>':
                next_symbol, next_turn = 'v', turn
            if symbol == 'v':
                next_symbol, next_turn = '>', turn
            if symbol == '<':
                next_symbol, next_turn = '^', turn
            if symbol == '^':
                next_symbol, next_turn = '<', turn

        elif path[row + dr][col + dc] == '/':
            if symbol == '>':
                next_symbol, next_turn = '^', turn
            if symbol == 'v':
                next_symbol, next_turn = '<', turn
            if symbol == '<':
                next_symbol, next_turn = 'v', turn
            if symbol == '^':
                next_symbol, next_turn = '>', turn

        elif path[row + dr][col + dc] == '+':

            if turn % 3 == 0:
                if symbol == '>':
                    next_symbol, next_turn = '^', turn + 1
                if symbol == 'v':
                    next_symbol, next_turn = '>', turn + 1
                if symbol == '<':
                    next_symbol, next_turn = 'v', turn + 1
                if symbol == '^':
                    next_symbol, next_turn = '<', turn + 1

            elif turn % 3 == 1:
                next_symbol, next_turn = symbol, turn + 1

            elif turn % 3 == 2:
                if symbol == '>':
                    next_symbol, next_turn = 'v', turn + 1
                if symbol == 'v':
                    next_symbol, next_turn = '<', turn + 1
                if symbol == '<':
                    next_symbol, next_turn = '^', turn + 1
                if symbol == '^':
                    next_symbol, next_turn = '>', turn + 1

        elif path[row + dr][col + dc] in ['|', '-']:
            next_symbol, next_turn = symbol, turn

        else:
            raise ValueError("path invalid")

        del result[row, col]

        if (row + dr, col + dc) in result:
            result[row + dr, col + dc] = ('X', next_turn)
        else:
            result[row + dr, col + dc] = (next_symbol, next_turn)

    return result


def test_cars():

    example = [
        "/->-\\        ",
        "|   |  /----\\",
        "| /-+--+-\\  |",
        "| | |  | v  |",
        "\\-+-/  \\-+--/",
        "   \\------/  "
    ]
    example = [list(line) for line in example]
    init = cars(example)

    assert len(init) == 2
    assert ('>', 0) in init.values()
    assert ('v', 0) in init.values()


def test_path():

    example = [
        "/->-\\        ",
        "|   |  /----\\",
        "| /-+--+-\\  |",
        "| | |  | v  |",
        "\\-+-/  \\-+--/",
        "   \\------/  "
    ]
    example = [list(line) for line in example]

    assert len(path(example)) > 0
    assert len(cars(path(example))) == 0


def test_move():

    example = [
        "/->-\\        ",
        "|   |  /----\\",
        "| /-+--+-\\  |",
        "| | |  | v  |",
        "\\-+-/  \\-+--/",
        "  \\------/   "
    ]
    example = [list(line) for line in example]

    c = cars(example)
    p = path(example)

    first_crash = (-1, -1)

    for _ in range(20):

        c = move(c, p)
        crashed = any(v.count('X') for v in c.values())
        if crashed:
            first_crash = next(k for k, v in c.items() if v.count('X'))
            break

    assert first_crash == (3, 7)

def read_input(filename: str) -> List[List[str]]:

    result = []
    with open(filename) as f:
        for line in f:
            result.append(list(line))

    return result


if __name__ == "__main__":

    test_cars()
    test_path()
    test_move()
    print("all tests passed.")

    m = read_input("input.txt")
    c = cars(m)
    p = path(m)

    first_crash = (-1, -1)

    for t in range(1000):

        c = move(c, p)
        crashed = any(v.count('X') for v in c.values())
        if crashed:
            first_crash = next(k for k, v in c.items() if v.count('X'))
            break

    print("answer:", '{},{}'.format(*reversed(first_crash)))
