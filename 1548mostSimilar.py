""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        """
        tp: targetPath
        Calculate the minimum edit distance without worrying about the path:
        	dp[i][v] means the minimum edit distance for tp[:i+1] ending with city v.
		Transition function:
			dp[i][v] = min(dp[i-1][u] + edit_cost(v)) for all edges (u, v)
			, where edit_cost(v) at index i is names[v] != tp[i].
		The minimum edit distance will be min(dp[-1][v] for v in range(n)).

		To construct the optimal path, we can maintain a 2D array (or dict) 
		prev when populate dp. Suppose prev[i][v] is u. Then (u, v) is the 
		ending edge of the optimal path at dp[i][v]. u is the previous city 
		before the ending city (v in the example)
		T: O(N^2 * len(tp))
		S: O(N * len(tp))
        """
        # construct graph
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)

        m = len(targetPath)  # m as #targetCities
        dp = [[m] * n for _ in range(m)]  # n as #totalCities
        prev = [[0] * n for _ in range(m)]  

        # update dp
        for v in range(n):  # ending city as v
        	dp[0][v] = (names[v] != targetPath[0])  # dp[0][x], tp[:1]: only the 1st city
        for i in range(1, m):  # process i-th in target path
        	for v in range(n):  
        		for u in graph[v]:  # prev cities connected to city v, update dp[i][v]
        		# based on dp[i-1][u]
        			if dp[i-1][u] < dp[i][v]:  # choose the min one
        				dp[i][v] = dp[i-1][u] 
        				prev[i][v] = u  # recording the previous city on optimal path
        		dp[i][v] += (names[v] != targetPath[i])  # edit_cost(v)

        # re-construct path
        path, min_dist = [0], m
        for v in range(n):
        	if dp[-1][v] < min_dist:
        		min_dist = dp[-1][v]  # dp[-1][v] means ending in v, full-path
        		path[0] = v  # update the last city in the path
        for i in range(m - 1, 0, -1):
        	u = prev[i][path[-1]]
        	path.append(u)
        return path[::-1]






        
