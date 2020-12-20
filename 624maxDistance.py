'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# just consider 1st and last element in each list
	# T: O(n), n as length of arrrays
	# S: O(1)
    def maxDistance(self, arrays: List[List[int]]) -> int:
    	res = 0
        min_ = arrays[0][0]
        max_ = arrays[0][-1]
        for i in range(1, len(arrays)):
            cur = arrays[i] # cur array
            res = max(res, max(abs(cur[-1] - min_), abs(max_ - cur[0])))
            min_ = min(min_, cur[0])
            max_ = max(max_, cur[-1])
        return res
            
        