def ford_fulkerson(graph, source, sink):
    n = len(graph)
    parent = [-1]*n  # To store augmenting path

    # DFS to find augmenting path
    def dfs(u, visited):
        visited[u] = True
        if u == sink:
            return True
        for v, cap in enumerate(graph[u]):
            if not visited[v] and cap > 0:
                parent[v] = u
                if dfs(v, visited):
                    return True
        return False

    max_flow = 0
    while True:
        visited = [False]*n
        if not dfs(source, visited):
            break  # No more augmenting paths
        # Find minimum capacity (bottleneck) along the path
        path_flow = float('inf')
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        # Add path flow to max_flow
        max_flow += path_flow
        # Update capacities in residual graph
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = u
    return max_flow

# ---------- Example Usage ----------
if __name__ == "__main__":
    # Graph adjacency matrix
    graph = [
        [0, 16, 13, 0, 0, 0],
        [0, 0, 10, 12, 0, 0],
        [0, 4, 0, 0, 14, 0],
        [0, 0, 9, 0, 0, 20],
        [0, 0, 0, 7, 0, 4],
        [0, 0, 0, 0, 0, 0]
    ]
    source = 0
    sink = 5
    print("Maximum Flow:", ford_fulkerson(graph, source, sink))
