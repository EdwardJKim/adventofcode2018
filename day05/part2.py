"""
--- Part Two ---

Time to improve the polymer.

One of the unit types is causing problems; it's preventing the polymer from 
collapsing as much as it should. Your goal is to figure out which unit type is
causing the most problems, remove all instances of it (regardless of polarity),
fully react the remaining polymer, and measure its length.

For example, again using the polymer dabAcCaCBAcCcaDA from above:

  - Removing all A/a units produces dbcCCBcCcD. Fully reacting this polymer
    produces dbCBcD, which has length 6.
  - Removing all B/b units produces daAcCaCAcCcaDA. Fully reacting this polymer
    produces daCAcaDA, which has length 8.
  - Removing all C/c units produces dabAaBAaDA. Fully reacting this polymer
    produces daDA, which has length 4.
  - Removing all D/d units produces abAcCaCBAcCcaA. Fully reacting this polymer
    produces abCBAc, which has length 6.

In this example, removing all C/c units was best, producing the answer 4.

What is the length of the shortest polymer you can produce by removing all
units of exactly one type and fully reacting the result?
"""
from part1 import read_input, scan


def remove_unit(polymer: str, unit: str) -> str:

    return ''.join(c for c in polymer if c.lower() != unit.lower())


def length_of_shorted_polymer(polymer: str) -> int:

    return min(scan(remove_unit(polymer, c)) for c in set(polymer.lower()))


def test_remove_unit():

    assert remove_unit("dabAcCaCBAcCcaDA", "a") == "dbcCCBcCcD"
    assert remove_unit("dabAcCaCBAcCcaDA", "A") == "dbcCCBcCcD"
    assert remove_unit("dabAcCaCBAcCcaDA", "b") == "daAcCaCAcCcaDA"
    assert remove_unit("dabAcCaCBAcCcaDA", "B") == "daAcCaCAcCcaDA"
    assert remove_unit("dabAcCaCBAcCcaDA", "c") == "dabAaBAaDA"
    assert remove_unit("dabAcCaCBAcCcaDA", "C") == "dabAaBAaDA"
    assert remove_unit("dabAcCaCBAcCcaDA", "d") == "abAcCaCBAcCcaA"
    assert remove_unit("dabAcCaCBAcCcaDA", "D") == "abAcCaCBAcCcaA"


def test_length_of_shorted_polymer():

    assert length_of_shorted_polymer("dabAcCaCBAcCcaDA") == 4


if __name__ == "__main__":

    test_remove_unit()
    test_length_of_shorted_polymer()
    print("all tests passed.")

    answer = length_of_shorted_polymer(read_input("input.txt"))
    print("answer:", answer)
