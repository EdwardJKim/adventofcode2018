"""
--- Part Two ---

As it turns out, you got the Elves' plan backwards. They actually want to know
how many recipes appear on the scoreboard to the left of the first recipes
whose scores are the digits from your puzzle input.

51589 first appears after 9 recipes.
01245 first appears after 5 recipes.
92510 first appears after 18 recipes.
59414 first appears after 2018 recipes.

How many recipes appear on the scoreboard to the left of the score sequence in
your puzzle input?
"""
def process(n: str) -> int:

    scores = [3, 7]
    first_elf, second_elf = 0, 1
    seq = [int(c) for c in n]
    i = 0

    while True:

        new_recipe = scores[first_elf] + scores[second_elf]
        scores.extend(int(c) for c in str(new_recipe))
        first_elf = (first_elf + 1 + scores[first_elf]) % len(scores)
        second_elf = (second_elf + 1 + scores[second_elf]) % len(scores)

        if scores[i: i + len(seq)] == seq:
            break

        i += 1

    return i


def test_process():

    assert process("51589") == 9
    assert process("01245") == 5
    assert process("92510") == 18
    assert process("59414") == 2018


if __name__ == "__main__":

    test_process()
    print("all tests passed.")

    n = input("Enter your puzzle input: ")
    answer = process(n.strip())
    print("answer:", answer)
