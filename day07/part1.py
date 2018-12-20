"""
--- Day 7: The Sum of Its Parts ---

You find yourself standing on a snow-covered coastline; apparently, you landed
a little off course. The region is too hilly to see the North Pole from here,
but you do spot some Elves that seem to be trying to unpack something that
washed ashore. It's quite cold out, so you decide to risk creating a paradox by
asking them for directions.

"Oh, are you the search party?" Somehow, you can understand whatever Elves from
the year 1018 speak; you assume it's Ancient Nordic Elvish. Could the device on
your wrist also be a translator? "Those clothes don't look very warm; take
this." They hand you a heavy coat.

"We do need to find our way back to the North Pole, but we have higher
priorities at the moment. You see, believe it or not, this box contains
something that will solve all of Santa's transportation problems - at least,
that's what it looks like from the pictures in the instructions." It doesn't
seem like they can read whatever language it's in, but you can: "Sleigh kit.
Some assembly required."

"'Sleigh'? What a wonderful name! You must help us assemble this 'sleigh' at
once!" They start excitedly pulling more parts out of the box.

The instructions specify a series of steps and requirements about which steps
must be finished before others can begin (your puzzle input). Each step is
designated by a single letter. For example, suppose you have the following
instructions:

Step C must be finished before step A can begin.
Step C must be finished before step F can begin.
Step A must be finished before step B can begin.
Step A must be finished before step D can begin.
Step B must be finished before step E can begin.
Step D must be finished before step E can begin.
Step F must be finished before step E can begin.

Visually, these requirements look like this:


  -->A--->B--
 /    \      \
C      -->D----->E
 \           /
  ---->F-----

Your first goal is to determine the order in which the steps should be
completed. If more than one step is ready, choose the step which is first
alphabetically. In this example, the steps would be completed as follows:

  - Only C is available, and so it is done first.
  - Next, both A and F are available. A is first alphabetically, so it is done
    next.
  - Then, even though F was available earlier, steps B and D are now also
    available, and B is the first alphabetically of the three.
  - After that, only D and F are available. E is not available because only
    some of its prerequisites are complete. Therefore, D is completed next.
  - F is the only choice, so it is done next.
  - Finally, E is completed.

So, in this example, the correct order is CABDFE.

In what order should the steps in your instructions be completed?
"""
from collections import defaultdict
from typing import Dict, Set


def read_input(filename: str) -> Dict[str, Set[str]]:

    deps: Dict[str, Set[str]] = defaultdict(set)

    with open(filename) as f:
        for line in f:
            words = line.split()
            before, after = words[1], words[7]
            deps[after].add(before)

    return deps


def find_available(deps: Dict[str, Set[str]]):

    values = {x for value in deps.values() for x in value}
    remaining = [x for x in values if not deps[x]]

    return sorted(remaining, reverse=True)


def remove_dependency(value: str, deps: Dict[str, Set[str]]) -> None:

    keys = list(deps.keys())
    for k in keys:
        if value in deps[k]:
            deps[k].remove(value)


def process(deps: Dict[str, Set[str]]) -> str:

    available = find_available(deps)
    result = []
    while available:
        start = available.pop()
        result.append(start)
        remove_dependency(start, deps)
        available = find_available(deps)

    result.extend([x for x in deps.keys() if x not in result])

    return ''.join(result)


def test_read_input():

    deps = read_input("test.txt")

    assert deps.keys() == {'A', 'F', 'B', 'D', 'E'}
    assert deps['A'] == {'C'}
    assert deps['F'] == {'C'}
    assert deps['B'] == {'A'}
    assert deps['D'] == {'A'}
    assert deps['E'] == {'B', 'D', 'F'}


def test_find_available():

    available = find_available(read_input("test.txt"))
    assert available == ['C']


def test_process():

    deps = read_input("test.txt")
    assert process(deps) == "CABDFE"


if __name__ == "__main__":

    test_read_input()
    test_find_available()
    test_process()
    print("all tests passed.")

    answer = process(read_input("input.txt"))
    print("answer:", answer)
