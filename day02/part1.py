"""
--- Day 2: Inventory Management System ---

You stop falling through time, catch your breath, and check the screen on the
device. "Destination reached. Current Year: 1518. Current Location: North Pole
Utility Closet 83N10." You made it! Now, to find those anomalies.

Outside the utility closet, you hear footsteps and a voice. "...I'm not sure
either. But now that so many people have chimneys, maybe he could sneak in that
way?" Another voice responds, "Actually, we've been working on a new kind of
suit that would let him fit through tight spaces like that. But, I heard that a
few days ago, they lost the prototype fabric, the design plans, everything!
Nobody on the team can even seem to remember important details of the project!"

"Wouldn't they have had enough fabric to fill several boxes in the warehouse?
They'd be stored together, so the box IDs should be similar. Too bad it would
take forever to search the warehouse for two similar box IDs..." They walk too
far away to hear any more.

Late at night, you sneak to the warehouse - who knows what kinds of paradoxes
you could cause if you were discovered - and use your fancy wrist device to
quickly scan every box and produce a list of the likely candidates (your puzzle
input).

To make sure you didn't miss any, you scan the likely candidate boxes again,
counting the number that have an ID containing exactly two of any letter and
then separately counting those with exactly three of any letter. You can
multiply those two counts together to get a rudimentary checksum and compare it
to what your device predicts.

For example, if you see the following box IDs:

  - abcdef contains no letters that appear exactly two or three times.
  - bababc contains two a and three b, so it counts for both.
  - abbcde contains two b, but no letter appears exactly three times.
  - abcccd contains three c, but no letter appears exactly two times.
  - aabcdd contains two a and two d, but it only counts once.
  - abcdee contains two e.
  - ababab contains three a and three b, but it only counts once.

Of these box IDs, four of them contain a letter which appears exactly twice,
and three of them contain a letter which appears exactly three times.
Multiplying these together produces a checksum of 4 * 3 = 12.

What is the checksum for your list of box IDs?
"""
from collections import Counter
from typing import List, Tuple


def count(s: str) -> Tuple[int, int]:

    counter = Counter(s)
    twos = threes = 0

    for k, v in counter.items():
        if v == 2:
            twos = 1
        if v == 3:
            threes = 1

    return twos, threes


def checksum(boxes: List[str]) -> int:

    twos = threes = 0
    for box in boxes:
        two, three = count(box)
        twos += two
        threes += three
    return twos * threes


def test_count():

    assert count("abcdef") == (0, 0)
    assert count("bababc") == (1, 1)
    assert count("abbcde") == (1, 0)
    assert count("abcccd") == (0, 1)
    assert count("aabcdd") == (1, 0)
    assert count("abcdee") == (1, 0)
    assert count("ababab") == (0, 1)


def test_checksum():

    example = [
        "abcdef",
        "bababc",
        "abbcde",
        "abcccd",
        "aabcdd",
        "abcdee",
        "ababab"
    ]

    assert checksum(example) == 12


def read_input(filename: str) -> List[str]:

    result = []
    with open(filename) as f:
        for line in f:
            result.append(line.strip())
    return result


if __name__ == "__main__":

    test_count()
    test_checksum()
    print("all tests passed.")

    answer = checksum(read_input("input.txt"))
    print("answer:", answer)
