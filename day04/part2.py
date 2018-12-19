"""
--- Part Two ---

Strategy 2: Of all guards, which guard is most frequently asleep on the same
minute?

In the example above, Guard #99 spent minute 45 asleep more than any other
guard or minute - three times in total. (In all other cases, any guard spent
any minute asleep at most twice.)

What is the ID of the guard you chose multiplied by the minute you chose? (In
the above example, the answer would be 99 * 45 = 4455.)
"""
from typing import Dict, List, Tuple
from part1 import read_input, process


def find_times_most_asleep(records: Dict[int, List[int]]) -> Tuple[int, int]:

    times_asleep = [
        (guard, max(minutes)) for guard, minutes in records.items()
    ]
    times_asleep.sort(key=lambda x: -x[1])
    return times_asleep[0]


def test_times_find_most_asleep():

    records = process(read_input("test.txt"))
    guard, times = find_times_most_asleep(records)
    assert guard == 99
    assert times == 3
    assert records[guard].index(times) == 45


if __name__ == "__main__":

    test_times_find_most_asleep()
    print("all tests passed.")

    records = process(read_input("input.txt"))
    guard, times = find_times_most_asleep(records)
    print("answer:", guard * records[guard].index(times))
