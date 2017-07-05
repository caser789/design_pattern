def bfs(graph, start, end):
    paths = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in paths:
            paths.append(current)
            if current == end:
                print paths
                return (True, paths)
            if current not in graph:
                continue
        visited = visited + graph[current]
    return (False, paths)


def dfs(graph, start, end):
    paths = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in paths:
            paths.append(current)
            if current == end:
                print paths
                return (True, paths)
            if current not in graph:
                continue
        visited = graph[current] + visited
    return (False, paths)


if __name__ == "__main__":
    graph = {
        "Frankfurt": ["Mannheim", "Wurzburg", "Kassel"],
        "Mannheim": ["Karlsruhe"],
        "Karlsruhe": ["Augsburg"],
        "Augsburg": ["Munchen"],
        "Wurzburg": ["Erfurt", "Nurnberg"],
        "Nurnberg": ["Stuttgart", "Munchen"],
        "Kassel": ["Munchen"],
        "Erfurt": [],
        "Stuttgart": [],
        "Munchen": [],
    }
    bfs_path = bfs(graph, "Frankfurt", "Nurnberg")
    dfs_path = dfs(graph, "Frankfurt", "Nurnberg")
    print "bfs Frankfurt-Nurnberg: {}".format(bfs_path[1] if bfs_path[0] else "Not Found")
    print "dfs Frankfurt-Nurnberg: {}".format(dfs_path[1] if dfs_path[0] else "Not Found")

    bfs_nopath = bfs(graph, "Wurzburg", "Kassel")
    dfs_nopath = dfs(graph, "Wurzburg", "Kassel")
    print "bfs Wurzbug-Kassel: {}".format(bfs_nopath[1] if bfs_nopath[0] else "Not Found")
    print "dfs Wurzbug-Kassel: {}".format(dfs_nopath[1] if dfs_nopath[0] else "Not Found")
