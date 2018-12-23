"""
--- Day 15: Beverage Bandits ---

Having perfected their hot chocolate, the Elves have a new problem: the Goblins 
that live in these caves will do anything to steal it. Looks like they're here 
for a fight.

You scan the area, generating a map of the walls (#), open cavern (.), and 
starting position of every Goblin (G) and Elf (E) (your puzzle input).

Combat proceeds in rounds; in each round, each unit that is still alive takes a 
turn, resolving all of its actions before the next unit's turn begins. On each 
unit's turn, it tries to move into range of an enemy (if it isn't already) and 
then attack (if it is in range).

All units are very disciplined and always follow very strict combat rules. 
Units never move or attack diagonally, as doing so would be dishonorable. When 
multiple choices are equally valid, ties are broken in reading order: 
top-to-bottom, then left-to-right. For instance, the order in which units take 
their turns within a round is the reading order of their starting positions in 
that round, regardless of the type of unit or whether other units have moved 
after the round started. For example:

                 would take their
These units:   turns in this order:
  #######           #######
  #.G.E.#           #.1.2.#
  #E.G.E#           #3.4.5#
  #.G.E.#           #.6.7.#
  #######           #######

Each unit begins its turn by identifying all possible targets (enemy units). If 
no targets remain, combat ends.

Then, the unit identifies all of the open squares (.) that are in range of each 
target; these are the squares which are adjacent (immediately up, down, left, 
or right) to any target and which aren't already occupied by a wall or another 
unit. Alternatively, the unit might already be in range of a target. If the 
unit is not already in range of a target, and there are no open squares which 
are in range of a target, the unit ends its turn.

If the unit is already in range of a target, it does not move, but continues 
its turn with an attack. Otherwise, since it is not in range of a target, it 
moves.

To move, the unit first considers the squares that are in range and determines 
which of those squares it could reach in the fewest steps. A step is a single 
movement to any adjacent (immediately up, down, left, or right) open (.) 
square. Units cannot move into walls or other units. The unit does this while 
considering the current positions of units and does not do any prediction about 
where units will be later. If the unit cannot reach (find an open path to) any 
of the squares that are in range, it ends its turn. If multiple squares are in 
range and tied for being reachable in the fewest steps, the square which is 
first in reading order is chosen. For example:

Targets:      In range:     Reachable:    Nearest:      Chosen:
#######       #######       #######       #######       #######
#E..G.#       #E.?G?#       #E.@G.#       #E.!G.#       #E.+G.#
#...#.#  -->  #.?.#?#  -->  #.@.#.#  -->  #.!.#.#  -->  #...#.#
#.G.#G#       #?G?#G#       #@G@#G#       #!G.#G#       #.G.#G#
#######       #######       #######       #######       #######

In the above scenario, the Elf has three targets (the three Goblins):

Each of the Goblins has open, adjacent squares which are in range (marked with 
a ? on the map).
Of those squares, four are reachable (marked @); the other two (on the right) 
would require moving through a wall or unit to reach.
Three of these reachable squares are nearest, requiring the fewest steps (only 
2) to reach (marked !).
Of those, the square which is first in reading order is chosen (+).
The unit then takes a single step toward the chosen square along the shortest 
path to that square. If multiple steps would put the unit equally closer to its 
destination, the unit chooses the step which is first in reading order. (This 
requires knowing when there is more than one shortest path so that you can 
consider the first step of each such path.) For example:

In range:     Nearest:      Chosen:       Distance:     Step:
#######       #######       #######       #######       #######
#.E...#       #.E...#       #.E...#       #4E212#       #..E..#
#...?.#  -->  #...!.#  -->  #...+.#  -->  #32101#  -->  #.....#
#..?G?#       #..!G.#       #...G.#       #432G2#       #...G.#
#######       #######       #######       #######       #######

The Elf sees three squares in range of a target (?), two of which are nearest 
(!), and so the first in reading order is chosen (+). Under "Distance", each 
open square is marked with its distance from the destination square; the two 
squares to which the Elf could move on this turn (down and to the right) are 
both equally good moves and would leave the Elf 2 steps from being in range of 
the Goblin. Because the step which is first in reading order is chosen, the Elf 
moves right one square.

Here's a larger example of movement:

Initially:
#########
#G..G..G#
#.......#
#.......#
#G..E..G#
#.......#
#.......#
#G..G..G#
#########

After 1 round:
#########
#.G...G.#
#...G...#
#...E..G#
#.G.....#
#.......#
#G..G..G#
#.......#
#########

After 2 rounds:
#########
#..G.G..#
#...G...#
#.G.E.G.#
#.......#
#G..G..G#
#.......#
#.......#
#########

After 3 rounds:
#########
#.......#
#..GGG..#
#..GEG..#
#G..G...#
#......G#
#.......#
#.......#
#########

Once the Goblins and Elf reach the positions above, they all are either in 
range of a target or cannot find any square in range of a target, and so none 
of the units can move until a unit dies.

After moving (or if the unit began its turn in range of a target), the unit 
attacks.

To attack, the unit first determines all of the targets that are in range of it 
by being immediately adjacent to it. If there are no such targets, the unit 
ends its turn. Otherwise, the adjacent target with the fewest hit points is 
selected; in a tie, the adjacent target with the fewest hit points which is 
first in reading order is selected.

The unit deals damage equal to its attack power to the selected target, 
reducing its hit points by that amount. If this reduces its hit points to 0 or 
fewer, the selected target dies: its square becomes . and it takes no further 
turns.

Each unit, either Goblin or Elf, has 3 attack power and starts with 200 hit 
points.

For example, suppose the only Elf is about to attack:

       HP:            HP:
G....  9       G....  9  
..G..  4       ..G..  4  
..EG.  2  -->  ..E..     
..G..  2       ..G..  2  
...G.  1       ...G.  1  

The "HP" column shows the hit points of the Goblin to the left in the 
corresponding row. The Elf is in range of three targets: the Goblin above it 
(with 4 hit points), the Goblin to its right (with 2 hit points), and the 
Goblin below it (also with 2 hit points). Because three targets are in range, 
the ones with the lowest hit points are selected: the two Goblins with 2 hit 
points each (one to the right of the Elf and one below the Elf). Of those, the 
Goblin first in reading order (the one to the right of the Elf) is selected. 
The selected Goblin's hit points (2) are reduced by the Elf's attack power (3), 
reducing its hit points to -1, killing it.

After attacking, the unit's turn ends. Regardless of how the unit's turn ends, 
the next unit in the round takes its turn. If all units have taken turns in 
this round, the round ends, and a new round begins.

The Elves look quite outnumbered. You need to determine the outcome of the 
battle: the number of full rounds that were completed (not counting the round 
in which combat ends) multiplied by the sum of the hit points of all remaining 
units at the moment combat ends. (Combat only ends when a unit finds no targets 
during its turn.)

Below is an entire sample combat. Next to each map, each row's units' hit 
points are listed from left to right.

Initially:
#######   
#.G...#   G(200)
#...EG#   E(200), G(200)
#.#.#G#   G(200)
#..G#E#   G(200), E(200)
#.....#   
#######   

After 1 round:
#######   
#..G..#   G(200)
#...EG#   E(197), G(197)
#.#G#G#   G(200), G(197)
#...#E#   E(197)
#.....#   
#######   

After 2 rounds:
#######   
#...G.#   G(200)
#..GEG#   G(200), E(188), G(194)
#.#.#G#   G(194)
#...#E#   E(194)
#.....#   
#######   

Combat ensues; eventually, the top Elf dies:

After 23 rounds:
#######   
#...G.#   G(200)
#..G.G#   G(200), G(131)
#.#.#G#   G(131)
#...#E#   E(131)
#.....#   
#######   

After 24 rounds:
#######   
#..G..#   G(200)
#...G.#   G(131)
#.#G#G#   G(200), G(128)
#...#E#   E(128)
#.....#   
#######   

After 25 rounds:
#######   
#.G...#   G(200)
#..G..#   G(131)
#.#.#G#   G(125)
#..G#E#   G(200), E(125)
#.....#   
#######   

After 26 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(122)
#...#E#   E(122)
#..G..#   G(200)
#######   

After 27 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(119)
#...#E#   E(119)
#...G.#   G(200)
#######   

After 28 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(116)
#...#E#   E(113)
#....G#   G(200)
#######   

More combat ensues; eventually, the bottom Elf dies:

After 47 rounds:
#######   
#G....#   G(200)
#.G...#   G(131)
#.#.#G#   G(59)
#...#.#   
#....G#   G(200)
#######   

Before the 48th round can finish, the top-left Goblin finds that there are no 
targets remaining, and so combat ends. So, the number of full rounds that were 
completed is 47, and the sum of the hit points of all remaining units is 
200+131+59+200 = 590. From these, the outcome of the battle is 47 * 590 = 27730.

Here are a few example summarized combats:

#######       #######
#G..#E#       #...#E#   E(200)
#E#E.E#       #E#...#   E(197)
#G.##.#  -->  #.E##.#   E(185)
#...#E#       #E..#E#   E(200), E(200)
#...E.#       #.....#
#######       #######

Combat ends after 37 full rounds
Elves win with 982 total hit points left
Outcome: 37 * 982 = 36334
#######       #######   
#E..EG#       #.E.E.#   E(164), E(197)
#.#G.E#       #.#E..#   E(200)
#E.##E#  -->  #E.##.#   E(98)
#G..#.#       #.E.#.#   E(200)
#..E#.#       #...#.#   
#######       #######   

Combat ends after 46 full rounds
Elves win with 859 total hit points left
Outcome: 46 * 859 = 39514
#######       #######   
#E.G#.#       #G.G#.#   G(200), G(98)
#.#G..#       #.#G..#   G(200)
#G.#.G#  -->  #..#..#   
#G..#.#       #...#G#   G(95)
#...E.#       #...G.#   G(200)
#######       #######   

Combat ends after 35 full rounds
Goblins win with 793 total hit points left
Outcome: 35 * 793 = 27755
#######       #######   
#.E...#       #.....#   
#.#..G#       #.#G..#   G(200)
#.###.#  -->  #.###.#   
#E#G#G#       #.#.#.#   
#...#G#       #G.G#G#   G(98), G(38), G(200)
#######       #######   

Combat ends after 54 full rounds
Goblins win with 536 total hit points left
Outcome: 54 * 536 = 28944
#########       #########   
#G......#       #.G.....#   G(137)
#.E.#...#       #G.G#...#   G(200), G(200)
#..##..G#       #.G##...#   G(200)
#...##..#  -->  #...##..#   
#...#...#       #.G.#...#   G(200)
#.G...G.#       #.......#   
#.....G.#       #.......#   
#########       #########   

Combat ends after 20 full rounds
Goblins win with 937 total hit points left
Outcome: 20 * 937 = 18740

What is the outcome of the combat described in your puzzle input?
"""
from collections import deque
from typing import List, Dict, Tuple, Deque, Set


class Mob:

    def __init__(self, mob_type: str, row: int, col: int) -> None:

        self.type = mob_type
        self.row = row
        self.col = col
        self.hp = 200
        self.power = 3
        self.alive = True


class Board:

    def __init__(self) -> None:

        self.board = [['.'] * 10 for _ in range(10)]
        self.mobs: Dict[Tuple[int, int], Mob] = dict()
        self.rounds = 0

    @property
    def sum_remaining_hp(self) -> int:

        return sum(mob.hp for _, mob in self.mobs.items() if mob.alive)

    @property
    def outcome(self) -> int:

        return self.rounds * self.sum_remaining_hp

    def read_from_file(self, filename: str) -> List[List[str]]:

        with open(filename) as f:
            self.board = [list(line.strip()) for line in f]

        return self.board

    def read_from_array(self, array: List[List[str]]) -> List[List[str]]:

        self.board = array

        return self.board

    def print_board(self) -> None:

        print("After {} rounds:".format(self.rounds))
        for i, r in enumerate(self.board):
            line = ''.join(r) + ' ' * 4
            for j, c in enumerate(r):
                if c == 'G':
                    line += "G(" + str(self.mobs[i, j].hp) + ") "
                if c == 'E':
                    line += "E(" + str(self.mobs[i, j].hp) + ") "
            print(line)

    def get_mobs(self) -> Dict[Tuple[int, int], Mob]:

        for i, r in enumerate(self.board):
            for j, c in enumerate(r):
                if c == 'G':
                    self.mobs[i, j] = Mob('G', i, j)
                if c == 'E':
                    self.mobs[i, j] = Mob('E', i, j)

        return self.mobs

    def are_both_teams_alive(self) -> bool:

        alive_mobs = [mob.type for mob in self.mobs.values() if mob.alive]

        return len(set(alive_mobs)) > 1
        

    def play(self) -> None:

        mobs = self.get_mobs()

        while self.are_both_teams_alive():

            remaining = sorted(
                [k for k, v in self.mobs.items() if v.alive],
                reverse=True
            )

            while remaining:

                row, col = remaining.pop()

                if not self.mobs[row, col].alive:
                    continue

                if not self.are_both_teams_alive():
                    return

                in_range_targets = self.get_in_range_targets(row, col)
                if in_range_targets:
                    enemy = in_range_targets[0]
                    if (self.attack_enemy(row, col, *enemy)
                        and enemy in remaining):
                        remaining.remove(enemy)
                    continue

                self.board[row][col] = '.'
                new_row, new_col = self.move_mob(row, col)
                self.mobs[new_row, new_col] = self.mobs.pop((row, col))
                self.board[new_row][new_col] = self.mobs[new_row, new_col].type

                in_range_targets = self.get_in_range_targets(new_row, new_col)
                if in_range_targets:
                    enemy = in_range_targets[0]
                    if (self.attack_enemy(new_row, new_col, *enemy)
                        and enemy in remaining):
                        remaining.remove(enemy)
                    continue

            self.rounds += 1


    def get_in_range_targets(
        self,
        row: int,
        col: int
        ) -> List[Tuple[int, int]]:

        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]

        result = []
        for dr, dc in offsets:
            if ((row, col) in self.mobs
                and (row + dr, col + dc) in self.mobs
                and self.mobs[row + dr, col + dc].alive
                and self.mobs[row, col].type != self.mobs[row + dr, col + dc].type):

                result.append((self.mobs[row + dr, col + dc].hp, row + dr, col + dc))

        return [x[1:] for x in sorted(result)]

    def attack_enemy(
        self,
        mob_row: int,
        mob_col: int,
        enemy_row: int,
        enemy_col: int
        ) -> bool:

        self.mobs[enemy_row, enemy_col].hp -= self.mobs[mob_row, mob_col].power
        if self.mobs[enemy_row, enemy_col].hp <= 0:
            self.board[enemy_row][enemy_col] = '.'
            self.mobs[enemy_row, enemy_col].alive = False
            return True

        return False

    def move_mob(self, row: int, col: int) -> Tuple[int, int]:

        cur = (row, col)
        if not (cur in self.mobs):
            raise ValueError("Invalid coordinates: ", cur)

        enemies = [
            x for x in sorted(self.mobs)
            if self.mobs[cur].type != self.mobs[x].type and self.mobs[x].alive
        ]

        offsets = [(-1, 0), (0, -1), (0, 1), (1, 0)]
        in_range = []
        for r, c in enemies:
            for dr, dc in offsets:
                if self.board[r + dr][c + dc] == '.':
                    in_range.append((r + dr, c + dc))

        reachable = dict()
        q: Deque[Tuple[int, int, int]] = deque()
        q.append((row, col, 0))
        visited: Set[Tuple[int, int]] = set()
        while q:
            r, c, d = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) in in_range:
                reachable[r, c] = d
            for dr, dc in offsets:
                if (0 <= r + dr < len(self.board)
                    and 0 <= c + dc < len(self.board[0])
                    and self.board[r + dr][c + dc] == '.'):
                    q.append((r + dr, c + dc, d + 1))

        nearest = [
            k for k, v in reachable.items() if v == min(reachable.values())
        ]
        if not nearest:
            return row, col

        nearest.sort()
        chosen = nearest[0]

        distance = {
            (row + dr, col + dc): float('inf') for dr, dc in offsets
        }
        q = deque()
        q.append((*chosen, 0))
        visited = set()
        while q:
            r, c, d = q.popleft()
            if (r, c) in visited:
                continue
            visited.add((r, c))
            if (r, c) in distance:
                distance[r, c] = d
            for dr, dc in offsets:
                if (0 <= r + dr < len(self.board)
                    and 0 <= c + dc < len(self.board[0])
                    and self.board[r + dr][c + dc] == '.'):
                    q.append((r + dr, c + dc, d + 1))

        step = [
            k for k, v in distance.items()
            if v < float('inf') and v == min(distance.values())
        ]
        step.sort()
        if step:
            return step[0]

        return row, col


def test_all():

    example = [
        "#######",
        "#.G...#",
        "#...EG#",
        "#.#.#G#",
        "#..G#E#",
        "#.....#",
        "#######"
    ]
    example = [list(row) for row in example]

    result = [
        "#######",
        "#G....#",
        "#.G...#",
        "#.#.#G#",
        "#...#.#",
        "#....G#",
        "#######"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 47
    assert board.board == result
    assert board.mobs[1, 1].hp == 200
    assert board.mobs[2, 2].hp == 131
    assert board.mobs[3, 5].hp == 59
    assert board.mobs[4, 5].alive is False
    assert board.mobs[5, 5].hp == 200

    assert board.sum_remaining_hp == 590
    assert board.outcome == 27730


    example = [
        "#######",
        "#G..#E#",
        "#E#E.E#",
        "#G.##.#",
        "#...#E#",
        "#...E.#",
        "#######"
    ]
    example = [list(row) for row in example]

    result = [
        "#######",
        "#...#E#",
        "#E#...#",
        "#.E##.#",
        "#E..#E#",
        "#.....#",
        "#######"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 37
    assert board.board == result
    assert board.sum_remaining_hp == 982
    assert board.outcome == 36334

    example = [
        "#######",
        "#E..EG#",
        "#.#G.E#", 
        "#E.##E#",
        "#G..#.#",
        "#..E#.#",
        "#######"
    ]
    example = [list(row) for row in example]

    result = [
        "#######",
        "#.E.E.#",
        "#.#E..#",
        "#E.##.#",
        "#.E.#.#",
        "#...#.#",
        "#######"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 46
    assert board.board == result
    assert board.sum_remaining_hp == 859
    assert board.outcome == 39514

    example = [
        "#######",
        "#E.G#.#",
        "#.#G..#", 
        "#G.#.G#",
        "#G..#.#",
        "#...E.#",
        "#######"
    ]
    example = [list(row) for row in example]

    result = [
        "#######",
        "#G.G#.#",
        "#.#G..#",
        "#..#..#",
        "#...#G#",
        "#...G.#",
        "#######"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 35
    assert board.board == result
    assert board.sum_remaining_hp == 793
    assert board.outcome == 27755

    example = [
        "#######",
        "#.E...#",
        "#.#..G#",
        "#.###.#",
        "#E#G#G#",
        "#...#G#",
        "#######"
    ]
    example = [list(row) for row in example]

    result = [
        "#######",
        "#.....#",
        "#.#G..#",
        "#.###.#",
        "#.#.#.#",
        "#G.G#G#",
        "#######"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 54
    assert board.board == result
    assert board.sum_remaining_hp == 536
    assert board.outcome == 28944

    example = [
        "#########",
        "#G......#",
        "#.E.#...#",
        "#..##..G#",
        "#...##..#",
        "#...#...#",
        "#.G...G.#",
        "#.....G.#",
        "#########"
    ]
    example = [list(row) for row in example]

    result = [
        "#########",
        "#.G.....#",
        "#G.G#...#",
        "#.G##...#",
        "#...##..#",
        "#.G.#...#",
        "#.......#",
        "#.......#",
        "#########"
    ]
    result = [list(row) for row in result]

    board = Board()
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 20
    assert board.board == result
    assert board.sum_remaining_hp == 937
    assert board.outcome == 18740


if __name__ == "__main__":

    test_all()
    print("all tests passed.")

    board = Board()
    board.read_from_file("input.txt")
    board.play()
    board.print_board()
    print("answer:", board.outcome)
