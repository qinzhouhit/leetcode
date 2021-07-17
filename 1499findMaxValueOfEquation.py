""" 
keys: 
Solutions:
Similar:
T:
S:
"""



"""
Because xi < xj,
yi + yj + |xi - xj| = (yi - xi) + (yj + xj)

So for each pair of (xj, yj),
we have xj + yj, and we only need to find out the maximum yi - xi.
To find out the maximum element in a sliding window,
we can use priority queue or stack.
"""


class Solution:
	# T: O(NlogN)
	# S: O(N)
    def findMaxValueOfEquation(self, points: List[List[int]], k: int) -> int:
        q = []
        res = float("-inf")
        for x, y in points:
        	while q and q[0][1] < x - k:  # not(xj - xi >= -k) -> not(xj >= xi - k) -> xj < xi - k
        		heapq.heappop(q)
        	if q:  # pop the minimal one of x-y, i.e., max y-x
        		res = max(res, -q[0][0] + x + y)
        	heap.heappush(q, (x - y, x))  # maximize yi - xi, i.e., minimize xi - yi

