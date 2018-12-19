"""
--- Part Two ---

Amidst the chaos, you notice that exactly one claim doesn't overlap by even a
single square inch of fabric with any other claim. If you can somehow draw
attention to it, maybe the Elves will be able to make Santa's suit after all!

For example, in the claims above, only claim 3 is intact after all claims are

What is the ID of the only claim that doesn't overlap?
"""
from typing import List, Tuple
from part1 import read_input, cover_fabric_with_claims


def find_non_overlapping_claim(
    claims: List[Tuple[int, int, int, int]]
    ) -> int:

    fabric = cover_fabric_with_claims(claims)

    for idx, claim in enumerate(claims):
        left, top, width, height = claim
        if all(fabric[i][j] < 2
            for i in range(top, top + height)
            for j in range(left, left + width)):
            return idx + 1

    return -1


def test_find_non_overlapping_claim():

    claims = [
        (1, 3, 4, 4),
        (3, 1, 4, 4),
        (5, 5, 2, 2)
    ]

    assert find_non_overlapping_claim(claims) == 3


if __name__ == "__main__":

    test_find_non_overlapping_claim()
    print("all tests passed.")

    answer = find_non_overlapping_claim(read_input("input.txt"))
    print("answer:", answer)
