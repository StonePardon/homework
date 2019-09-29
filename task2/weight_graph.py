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

    def dfs_paths(self, start, last):
        stack = [(start, [start])]  # (node, path)
        while stack:
            (node, path) = stack.pop()
            for next in set(self.array[node]) - set(path):
                if next == last:
                    yield path + [next]
                else:
                    stack.append((next, path + [next]))

    def short_path(self, start, last):
        all_path = list(self.dfs_paths(start, last))
        weight = []
        ribss = []
        for pair in self.ribs:
            ribss.append([pair[1], pair[0]])
            ribss.append([pair[0], pair[1]])
            weight.append(pair[2])
            weight.append(pair[2])
        min_p = []
        path_index = int(0)
        for path in all_path:
            i = 0
            min_p.append(0)
            while i < len(path) - 1:
                index = ribss.index([path[i], path[i+1]])
                min_p[path_index] += weight[index]
                i += 1
            path_index += 1
        ans = min_p[0]
        min_path = all_path[0]
        for i in range(len(min_p)):
            if ans > min_p[i]:
                ans = min_p[i]
                min_path = all_path[i]
        return min_path


x = [[0, 3, 1], [1, 3, 2], [2, 3, 3], [4, 3, 4], [5, 4, 5], [2, 5, 5]]
gr = Graph(x)
print(gr.array)
print(gr.bfs(0))
print(gr.dfs(0))
print(gr.short_path(0, 5))
