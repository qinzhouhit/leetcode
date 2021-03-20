'''
keys:
Solutions:
Similar: 209
T:
S:
'''
from typing import List
import collections

class Solution:
	# O(N) for S and T
    def shortestSubarray(self, A: List[int], K: int) -> int:
        d = collections.deque([0, 0])
        res, cur = float("inf"), 0
        for r, val in enumerate(A):
        	cur += val # prefix sum
        	while d and cur - d[0][-1] >= K:
        		res = min(res, r - d.popleft()[0] + 1)
        	while d and cur <= d[-1][1]: # keep prefix sum increasing in deque
        		d.pop()
        	d.append([r+1, cur])
        return res if res < float("inf") else -1
