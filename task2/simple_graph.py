from collections import deque


def make_graph(ribs):
    graph = {}
    for pair in ribs:
        if pair[0] not in graph:
            graph[pair[0]] = []
        graph[pair[0]].append(pair[1])
        if pair[1] not in graph:
            graph[pair[1]] = []
        graph[pair[1]].append(pair[0])
    return graph


def dfs(graph, start):
    visited = []
    stack = [start]
    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(set(graph[node]) - set(visited))
    return visited


def bfs(graph, start):
    visited = []
    list_of_node = deque([start])
    while list_of_node:
        node = list_of_node.pop()
        if node not in visited:
            visited.append(node)
            list_of_node.extendleft(set(graph[node]) - set(visited))
    return visited


