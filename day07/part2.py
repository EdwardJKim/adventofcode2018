"""
--- Part Two ---

As you're about to begin construction, four of the Elves offer to help. "The
sun will set soon; it'll go faster if we work together." Now, you need to
account for multiple people working on steps simultaneously. If multiple steps
are available, workers should still begin them in alphabetical order.

Each step takes 60 seconds plus an amount corresponding to its letter: A=1,
B=2, C=3, and so on. So, step A takes 60+1=61 seconds, while step Z takes
60+26=86 seconds. No time is required between steps.

To simplify things for the example, however, suppose you only have help from
one Elf (a total of two workers) and that each step takes 60 fewer seconds (so
that step A takes 1 second and step Z takes 26 seconds). Then, using the same
instructions as above, this is how each second would be spent:

Second   Worker 1   Worker 2   Done
   0        C          .        
   1        C          .        
   2        C          .        
   3        A          F       C
   4        B          F       CA
   5        B          F       CA
   6        D          F       CAB
   7        D          F       CAB
   8        D          F       CAB
   9        D          .       CABF
  10        E          .       CABFD
  11        E          .       CABFD
  12        E          .       CABFD
  13        E          .       CABFD
  14        E          .       CABFD
  15        .          .       CABFDE

Each row represents one second of time. The Second column identifies how many
seconds have passed as of the beginning of that second. Each worker column
shows the step that worker is currently doing (or . if they are idle). The
Done column shows completed steps.

Note that the order of the steps has changed; this is because steps now take
time to finish and multiple workers can begin multiple steps simultaneously.

In this example, it would take 15 seconds for two workers to complete these
steps.

With 5 workers and the 60+ second step durations described above, how long will
it take to complete all of the steps?
"""
import heapq
from typing import Dict, Set
from part1 import read_input, find_available, remove_dependency


def process(
    dependencies: Dict[str, Set[str]],
    workers: int = 5,
    duration: int = 60
    ) -> int:

    available_jobs = find_available(dependencies)
    available_workers = list(range(workers))

    heap = []
    processing = set()
    processed = set()
    t = 0 

    while available_jobs or heap:

        if available_jobs and available_workers:
            job = heapq.heappop(available_jobs)
            end_time = t + duration + 1 + ord(job) - ord('A')
            worker = available_workers.pop()
            heapq.heappush(heap, (end_time, job, worker))
            processing.add(job)
            continue

        t, completed_job, completed_worker = heapq.heappop(heap)
        processed.add(completed_job)
        remove_dependency(completed_job, dependencies)
        available_workers.append(completed_worker)
        available_jobs = find_available(dependencies)
        available_jobs = [x for x in available_jobs if x not in processing]

    remaining_jobs = [x for x in dependencies if x not in processed]
    for job in remaining_jobs:
        t += duration + 1 + ord(job) - ord('A')

    return t


def test_process():

    deps = read_input("test.txt")
    assert process(deps, workers=2, duration=0) == 15


if __name__ == "__main__":

    test_process()
    print("all tests passed.")

    answer = process(read_input("input.txt"))
    print("answer:", answer)
