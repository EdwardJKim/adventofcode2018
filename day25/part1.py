from collections import deque, defaultdict
from typing import List, Tuple, Set, Dict, Deque


def distance(a, b):

    return sum(abs(ax - bx) for ax, bx in zip(a, b))


def get_constellations(
    points: List[Tuple[int, ...]]
    ) -> List[Set[Tuple[int, ...]]]:

    n = len(points)
    graph: Dict[Tuple[int, ...], Set[Tuple[int, ...]]] = defaultdict(set)
    
    for i in range(n):
        for j in range(n):
            if i == j or distance(points[i], points[j]) > 3:
                continue
            graph[points[i]].add(points[j])
    
    
    constellations = []
    
    q: Deque[Tuple[int, ...]] = deque()
    visited: Set[Tuple[int, ...]] = set()
    remaining = set(points)
    constellation: Set[Tuple[int, ...]] = set()
    
    while q or remaining:
    
        if q:
            point = q.popleft()
            if point in remaining:
                remaining.remove(point)
        else:
            if constellation:
                constellations.append(constellation)
            point = remaining.pop()
            constellation = set([point])
    
        if point in visited:
            continue
        visited.add(point)
    
        for neighbor in graph[point]:
            q.append(neighbor)
    
    if constellation:
        constellations.append(constellation)

    return constellations


def test_get_constellations():

    example = [
        " 0,0,0,0",
        " 3,0,0,0",
        " 0,3,0,0",
        " 0,0,3,0",
        " 0,0,0,3",
        " 0,0,0,6",
        " 9,0,0,0",
        "12,0,0,0"
    ]
    points = [tuple(map(int, line.split(','))) for line in example]
    assert len(get_constellations(points)) == 2
    
    example = [
        "-1,2,2,0",
        "0,0,2,-2",
        "0,0,0,-2",
        "-1,2,0,0",
        "-2,-2,-2,2",
        "3,0,2,-1",
        "-1,3,2,2",
        "-1,0,-1,0",
        "0,2,1,-2",
        "3,0,0,0"
    ]
    points = [tuple(map(int, line.split(','))) for line in example]
    assert len(get_constellations(points)) == 4
    
    example = [
        "1,-1,0,1",
        "2,0,-1,0",
        "3,2,-1,0",
        "0,0,3,1",
        "0,0,-1,-1",
        "2,3,-2,0",
        "-2,2,0,0",
        "2,-2,0,-1",
        "1,-1,0,-1",
        "3,2,0,2"
    ]
    points = [tuple(map(int, line.split(','))) for line in example]
    assert len(get_constellations(points)) == 3
    
    example = [
        "1,-1,-1,-2",
        "-2,-2,0,1",
        "0,2,1,3",
        "-2,3,-2,1",
        "0,2,3,-2",
        "-1,-1,1,-2",
        "0,-2,-1,0",
        "-2,2,3,-1",
        "1,2,2,0",
        "-1,-2,0,-2"
    ]
    points = [tuple(map(int, line.split(','))) for line in example]
    assert len(get_constellations(points)) == 8


if __name__ == "__main__":

    test_get_constellations()
    print("all tests passed.")

    points = [
        tuple(map(int, line.strip().split(',')))
        for line in open("input.txt")
    ]
    answer = len(get_constellations(points))
    print("answer:", answer)
