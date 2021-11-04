"""
Assuming we have a directed graph represented with an adjacency list.

Example:
graph = {'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'E'
"""


def dfsRecursive(graph: dict):
    def dfsHelper(graph: dict, source: str, visited: set, traversed: list):
        if source not in visited:
            traversed.append(source)
            visited.add(source)
            for nb in graph[source]:
                if nb not in visited:
                    dfsHelper(graph, nb, visited, traversed)

    visited = set()
    traversed = []
    for node in graph.keys():
        dfsHelper(graph, node, visited, traversed)
    return traversed
