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
        
