"""
--- Part Two ---

Confident that your list of box IDs is complete, you're ready to find the boxes
full of prototype fabric.

The boxes will have IDs which differ by exactly one character at the same
position in both strings. For example, given the following box IDs:

abcde
fghij
klmno
pqrst
fguij
axcye
wvxyz

The IDs abcde and axcye are close, but they differ by two characters (the
second and fourth). However, the IDs fghij and fguij differ by exactly one
character, the third (h and u). Those must be the correct boxes.

What letters are common between the two correct box IDs? (In the example above,
this is found by removing the differing character from either ID, producing
fgij.)
"""
import itertools
from typing import List, Tuple
from part1 import read_input


def distance(s: str, t: str) -> int:

    return sum(c != d for c, d in zip(s, t))


def common_letters(s: str, t: str) -> str:

    return ''.join(c for c, d in zip(s, t) if c == d)


def find_boxes(boxes: List[str]) -> Tuple[str, str]:

    for box1, box2 in itertools.permutations(boxes, 2):
        if distance(box1, box2) == 1:
            return box1, box2

    return '', ''


def test_distance():

    assert distance("abcde", "axcye") == 2
    assert distance("fghij", "fguij") == 1


def test_common_letters():

    assert common_letters("abcde", "axcye") == "ace"
    assert common_letters("fghij", "fguij") == "fgij"


def test_find_boxes():

    example = [
        "abcde",
        "fghij",
        "klmno",
        "pqrst",
        "fguij",
        "axcye",
        "wvxyz"
    ]

    assert find_boxes(example) == ("fghij", "fguij")


if __name__ == "__main__":

    test_distance()
    test_common_letters()
    test_find_boxes()
    print("all tests passed.")

    answer = common_letters(*find_boxes(read_input("input.txt")))
    print("answer:", answer)
