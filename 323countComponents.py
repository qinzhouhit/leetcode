"""
keys:
Solutions:
Similar:
T:
S:
""" 
from typing import List


class Solution:
	"""
	DSU here uses union by rank, otherwise the time complexity 
	is O(log(N)) for each merge.
	Only with both Union by rank and path compression, we have 
	~O(1) time for each union/find operation, so it gives O(V + E) time in total.
	"""
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        def find(x):  # find the root of x
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
            
        def union(xy):
            x, y = map(find, xy)
            if rank[x] < rank[y]:
                parent[x] = y  # make the low rank one as child
            else:
                parent[y] = x
                if rank[x] == rank[y]:
                    rank[x] += 1
        
        parent, rank = range(n), [0] * n  # parent: ids of the nodes
        map(union, edges)  # fancy way...
        return len({find(x) for x in parent})


    # dfs
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        graph = collections.defaultdict(list)
        for edge in edges:
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])

        ans = 0
        visited = set()
        for vertex in range(n):
            if not vertex in visited:
                self.dfs(graph, vertex, visited)
                ans += 1
        return ans
        
    
    def dfs(self, graph, vertex, visited):
        if vertex in visited:
            return
        visited.add(vertex)
        for nei in graph[vertex]:
            self.dfs(graph, nei, visited)






