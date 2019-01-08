from typing import List
from part1 import Units, read_input, fight


def boost(units: List[Units], amount: int) -> None:

    for unit in units:
        unit.attack_damage += amount


def test_boost():

    immune, infection = read_input("test.txt")
    boost(immune, 1570)
    immune_left, infection_left = fight(immune, infection)

    assert immune_left == 51
    assert infection_left == 0


if __name__ == "__main__":

    test_boost()

    boost_amount = 1
    while True:
        immune, infection = read_input("input.txt")
        boost(immune, boost_amount)
        immune_left, infection_left = fight(immune, infection)
        print(boost_amount, immune_left, infection_left)
        if infection_left == 0:
            break
        boost_amount += 1

    print("answer:", immune_left)
