def all_paths(graph, start, end):
    """
    graph: dict of adjacency list {node: [neighbors]}
    start: start node
    end: end node
    """
    result = []

    def dfs(node, path):
        path.append(node)
        if node == end:
            result.append(path.copy())  # store a copy of path
        else:
            for neighbor in graph.get(node, []):
                dfs(neighbor, path)
        path.pop()  # backtrack

    dfs(start, [])
    return result

# ---------- Example Usage ----------
if __name__ == "__main__":
    graph = {
        0: [1, 2],
        1: [3],
        2: [3],
        3: []
    }
    start = 0
    end = 3
    paths = all_paths(graph, start, end)
    print("All Paths from", start, "to", end, ":", paths)
