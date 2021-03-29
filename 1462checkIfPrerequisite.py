'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# topological sort
	# T: O(P * N), N for topological sort and P for passing all prerequisites.
	# S: O(N^2) for all sets.
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        sortedOrder = []
        if n <= 0:
            return False
        
        inDegree = {i:0 for i in range(n)}
        g = {i:[] for i in range(n)}
        pres = collections.defaultdict(set)
        
        for pre, course in prerequisites:
            inDegree[course] += 1
            g[pre].append(course) # pre -> child
            pres[course].add(pre) # course: list of pres
        
        source = deque()
        for k, v in inDegree.items():
            if v == 0:
                source.append(k)
                
        while source:
            pre = source.popleft()
            sortedOrder.append(pre)
            for course in g[pre]:
                pres[course] |= pres[pre]
                inDegree[course] -= 1
                if inDegree[course] == 0:
                    source.append(course)
        
        res = []
        for pre, course in queries:
            if pre in pres[course]:
                res.append(True)
            else:
                res.append(False)
        return res

    # dfs
    # https://leetcode.com/problems/course-schedule-iv/discuss/660883/Clean-Python-3-topological-sort-and-set-O(P-*-N)/824701s
    def checkIfPrerequisite(self, n: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        d = defaultdict(list)
        for x, y in prerequisites:
            d[x] += y,
        
        @lru_cache(None)
        def dfs(x, y):
            if x == y: return True
            return any(dfs(n, y) for n in d[x])
        
        return [dfs(x, y) for x, y in queries]












