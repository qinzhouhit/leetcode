'''
keys: topological sort
Solutions:
Similar:
T: O(V+E) ~ O(V^2), but V^2 edges must result in multiple loops
S: O(V+E) ~ O(V^2)
'''
from typing import List

# the presence of a cycle in the graph shows us that a proper
# ordering of prerequisites is not possible at all

import collections
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph_ = collections.defaultdict(list)

        for pair in prerequisites:
            graph_[pair[1]].append(pair[0]) # k: pre, v: course, k -> v

        status = [0]*numCourses
        res = []
        for i in range(numCourses):
            if self.dfs(i, status, graph_, res):
                return []
        return res[::-1]

    def dfs(self, cur, status, graph_, res):
        if status[cur] == 1: return True # found a ring
        if status[cur] == 2: return False # not a problem
        status[cur] = 1

        for i in graph_[cur]: # visiting all neighbors
            if self.dfs(i, status, graph_, res):
                return True # if any ring

        status[cur] = 2 # mark as visited after visiting all neighbors
        res.append(cur)
        return False # no ring found


