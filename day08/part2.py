"""
--- Part Two --- 
2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2
A----------------------------------
    B----------- C-----------
                     D-----

The second check is slightly more complicated: you need to find the value of
the root node (A in the example above).

The value of a node depends on whether it has child nodes.

If a node has no child nodes, its value is the sum of its metadata entries. So,
the value of node B is 10+11+12=33, and the value of node D is 99.

However, if a node does have child nodes, the metadata entries become indexes
which refer to those child nodes. A metadata entry of 1 refers to the first
child node, 2 to the second, 3 to the third, and so on. The value of this node
is the sum of the values of the child nodes referenced by the metadata entries.
If a referenced child node does not exist, that reference is skipped. A child
node can be referenced multiple time and counts each time it is referenced. A
metadata entry of 0 does not refer to any child node.

For example, again using the above nodes:

  - Node C has one metadata entry, 2. Because node C has only one child node, 2
    references a child node which does not exist, and so the value of node C is
    0.

  - Node A has three metadata entries: 1, 1, and 2. The 1 references node A's
    first child node, B, and the 2 references node A's second child node, C.
    Because node B has a value of 33 and node C has a value of 0, the value of
    node A is 33+33+0=66.

So, in this example, the value of the root node is 66.

What is the value of the root node?
"""
from typing import List
from part1 import read_input


def process(data: List[int]) -> int:

    def _search(A):

        num_children = A[0]
        num_metadata = A[1]
        remaining_data = A[2:]

        total = 0

        if num_children == 0:
            total += sum(remaining_data[:num_metadata])
            return total, remaining_data[num_metadata:]

        node_values = []
        for i in range(num_children):
            sum_metadata, remaining_data = _search(remaining_data)
            node_values.append(sum_metadata)

        metadata = remaining_data[:num_metadata]

        for i in metadata:
            if i > len(node_values):
                continue
            total += node_values[i - 1]

        return total, remaining_data[num_metadata:]

    result, _ = _search(data)

    return result


def test_process():

    A = [int(x) for x in "2 3 0 3 10 11 12 1 1 0 1 99 2 1 1 2".split()]
    assert process(A) == 66


if __name__ == "__main__":

    test_process()
    print("all tests passed.")

    answer = process(read_input("input.txt"))
    print("answer:", answer)
