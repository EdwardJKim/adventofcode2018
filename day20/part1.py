"""
--- Day 20: A Regular Map ---

While you were learning about instruction pointers, the Elves made considerable 
progress. When you look up, you discover that the North Pole base construction 
project has completely surrounded you.

The area you are in is made up entirely of rooms and doors. The rooms are 
arranged in a grid, and rooms only connect to adjacent rooms when a door is 
present between them.

For example, drawing rooms as ., walls as #, doors as | or -, your current 
position as X, and where north is up, the area you're in might look like this:

#####
#.|.#
#-###
#.|X#
#####

You get the attention of a passing construction Elf and ask for a map. "I don't 
have time to draw out a map of this place - it's huge. Instead, I can give you 
directions to every room in the facility!" He writes down some directions on a 
piece of parchment and runs off. In the example above, the instructions might 
have been ^WNE$, a regular expression or "regex" (your puzzle input).

The regex matches routes (like WNE for "west, north, east") that will take you 
from your current room through various doors in the facility. In aggregate, the 
routes will take you through every door in the facility at least once; mapping 
out all of these routes will let you build a proper map and find your way 
around.

^ and $ are at the beginning and end of your regex; these just mean that the 
regex doesn't match anything outside the routes it describes. (Specifically, ^ 
matches the start of the route, and $ matches the end of it.) These characters 
will not appear elsewhere in the regex.

The rest of the regex matches various sequences of the characters N (north), S 
(south), E (east), and W (west). In the example above, ^WNE$ matches only one 
route, WNE, which means you can move west, then north, then east from your 
current position. Sequences of letters like this always match that exact route 
in the same order.

Sometimes, the route can branch. A branch is given by a list of options 
separated by pipes (|) and wrapped in parentheses. So, ^N(E|W)N$ contains a 
branch: after going north, you must choose to go either east or west before 
finishing your route by going north again. By tracing out the possible routes 
after branching, you can determine where the doors are and, therefore, where 
the rooms are in the facility.

For example, consider this regex: ^ENWWW(NEEE|SSE(EE|N))$

This regex begins with ENWWW, which means that from your current position, all 
routes must begin by moving east, north, and then west three times, in that 
order. After this, there is a branch. Before you consider the branch, this is 
what you know about the map so far, with doors you aren't sure about marked 
with a ?:

#?#?#?#?#
?.|.|.|.?
#?#?#?#-#
    ?X|.?
    #?#?#

After this point, there is (NEEE|SSE(EE|N)). This gives you exactly two 
options: NEEE and SSE(EE|N). By following NEEE, the map now looks like this:

#?#?#?#?#
?.|.|.|.?
#-#?#?#?#
?.|.|.|.?
#?#?#?#-#
    ?X|.?
    #?#?#

Now, only SSE(EE|N) remains. Because it is in the same parenthesized group as 
NEEE, it starts from the same room NEEE started in. It states that starting 
from that point, there exist doors which will allow you to move south twice, 
then east; this ends up at another branch. After that, you can either move east 
twice or north once. This information fills in the rest of the doors:

#?#?#?#?#
?.|.|.|.?
#-#?#?#?#
?.|.|.|.?
#-#?#?#-#
?.?.?X|.?
#-#-#?#?#
?.|.|.|.?
#?#?#?#?#

Once you've followed all possible routes, you know the remaining unknown parts 
are all walls, producing a finished map of the facility:

#########
#.|.|.|.#
#-#######
#.|.|.|.#
#-#####-#
#.#.#X|.#
#-#-#####
#.|.|.|.#
#########

Sometimes, a list of options can have an empty option, like (NEWS|WNSE|). This 
means that routes at this point could effectively skip the options in 
parentheses and move on immediately. For example, consider this regex and the 
corresponding map:

^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$

###########
#.|.#.|.#.#
#-###-#-#-#
#.|.|.#.#.#
#-#####-#-#
#.#.#X|.#.#
#-#-#####-#
#.#.|.|.|.#
#-###-###-#
#.|.|.#.|.#
###########

This regex has one main route which, at three locations, can optionally include 
additional detours and be valid: (NEWS|), (WNSE|), and (SWEN|). Regardless of 
which option is taken, the route continues from the position it is left at 
after taking those steps. So, for example, this regex matches all of the 
following routes (and more that aren't listed here):

ENNWSWWSSSEENEENNN
ENNWSWWNEWSSSSEENEENNN
ENNWSWWNEWSSSSEENEESWENNNN
ENNWSWWSSSEENWNSEEENNN

By following the various routes the regex matches, a full map of all of the 
doors and rooms in the facility can be assembled.

To get a sense for the size of this facility, you'd like to determine which 
room is furthest from you: specifically, you would like to find the room for 
which the shortest path to that room would require passing through the most 
doors.

In the first example (^WNE$), this would be the north-east corner 3 doors away.
In the second example (^ENWWW(NEEE|SSE(EE|N))$), this would be the south-east 
corner 10 doors away.
In the third example (^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$), this would be 
the north-east corner 18 doors away.
Here are a few more examples:

Regex: ^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$
Furthest room requires passing 23 doors

#############
#.|.|.|.|.|.#
#-#####-###-#
#.#.|.#.#.#.#
#-#-###-#-#-#
#.#.#.|.#.|.#
#-#-#-#####-#
#.#.#.#X|.#.#
#-#-#-###-#-#
#.|.#.|.#.#.#
###-#-###-#-#
#.|.#.|.|.#.#
#############

Regex: ^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$
Furthest room requires passing 31 doors

###############
#.|.|.|.#.|.|.#
#-###-###-#-#-#
#.|.#.|.|.#.#.#
#-#########-#-#
#.#.|.|.|.|.#.#
#-#-#########-#
#.#.#.|X#.|.#.#
###-#-###-#-#-#
#.|.#.#.|.#.|.#
#-###-#####-###
#.|.#.|.|.#.#.#
#-#-#####-#-#-#
#.#.|.|.|.#.|.#
###############

What is the largest number of doors you would be required to pass through to 
reach a room? That is, find the room for which the shortest path from your 
starting location to that room would require passing through the most doors; 
what is the fewest doors you can pass through to reach it?
"""
from collections import deque
from typing import List, Deque, Set, Tuple


def create_grid(regex: str) -> List[List[str]]:

    n = regex.count('N')
    s = regex.count('S')
    e = regex.count('E')
    w = regex.count('W')

    grid = []
    for i in range(n + s + 1):
        grid.append("#?" + "#?" * (e + w) + "#")
        grid.append("?." + "?." * (e + w) + "?")
    grid.append("#?" + "#?" * (e + w) + "#")

    result = [list(row) for row in grid]

    return result


def search(regex: str) -> List[List[str]]:

    def _move(row, col, remaining):

        if not remaining:
            return

        left, right = 0, len(remaining) - 1
        while left <= right:
            c = remaining[left]
            if c == 'N':
                grid[row - 1][col] = '-'
                row -= 2
            if c == 'S':
                grid[row + 1][col] = '-'
                row += 2
            if c == 'E':
                grid[row][col + 1] = '|'
                col += 2
            if c == 'W':
                grid[row][col - 1] = '|'
                col -= 2
            if c == '(':
                right_paren = right
                while left < right_paren and remaining[right_paren] != ')':
                    right_paren -= 1
                stack = []
                for mid in range(left + 1, right_paren + 1):
                    if remaining[mid] in '|)' and not stack:
                        _move(row, col, remaining[left + 1: mid])
                        left = mid
                    elif remaining[mid] == '(':
                        stack.append('(')
                    elif remaining[mid] == ')' and stack:
                        stack.pop()
            left += 1

        return

    grid = create_grid(regex)
    m, n = len(grid), len(grid[0])
    start_row, start_col = (m - 1) // 2, (n - 1) // 2
    grid[start_row][start_col] = 'X'

    _move(start_row, start_col, regex)

    for i in range(m):
        for j in range(n):
            if grid[i][j] == '?':
                grid[i][j] = '#'

    return grid


def shortest_path_to_furthest_room(grid:List[List[str]]) -> int:

    m, n = len(grid), len(grid[0])

    for i in range(m):
        for j in range(n):
            if grid[i][j] == 'X':
                row, col = i, j

    q: Deque = deque()
    q.append((row, col, 0))

    visited: Set[Tuple[int, int]] = set()

    furthest = 0

    while q:

         row, col, dist = q.popleft()

         if (row, col) in visited or not (0 <= row < m and 0 <= col < n):
             continue
         visited.add((row, col))

         furthest = max(furthest, dist)

         for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
             if (0 <= row + dr < m and 0 <= col + dc < n
                 and grid[row + dr][col + dc] in '|-'
                 and (row + dr, col + dc) not in visited):
                 q.append((row + 2 * dr, col + 2 * dc, dist + 1))

    return furthest


def test_search():

    regex = "^WNE$"
    grid = search(regex)
    assert shortest_path_to_furthest_room(grid) == 3

    regex = "^ENWWW(NEEE|SSE(EE|N))$"
    grid = search(regex)
    assert shortest_path_to_furthest_room(grid) == 10

    regex = "^ENNWSWW(NEWS|)SSSEEN(WNSE|)EE(SWEN|)NNN$"
    grid = search(regex)
    assert shortest_path_to_furthest_room(grid) == 18

    regex = "^ESSWWN(E|NNENN(EESS(WNSE|)SSS|WWWSSSSE(SW|NNNE)))$"
    grid = search(regex)
    assert shortest_path_to_furthest_room(grid) == 23

    regex = "^WSSEESWWWNW(S|NENNEEEENN(ESSSSW(NWSW|SSEN)|WSWWN(E|WWS(E|SS))))$"
    grid = search(regex)
    assert shortest_path_to_furthest_room(grid) == 31


if __name__ == "__main__":

    test_search()
    print("all tests passed.")

    answer = shortest_path_to_furthest_room(search(open("input.txt").read()))
    print("answer:", answer)
