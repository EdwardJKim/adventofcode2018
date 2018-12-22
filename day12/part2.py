"""
--- Part Two ---

You realize that 20 generations aren't enough. After all, these plants will
need to last another 1500 years to even reach your timeline, not to mention
your future.

After fifty billion (50000000000) generations, what is the sum of the numbers
of all pots which contain a plant?
"""
from part1 import get_initial_state_from_file, get_changes_from_file, grow
from typing import Dict, Tuple


def process(initial_state: str, changes: Dict[str, str], epochs: int) -> int:

    state = initial_state
    start_idx = 0

    cache: Dict[Tuple[int, str], Tuple[int, str]] = dict()

    for t in range(epochs):
        if (start_idx, state) in cache:
            start_idx, state = cache[start_idx, state]
        else:
            cache[start_idx, state] = grow(start_idx, state, changes)
            if cache[start_idx, state][1] == state:
                start_idx += epochs - t
                break
            start_idx, state = cache[start_idx, state]

    return sum(i + start_idx for i, x in enumerate(state) if x == '#')


def test_process():

    initial_state = get_initial_state_from_file("test.txt")
    changes = get_changes_from_file("test.txt")

    assert process(initial_state, changes, 20) == 325

    initial_state = get_initial_state_from_file("input.txt")
    changes = get_changes_from_file("input.txt")

    assert process(initial_state, changes, 20) == 3605


if __name__ == "__main__":

    test_process()
    print("all tests passed.")

    
    initial_state = get_initial_state_from_file("input.txt")
    changes = get_changes_from_file("input.txt")
    answer = process(initial_state, changes, 50000000000)
    print("answer:", answer)
