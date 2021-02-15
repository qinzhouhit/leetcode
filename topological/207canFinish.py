'''
keys:
Solutions:
Similar:
T:
S:
'''

# educative.op version
# detect if there is any cycle
from collections import deque
# S and T: O(V+E)
def canFinish(,self numCourses: int, prerequisites: List[List[int]]) -> bool:
    sortedOrder = []
    if numCourses <= 0:
        return False
    # dont use defaultdict to define, will miss nodesa
    inDegree = {i: 0 for i in range(numCourses)}
    graph = {i: [] for i in range(numCourses)}

    for pair in prerequisites:
        parent, child = pair[0], pair[1]
        inDegree[child] += 1
        graph[parent].append(child)

    sources = deque()
    for k, v in inDegree.items():
        if v == 0:
            sources.append(k)

    while sources:
        vertex = sources.popleft()
        sortedOrder.append(vertex)
        for child in graph[vertex]:
            inDegree[child] -= 1
            if inDegree[child] == 0:
                sources.append(child)
    if len(sortedOrder) != numCourses:
        return False
    return True


# https://leetcode.com/problems/course-schedule/discuss/58586/Python-20-lines-DFS-solution-sharing-with-explanation
# dfs solution
# O(∣E∣+∣V∣^2) where |E| is the number of dependencies, |V| is the number 
# of courses and dd is the maximum length of acyclic paths in the graph.
'''
if node v has not been visited, then mark it as 0.
if node v is being visited, then mark it as -1. If we find a vertex marked as -1 in DFS, then their is a ring.
if node v has been visited, then mark it as 1. If a vertex was marked as 1, then no ring contains v or its successors.
'''
def canFinish1(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
    graph = [[] for _ in range(numCourses)]
    visited = [0] * numCourses
    for parent, child in prerequisites:
        graph[parent] = child

    def dfs(vertex):
        if visited[vertex] == -1: # a being visited node -> a cycle
            return False # cycle found
        if visited[vertex] == 1: # if already visited
            return True
        visited[vertex] = -1 # being visited
        for child in graph[vertex]:
            if not dfs(child):
                return False
        visited[vertex] = 1 # mark it as done visited
        return True

    for vertex in range(numCourses):
        if not dfs(vertex):
            return False
    return True



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



