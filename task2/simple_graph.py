from collections import deque


class Graph:
    def __init__(self, x):
        self.array = {}
        self.ribs = x
        for pair in x:
            if pair[0] not in self.array:
                self.array[pair[0]] = []
            self.array[pair[0]].append(pair[1])
            if pair[1] not in self.array:
                self.array[pair[1]] = []
            self.array[pair[1]].append(pair[0])

    def dfs(self, start):
        visited = []
        stack = [start]
        while stack:
            node = stack.pop()
            if node not in visited:
                visited.append(node)
                stack.extend(set(self.array[node]) - set(visited))
        return visited

    def bfs(self, start):
        visited = []
        list_of_node = deque([start])
        while list_of_node:
            node = list_of_node.pop()
            if node not in visited:
                visited.append(node)
                list_of_node.extendleft(set(self.array[node]) - set(visited))
        return visited

