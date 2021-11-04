"""
Assuming we have a directed graph represented with an adjacency list.

Example:
graph = {'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'E'
"""
from collections import deque


def bfsIterative(graph: dict):
    visited = set()
    queue = deque()
    traversed = []
    for node in graph:
        queue = deque([node])
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                traversed.append(cur)
                for nb in graph[cur]:
                    if nb not in visited:
                        visited.add(nb)
    return traversed
