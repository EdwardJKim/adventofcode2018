"""
--- Part Two ---

In order to determine the timing window for your underflow exploit, you also
need an upper bound:

What is the lowest non-negative integer value for register 0 that causes the
program to halt after executing the most instructions? (The program must
actually halt; running forever does not count as halting.)
"""
from collections import defaultdict
from opcodes import OPERATORS
from typing import List


def run(program: List[str]) -> int:

    ip = int(program[0].split()[1])
    
    instructions = program[1:]
    register = [0, 0, 0, 0, 0, 0]

    seen: List[int] = []
    count = 0

    while True:
        op, *tail = instructions[register[ip]].split()
        instr = [0] + [int(x) for x in tail]
        f = OPERATORS[op]

        if register[ip] == 17:
            register[3] //= 256
            register[ip] = 8
            continue

        if register[ip] == 28:
            if register[4] in seen:
                return seen[-1]
            seen.append(register[4])
            print(register[4])

        register = f(register, instr)
        if register[ip] + 1 >= len(instructions):
            break
        register[ip] += 1
        count += 1

    return -1


if __name__ == "__main__":

    answer = run(open("input.txt").readlines())
    print("answer:", answer)
