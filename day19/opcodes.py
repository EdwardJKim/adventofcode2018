from functools import partial
import operator
from typing import List, Callable, Tuple


def op_register(op: Callable, reg: List[int], instr: List[int]) -> List[int]:

    reg_a, reg_b = reg[instr[1]], reg[instr[2]]
    reg[instr[3]] = op(reg_a, reg_b)

    return reg


def op_immediate(op: Callable, reg: List[int], instr: List[int]) -> List[int]:

    reg_a, val_b = reg[instr[1]], instr[2]
    reg[instr[3]] = op(reg_a, val_b)

    return reg


ADDR = partial(op_register, operator.add)
ADDI = partial(op_immediate, operator.add)
MULR = partial(op_register, operator.mul)
MULI = partial(op_immediate, operator.mul)
BANR = partial(op_register, operator.and_)
BANI = partial(op_immediate, operator.and_)
BORR = partial(op_register, operator.or_)
BORI = partial(op_immediate, operator.or_)


def setr(reg: List[int], instr: List[int]) -> List[int]:

    reg_a = reg[instr[1]]
    reg[instr[3]] = reg_a

    return reg


def seti(reg: List[int], instr: List[int]) -> List[int]:

    val_a = instr[1]
    reg[instr[3]] = val_a

    return reg


SETR = setr
SETI = seti


def cmp_immediate_register(
    cmp: Callable,
    reg: List[int],
    instr: List[int]
    ) -> List[int]:

    val_a, reg_b = instr[1], reg[instr[2]]
    reg[instr[3]] = 1 if cmp(val_a, reg_b) else 0

    return reg


def cmp_register_immediate(
    cmp: Callable,
    reg: List[int],
    instr: List[int]
    ) -> List[int]:

    reg_a, val_b = reg[instr[1]], instr[2]
    reg[instr[3]] = 1 if cmp(reg_a, val_b) else 0

    return reg


def cmp_register_register(
    cmp: Callable,
    reg: List[int],
    instr: List[int]
    ) -> List[int]:

    reg_a, reg_b = reg[instr[1]], reg[instr[2]]
    reg[instr[3]] = 1 if cmp(reg_a, reg_b) else 0

    return reg


GTIR = partial(cmp_immediate_register, operator.gt)
GTRI = partial(cmp_register_immediate, operator.gt)
GTRR = partial(cmp_register_register, operator.gt)
EQIR = partial(cmp_immediate_register, operator.eq)
EQRI = partial(cmp_register_immediate, operator.eq)
EQRR = partial(cmp_register_register, operator.eq)


OPERATORS = {
    "addr": ADDR, "addi": ADDI, "mulr": MULR, "muli": MULI,
    "banr": BANR, "bani": BANI, "borr": BORR, "bori": BORI,
    "setr": SETR, "seti": SETI, "gtir": GTIR, "gtri": GTRI,
    "gtrr": GTRR, "eqir": EQIR, "eqri": EQRI, "eqrr": EQRR
}
