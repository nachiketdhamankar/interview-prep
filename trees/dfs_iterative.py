"""
Assuming we have a directed graph represented with an adjacency list.

Example:
graph = {'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'E'
"""


def dfsIterative(graph: dict):
    visited = set()
    traversed = []
    for node in graph.keys():
        stack = [node]
        while stack:
            cur = stack.pop()
            if cur not in visited:
                traversed.append(cur)
                visited.add(cur)
                for nb in graph[cur]:
                    stack.append(nb)
    return traversed
