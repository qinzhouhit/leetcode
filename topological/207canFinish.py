'''
keys:
Solutions:
Similar:
T:
S:
'''

# Topological sort O(n)
import collections
class Solution:
    unvisited = 0; visiting = 1; visited = 2
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph_ = collections.defaultdict(list)

        for pair in prerequisites:
            graph_[pair[1]].append(pair[0]) # k: pre, v: course

        status = [0]*numCourses
        for i in range(numCourses):
            if self.dfs(i, status, graph_):
                return False

        return True

    def dfs(self, cur, status, graph_):
        if status[cur] == 1: return True # found a ring
        if status[cur] == 2: return False # not a problem
        status[cur] = 1

        for i in graph_[cur]: # visiting all neighbors
            if self.dfs(i, status, graph_):
                return True # if any ring

        status[cur] = 2 # mark as visited after visiting all neighbors
        return False # no ring found


