"""
--- Part Two ---
This important natural resource will need to last for at least thousands of 
years. Are the Elves collecting this lumber sustainably?

What will the total resource value of the lumber collection area be after 
1000000000 minutes?
"""
from part1 import change, get_resource_value
from typing import Dict


if __name__ == "__main__":

    area = [list(line.strip()) for line in open("input.txt")]

    visited: Dict[str, int] = dict()
    joined = ''.join(''.join(row) for row in area)
    visited[joined] = 0

    target_minutes = 1000000000
    t = 0
    already_jumped = False

    while t < target_minutes:
        t += 1
        area = change(area)
        joined = ''.join(''.join(row) for row in area)
        if joined in visited and not already_jumped:
            jump = (target_minutes - t) // (t - visited[joined])
            t += jump * (t - visited[joined])
            already_jumped = True
            continue
        visited[joined] = t

    answer = get_resource_value(area)
    print("answer:", answer)
