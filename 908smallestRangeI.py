'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
If min(A) + K < max(A) - K, then return max(A) - min(A) - 2 * K
If min(A) + K >= max(A) - K, then return 0
'''
class Solution:
	# T: O(N), S: O(1)
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maxB = max(A) - K # minimize maxB
        minB = min(A) + K # maximize minB
        diff = maxB - minB # then, the diff is minimized
        return diff if diff > 0 else 0