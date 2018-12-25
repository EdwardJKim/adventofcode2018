"""
--- Part Two ---

Okay, so the facility is big.

How many rooms have a shortest path from your current location that pass
through at least 1000 doors?
"""
from collections import deque
from typing import List, Deque, Set, Tuple
from part1 import search


def more_than_100_doors(grid:List[List[str]]) -> int:

    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'X':
                row, col = i, j

    q: Deque = deque()
    q.append((row, col, 0))

    visited: Set[Tuple[int, int]] = set()

    count = 0

    while q:

         row, col, dist = q.popleft()

         if (row, col) in visited or not (0 <= row < m and 0 <= col < n):
             continue
         visited.add((row, col))

         if dist >= 1000:
             count += 1

         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
             if (0 <= row + dr < m and 0 <= col + dc < n
                 and grid[row + dr][col + dc] in '|-'
                 and (row + dr, col + dc) not in visited):
                 q.append((row + 2 * dr, col + 2 * dc, dist + 1))

    return count


if __name__ == "__main__":

    answer = more_than_100_doors(search(open("input.txt").read()))
    print("answer:", answer)
