from typing import Dict, Tuple, List
from part1 import Board, Mob


class PowerMob(Mob):

    def __init__(self, mob_type: str, row: int, col: int, power: int) -> None:

        self.type = mob_type
        self.row = row
        self.col = col
        self.hp = 200
        self.power = power
        self.alive = True


class PowerBoard(Board):

    def __init__(self, elf_power: int) -> None:

        super().__init__()
        self.elf_power = elf_power
        self.n_elves = 0

    def get_mobs(self) -> Dict[Tuple[int, int], Mob]:

        for i, r in enumerate(self.board):
            for j, c in enumerate(r):
                if c == 'G':
                    self.mobs[i, j] = Mob('G', i, j)
                if c == 'E':
                    self.mobs[i, j] = PowerMob('E', i, j, power=self.elf_power)
                    self.n_elves += 1

        return self.mobs

    def elves_won_without_death(self) -> bool:

        alive_elves = sum(
            1 for mob in self.mobs.values()
            if mob.alive and mob.type == 'E'
        )
        return not self.are_both_teams_alive() and alive_elves == self.n_elves


def find_lowest_attack_power_for_elves(
    initial_board: List[List[str]],
    n: int = 1000
    ) -> int:

    for power in range(3, 3 + n):
        board = PowerBoard(power)
        board.read_from_array(list(list(row) for row in initial_board))
        board.play()
        if board.elves_won_without_death():
            break
    return power


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
        "#..E..#",
        "#...E.#",
        "#.#.#.#",
        "#...#.#",
        "#.....#",
        "#######"
    ]
    result = [list(row) for row in result]

    t = find_lowest_attack_power_for_elves(example)
    board = PowerBoard(t)
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 29
    assert board.board == result
    assert board.sum_remaining_hp == 172
    assert board.outcome == 4988

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
        "#E.##E#",
        "#.E.#.#",
        "#...#.#",
        "#######"
    ]
    result = [list(row) for row in result]

    t = find_lowest_attack_power_for_elves(example)
    board = PowerBoard(t)
    board.read_from_array(example)
    board.play()
    board.print_board()

    assert board.rounds == 33
    assert board.board == result
    assert board.sum_remaining_hp == 948
    assert board.outcome == 31284


if __name__ == "__main__":

    test_all()
    print("all tests passed.")


    t = find_lowest_attack_power_for_elves(
        [list(line) for line in open("input.txt")]
    )
    board = PowerBoard(t)
    board.read_from_file("input.txt")
    board.play()
    board.print_board()
    print("answer:", board.outcome)
