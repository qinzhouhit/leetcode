'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# T: O(N), S: O(1)
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        ptr = 0
        for i, val in enumerate(nums):
            if i == len(nums)-1 or nums[i+1] - nums[i] > 1:
                res.append(str(nums[ptr]) + "->" + str(val) if nums[ptr] != val else str(val))
                ptr = i + 1
        return res