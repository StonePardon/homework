from collections import deque


class Graph:
    def __init__(self, x):
        self.array = {}
        self.ribs = x
        self.point = []
        for pair in x:
            if pair[0] not in self.array:
                self.array[pair[0]] = []
            self.array[pair[0]].append(pair[1])
            if pair[1] not in self.array:
                self.array[pair[1]] = []
            self.array[pair[1]].append(pair[0])
            if pair[0] not in self.point:
                self.point.append(pair[0])
            if pair[1] not in self.point:
                self.point.append(pair[1])

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
        if all_path == []:
            return -1
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
        for i in range(len(min_p)):
            if ans > min_p[i]:
                ans = min_p[i]
        return ans


def new_time(time, num, point):
    my_list = Graph(time)
    flag = 0
    for i in my_list.point:
        if i == point:
            flag = 1
    if flag == 0:
        return -1
    ans = 0
    for i in range(N):
        tmp = my_list.short_path(point, i)
        if tmp > 0:
            ans = ans + tmp
    return ans


times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
x = 2
N = 4

print(new_time(times, N, x))

