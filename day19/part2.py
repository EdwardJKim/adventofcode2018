"""
--- Part Two ---

A new background process immediately spins up in its place. It appears
identical, but on closer inspection, you notice that this time, register 0
started with the value 1.

What value is left in register 0 when this new background process halts?
"""
from opcodes import OPERATORS
from typing import List


def run(program: List[str]) -> List[int]:

    ip = int(program[0].split()[1])
    
    instructions = program[1:]
    register = [1, 0, 0, 0, 0, 0]

    while True:

        op, *tail = instructions[register[ip]].split()
        instr = [0] + [int(x) for x in tail]
        f = OPERATORS[op]

        if register[ip] == 2 and register[4] != 0:
            if register[1] % register[4] == 0:
                register[0] += register[4]
                print(register)
            register[2] = register[1]
            register[3] = 1
            register[ip] = 12
            continue

        register = f(register, instr)

        if register[ip] + 1 >= len(instructions):
            break

        register[ip] += 1

    return register


if __name__ == "__main__":

    answer = run(open("input.txt").readlines())
    print("answer:", answer[0])
