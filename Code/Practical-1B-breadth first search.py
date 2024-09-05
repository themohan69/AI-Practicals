# Graph representation
graph1 = {
    'A': set(['B', 'C']),
    'B': set(['A', 'D', 'E']),
    'C': set(['A', 'F']),
    'D': set(['B']),
    'E': set(['B', 'F']),
    'F': set(['C', 'E']),
}

# Depth-First Search (DFS)
def dfs(start):
    queue = [start]
    levels = {start: 0}
    visited = set([start])
    while queue:
        node = queue.pop(0)
        neighbours = graph1[node]
        for neighbour in neighbours:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.add(neighbour)
                levels[neighbour] = levels[node] + 1
        print(levels)  # Print graph levels
    return visited

# Example usage of DFS
print(str(dfs('A')))  # Print visited nodes

# Breadth-First Search (BFS) for finding paths
def bfs_paths(graph, start, goal):
    queue = [(start, [start])]
    while queue:
        (vertex, path) = queue.pop(0)
        for next in graph[vertex] - set(path):
            if next == goal:
                yield path + [next]
            else:
                queue.append((next, path + [next]))

# Example usage of BFS to find paths
result = list(bfs_paths(graph1, 'A', 'F'))
print(result)  # Output: [['A', 'C', 'F'], ['A', 'B', 'E', 'F']]

# Finding the shortest path using BFS
def shortest_path(graph, start, goal):
    try:
        return next(bfs_paths(graph, start, goal))
    except StopIteration:
        return None

# Example usage of finding the shortest path
result1 = shortest_path(graph1, 'A', 'F')
print(result1)  # Output: ['A', 'C', 'F']
