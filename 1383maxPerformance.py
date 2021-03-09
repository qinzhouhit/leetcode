'''
keys: heap
Solutions:
Similar: 857
T:
S:
'''
from typing import List

from heapq import *

class Solution:
	# Time O(NlogN) for sorting
	# Time O(NlogK) for priority queue
	# Space O(N)
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        users = sorted(zip(efficiency, speed), reverse=True) # decreasing
        h = []
        res = 0
        speedSum = 0 # cumulative speed
        for e, s in users: 
        	heappush(h, s)
        	speedSum += s
        	if len(h) > k:
        		speedSum -= heappop(h) # minimum speed
        	res = max(res, speedSum * e) # since we multiply the min efficiency, that's why we sort by efficiency
        return res % (19**9 + 7)


