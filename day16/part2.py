"""
--- Part Two ---

Using the samples you collected, work out the number of each opcode and execute 
the test program (the second section of your puzzle input).

What value is contained in register 0 after executing the test program?
"""
from collections import defaultdict
from typing import List, Dict, Callable
from part1 import OPERATORS, read_input


def match_opcode(
    instr_list: List[List[int]],
    before_list: List[List[int]],
    after_list: List[List[int]]
    ) -> Dict[int, Callable]:

    candidates: Dict[int, List[int]] = defaultdict(list)
    
    for instr, before, after in zip(instr_list, before_list, after_list):
        for i in range(len(OPERATORS)):
            operator = OPERATORS[i]
            if operator(list(before), instr) == after:
                candidates[instr[0]].append(i)

    result: Dict[int, Callable] = dict()

    while candidates:
        for i in list(candidates.keys()):
            if len(set(candidates[i])) == 1:
                idx = candidates[i][0]
                result[i] = OPERATORS[idx]
                for j in list(candidates.keys()):
                    candidates[j] = [x for x in candidates[j] if x != idx]
                    if not candidates[j]:
                        del candidates[j]

    return result


def read_input_second_section(filename:str) -> List[List[int]]:

    with open(filename) as f:
        lines = f.readlines()

    i = 0
    while i < len(lines) and lines[i].startswith("Before:"):
        i += 4

    result = []
    for line in lines[i:]:
        splitted = line.strip().split()
        if splitted:
            result.append([int(x) for x in splitted])

    return result

if __name__ == "__main__":

    instr_list, before_list, after_list = read_input("input.txt")
    opcodes = match_opcode(instr_list, before_list, after_list)
    register = after_list[-1]
    instructions = read_input_second_section("input.txt")
    for instr in instructions:
        operator = opcodes[instr[0]]
        register = operator(list(register), instr)
    
    print("answer:", register[0])
