"""
--- Day 8: Memory Maneuver ---

The sleigh is much easier to pull than you'd expect for something its weight.
Unfortunately, neither you nor the Elves know which way the North Pole is from
here.

You check your wrist device for anything that might help. It seems to have some
kind of navigation system! Activating the navigation system produces more bad
news: "Failed to start navigation system. Could not read software license
file."

The navigation system's license file consists of a list of numbers (your puzzle
input). The numbers define a data structure which, when processed, produces
some kind of tree that can be used to calculate the license number.

The tree is made up of nodes; a single, outermost node forms the tree's root,
and it contains all other nodes in the tree (or contains nodes that contain
nodes, and so on).

Specifically, a node consists of:

  - A header, which is always exactly two numbers:
      - The quantity of child nodes.
      - The quantity of metadata entries.
  - Zero or more child nodes (as specified in the header).
  - One or more metadata entries (as specified in the header).

Each child node is itself a node that has its own header, child nodes, and
metadata. For example:

2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

In this example, each node of the tree is also marked with an underline
starting with a letter for easier identification. In it, there are four nodes:

  - A, which has 2 child nodes (B, C) and 3 metadata entries (1, 1, 2).
  - B, which has 0 child nodes and 3 metadata entries (10, 11, 12).
  - C, which has 1 child node (D) and 1 metadata entry (2).
  - D, which has 0 child nodes and 1 metadata entry (99).

The first check done on the license file is to simply add up all of the
metadata entries. In this example, that sum is 1+1+2+10+11+12+2+99=138.

What is the sum of all metadata entries?
"""
from typing import List


def read_input(filename: str) -> List[int]:

    with open("input.txt") as f:
    
        data = [int(x) for x in f.read().strip().split()]

    return data


def process(data: List[int]) -> int:

    def _search(A):

        num_children = A[0]
        num_metadata = A[1]
        remaining_data = A[2:]

        total = 0

        if num_children == 0:
            total += sum(remaining_data[:num_metadata])
            return total, remaining_data[num_metadata:]

        for i in range(num_children):
            sum_metadata, remaining_data = _search(remaining_data)
            total += sum_metadata

        total += sum(remaining_data[:num_metadata])

        return total, remaining_data[num_metadata:]

    result, _ = _search(data)

    return result


def test_process():

    A = [int(x) for x in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()]
    assert process(A) == 138


if __name__ == "__main__":

    test_process()
    print("all tests passed.")

    answer = process(read_input("input.txt"))
    print("answer:", answer)
