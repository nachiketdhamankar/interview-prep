def topoWithCyce(graph: dict):
    VISITING, DONE_VISITING = 0, 1

    def dfs(node: str, graph: dict, lst: list, vertexState: dict):
        if node in vertexState and vertexState[node] == DONE_VISITING: return
        vertexState[node] = VISITING
        if node in graph:
            for nb in graph[node]:
                if nb in vertexState and vertexState[nb] == VISITING:
                    # Cycle Detected
                    lst.appendleft(float('inf'))
                    return
                dfs(nb, graph, lst, vertexState)
        vertexState[node] = DONE_VISITING
        lst.appendleft(node)

    lst = deque()
    vertexState = defaultdict(int)
    for node in graph.keys():
        dfs(node, graph, lst, vertexState)
    return list(lst)
