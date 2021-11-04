"""
Topological Sort without cycle detection
"""
from typing import List
from collections import deque


def dfsHelper(graph, source, visited, sortedLst):
    visited.add(source)
    if source in graph:
        for neighbour in graph[source]:
            if neighbour not in visited:
                dfsHelper(graph, neighbour, visited, sortedLst)
    sortedLst.appendleft(source)


def topoSort(graph: dict) -> List[str]:
    visited = set()
    sortedLst = deque()
    for node in graph:
        if node in visited:
            continue
        else:
            dfsHelper(graph, node, visited, sortedLst)
    return list(sortedLst)


graphAcycle = {
    'a': ['b', 'c'],
    'b': ['c', 'd'],
    'c': ['d'],
    'd': []
}
source = 'a'
print(topoSort(graph=graphAcycle))
