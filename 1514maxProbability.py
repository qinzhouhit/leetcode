'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/path-with-maximum-probability/discuss/731767/JavaPython-3-2-codes%3A-Bellman-Ford-and-Dijkstra's-algorithm-w-brief-explanation-and-analysis.
	# T: O(n + Elogn)
	# S: O(n + E), E = len(edges)
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        p, g = [0.0] * n, defaultdict(list) # probability for vertices, graph
        for index, (a, b) in enumerate(edges): # index is for accessing succProb
            g[a].append((b, index))
            g[b].append((a, index))
        p[start] = 1.0
        heap = [(-p[start], start)] # maxheap, cumulative prob
        while heap:
            prob, cur = heapq.heappop(heap)
            if cur == end:
                return -prob
            for neighbor, index in g.get(cur, []):
                if -prob * succProb[index] > p[neighbor]:
                    p[neighbor] = -prob * succProb[index]
                    heapq.heappush(heap, (-p[neighbor], neighbor))
        return 0.0