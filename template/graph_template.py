def traverse(graph, start, end, action):
    paths = []
    visited = [start]
    while visited:
        current = visited.pop(0)
        if current not in paths:
            paths.append(current)
            if current == end:
                return (True, paths)
            if current not in graph:
                continue
        visited = action(visited, graph[current])
    return False, paths


def extend_bfs_path(visited, current):
    return visited + current


def extend_dfs_path(visited, current):
    return current + visited
