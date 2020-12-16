'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# linear scan; T: O(N) and S: O(1)
    def findPeakElement(self, nums: List[int]) -> int:
        for i in range(len(nums)-1):
        	if nums[i+1] < nums[i]:
        		return i
        return len(nums) - 1


    # iterative binary search
    def findPeakElement1(self, nums: List[int]) -> int:
	    l, r = 0, len(nums) - 1
        while l < r:
            mid = l + (r - l) // 2
            if  nums[mid] > nums[mid+1]: # descending
                r = mid # peak must be at left part
            else: # notice that nums[mid] != nums[mid+1] by definition
                l = mid + 1
        return l # in the end, l == r