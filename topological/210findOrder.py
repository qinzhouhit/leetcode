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



# educative.io, topological sort
def findOrder2(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
    sortedOrder = []
    if numCourses <= 0:
        return False

    inDegree = {i: 0 for i in range(numCourses)}
    graph = {i: [] for i in range(numCourses)}

    for pair in prerequisites:
        # Must take course pair[1] before pair[0] !!! Different from 207
        parent, child = pair[1], pair[0]
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

    # return the sorted result instead of False/True
    if len(sortedOrder) != numCourses:
        return []
    return sortedOrder





import collections
class Solution:
    # https://leetcode.com/problems/course-schedule-ii/discuss/59455/Fast-python-DFS-solution-with-inline-explanation
    # O(N) for S and T, N as number of courses
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # use DFS to parse the course structure
        self.graph = collections.defaultdict(list) # a graph for all courses
        self.res = [] # start from empty
        for pair in prerequisites:
            self.graph[pair[0]].append(pair[1]) 
        self.visited = [0 for _ in range(numCourses)] # DAG detection 
        for x in range(numCourses):
            if not self.dfs(x):
                return []
             # continue to search the whole graph
        return self.res
    
    def dfs(self, node):
        if self.visited[node] == -1: # cycle detected
            return False
        if self.visited[node] == 1:
            return True # has been finished, and been added to self.res
        self.visited[node] = -1 # mark as visited
        for nei in self.graph[node]:
            if not self.dfs(nei):
                return False
        self.visited[node] = 1 # mark as finished
        # add to solution as the course depenedent on previous ones
        self.res.append(node) 
        return True
    
    
    
    # iterative dfs; indegree, O(V+E) for S and T
    def findOrder1(self, numCourses, prerequisites):
        # dic[i] is the indegree of the node i,  computing will be faster
        dic  = [0 for i in range(numCourses)];
        neigh = collections.defaultdict(set)
        for i, j in prerequisites:
            dic[i] += 1;
            neigh[j].add(i)
        stack  = [i for i in range(numCourses) if dic[i] == 0];
        res = []
        while stack:
            node = stack.pop()
            res.append(node)
            for i in neigh[node]:
                dic[i] -= 1
                if dic[i] == 0:
                    stack.append(i)
        # for i in range(numCourses):
        #     if dic[i] > 0:
        #         return []
        if sum(dic) > 0: return []
        return res


