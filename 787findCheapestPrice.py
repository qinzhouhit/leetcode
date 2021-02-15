'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# >>> BFS
	# T: O(E + NLogN), N here denotes to kn (which can be interpreted as each node n has k states)
	# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/115541/JavaPython-Priority-Queue-Solution
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		g = collections.defaultdict(dict)
        for s, e, price in flights:
            g[s][e] = price
        heap = [(0, src, K + 1)] # cur cost, starting point, remaining stops
        while heap:
            cost, cur_node, residue = heapq.heappop(heap)
            if cur_node == dst:
                return cost
            if residue > 0:
                for nxt in g[cur_node]:
                    heapq.heappush(heap, (cost + g[cur_node][nxt], nxt, residue - 1))
        return -1


	# >>> BFS
	# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/686774/SUGGESTION-FOR-BEGINNERS-BFS-or-DIJKSHTRA-or-DP
	# T: the time taken for extract min and then addition to the heap (or simply, heap replace)
    # would be O(V^2 * logV), V for number of cities and E for number of flights
    # S: O(V) for the adjacent matrix
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
		if src == dst: 
            return 0
        d = collections.defaultdict(list)
        seen = collections.defaultdict(lambda: float('inf'))
        for s, e, price in flights:
            d[s] += [(e, price)]
    
        q = deque([(src, -1, 0)])
        
        while q:
            cur, k, cost = q.popleft()
            if cur == dst or k == K: 
            	continue 
            for nxt, p in d[cur]:
                if cost + p >= seen[nxt]:
                    continue
                else:
                    seen[nxt] = cost+p
                    q.append((nxt, k+1, cost+p))
                
        return seen[dst] if seen[dst] < float('inf') else -1


	




	# >>> dfs
	# https://leetcode.com/problems/cheapest-flights-within-k-stops/discuss/128217/Three-C%2B%2B-solutions-BFS-DFS-and-BF
	def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        g = collections.defaultdict(list)
        for s, e, price in flights:
            g[s].append([e, price])
        
        def find(start, end, residue, cur_cost):
            nonlocal res
            # print (start, cur_cost, dst, residue)
            if start == end:
                # print (start, dst)
                res = cur_cost
                return
            if residue == 0:
                return 
            # seen.add(start)
            for nxt, price in g[start]:
                # if nxt not in seen:
                if cur_cost + price > res: 
                    continue
                find(nxt, end, residue-1, cur_cost+price)

        res = float("inf") 
        # seen = set([src]) # no need for seen since there is no loop
        find(src, dst, K+1, 0)
        return res if res != float("inf") else -1 


    # >>> official dfs                
    def __init__(self):
        self.adj_matrix = None
        self.memo = {}
    
    def findShortest(self, node, stops, dst, n):
            
        # No need to go any further if the destination is reached    
        if node == dst:
            return 0
        
        # Can't go any further if no stops left
        if stops < 0:
            return float("inf")
        
        # If the result of this state is already cached, return it
        if (node, stops) in self.memo:
            return self.memo[(node, stops)]
        
        # Recursive calls over all the neighbors
        ans = float("inf")
        for neighbor in range(n):
            if self.adj_matrix[node][neighbor] > 0:
                ans = min(ans, self.findShortest(neighbor, stops-1, dst, n) + self.adj_matrix[node][neighbor])
        
        # Cache the result
        self.memo[(node, stops)] = ans        
        return ans
    
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        self.adj_matrix = [[0 for _ in range(n)] for _ in range(n)]
        self.memo = {}
        for s, d, w in flights:
            self.adj_matrix[s][d] = w
        
        result = self.findShortest(src, K, dst, n)
        return -1 if result == float("inf") else result