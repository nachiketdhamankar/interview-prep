"""
Assuming we have a directed graph represented with an adjacency list.

Example:
graph = {'A': ['B', 'C'],
 'B': ['D', 'E'],
 'C': ['F'],
 'E'
"""


def bfsRecursive(graph: dict):
    def bfsHelper(graph: dict, visited: set, traversed: list, queue: deque):
        if not queue:
            return
        cur = queue.popleft()
        if cur not in visited:
            traversed.append(cur)
            visited.add(cur)
            for nb in graph[cur]:
                if nb not in visited:
                    queue.append(nb)
                    visited.add(nb)
                    traversed.append(nb)
        bfsHelper(graph, visited, traversed, queue)
        return

    traversed = []
    visited = set()
    for node in graph:
        queue = deque([node])
        bfsHelper(graph, visited, traversed, queue)
    return traversed
