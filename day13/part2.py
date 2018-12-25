"""
--- Part Two ---

There isn't much you can do to prevent crashes in this ridiculous system.
However, by predicting the crashes, the Elves know where to be in advance and
instantly remove the two crashing carts the moment any crash occurs.

They can proceed like this for a while, but eventually, they're going to run
out of carts. It could be useful to figure out where the last cart that hasn't
crashed will end up.

For example:

/>-<\  
|   |  
| /<+-\
| | | v
\>+</ |
  |   ^
  \<->/

/---\  
|   |  
| v-+-\
| | | |
\-+-/ |
  |   |
  ^---^

/---\  
|   |  
| /-+-\
| v | |
\-+-/ |
  ^   ^
  \---/

/---\  
|   |  
| /-+-\
| | | |
\-+-/ ^
  |   |
  \---/

After four very expensive crashes, a tick ends with only one cart remaining;
its final location is 6,4.

What is the location of the last cart at the end of the first tick where it is
the only cart left?
"""
from part1 import cars, path, read_input, STATUS
from typing import Dict, Tuple, List


def move(
    cars: Dict[Tuple[int, int], Tuple[str, int]],
    path:List[List[str]]
    ) -> Dict[Tuple[int, int], Tuple[str, int]]:

    result: Dict[Tuple[int, int], Tuple[str, int]] = dict(cars)

    for row, col in sorted(cars):

        if (row, col) not in result:
            continue

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
            del result[row + dr, col + dc]
        else:
            result[row + dr, col + dc] = (next_symbol, next_turn)

    return result


def remove_crash(
    cars: Dict[Tuple[int, int], Tuple[str, int]]
    ) -> Dict[Tuple[int, int], Tuple[str, int]]:

    return {k: v for k, v in cars.items() if v.count('X') == 0}


def test_remove_crash():

    example = [
        "/>-<\\  ",
        "|   |  ",
        "| /<+-\\",
        "| | | v",
        "\\>+</ |",
        "  |   ^",
        "  \\<->/",
    ]
    example = [list(line) for line in example]

    c = cars(example)
    p = path(example)

    while len(c) > 1:

        c = move(c, p)
        while any(v.count('X') for v in c.values()):
            c = remove_crash(c)

    assert next(iter(c.keys())) == (4, 6)


if __name__ == "__main__":

    test_remove_crash()
    print("all tests passed.")

    m = read_input("input.txt")
    c = cars(m)
    p = path(m)

    while len(c) > 1:

        c = move(c, p)
        while any(v.count('X') for v in c.values()):
            c = remove_crash(c)

    print("answer:", '{},{}'.format(*reversed(next(iter(c.keys())))))
