"""
--- Part Two ---

Good thing you didn't have to wait, because that would have taken a long time -
much longer than the 3 seconds in the example above.

Impressed by your sub-hour communication capabilities, the Elves are curious:
exactly how many seconds would they have needed to wait for that message to
appear?
"""
from part1 import read_input, find_min, draw_message


if __name__ == "__main__":

    pos, vel = read_input('input.txt')
    t = find_min(pos, vel)
    pos, vel = read_input('input.txt')
    print(f"After {t} seconds:")
    draw_message(t, pos, vel)
