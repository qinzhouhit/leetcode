'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

import functools

class Solution:
    '''
    As a result, for a graph with N nodes, at maximum, there could be 
    sum_{i=0}^{N-2}{2^i} = 2^{N-1} - 1 number of paths between the 
    starting and the ending nodes.
    
    T: O(N*2^N), 2^(N-1) - 1 possible path in the graph
    for each path, could be N-2 intermediate nodes, O(N) to build the path
    S: O(N*2^N), 2^(N-1) - 1 paths times the nodes in the path, i.e., N
    '''
    def allPathsSourceTarget1(self, graph: List[List[int]]) -> List[List[int]]:
        n = len(graph)
        target = n - 1
        res = []
        
        def backtrack(cur, path):
            if cur == target:
                res.append(list(path))
                return
            for nxt in graph[cur]:
                path.append(nxt)
                backtrack(nxt, path)
                path.pop()
        path = [0]
        backtrack(0, path)
        return res

    # self-made
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        def helper(cur, path):
            if cur == target:
                res.append(path[:])
            for neighbor in graph[cur]:
                helper(neighbor, path+[neighbor])

        path = [0]
        res = []
        target = len(graph) - 1 # value of target node
        helper(0, path)
        return res


    # top-down memo
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1

        # apply the memoization
        @functools.lru_cache(maxsize=None)
        def helper(currNode):
            if currNode == target:
                return [[target]]

            results = []
            for nextNode in graph[currNode]:
                for path in helper(nextNode):
                    results.append([currNode] + path)

            return results

        return helper(0)


obj = Solution()
print (obj.allPathsSourceTarget([[1,2],[3],[3],[]]))
