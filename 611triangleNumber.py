'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# brute force, LTE
	# T: O(n^3), S: O(1)
    def triangleNumber(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                for k in range(j+1, n):
                    if nums[i] + nums[j] > nums[k] and nums[i] + nums[k] > nums[j] and nums[j] + nums[k] > nums[i]:
                        res += 1
        return res


    # T: O(n^2) for two pointers
    # https://leetcode.com/problems/valid-triangle-number/discuss/104174/Java-O(n2)-Time-O(1)-Space
    def triangleNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	res, n = 0, len(nums)
    	for i in range(n-1, 1, -1):
    		l, r = 0, i-1
    		while l < r:
    			if nums[l] + nums[r] > nums[i]:
    				res += r - l # all the vals in between will also work, just increase l
    				r -= 1
    			else:
    				l += 1
    	return res


   	# official O(n^2)
    def triangleNumber(self, nums: List[int]) -> int:
    	nums.sort()
    	res = 0; n = len(nums)
    	for i in range(n-2):
    		k = i + 2
    		for j in range(i+1, n-1):
    			if nums[i] != 0:
    				while k < n and nums[i] + nums[j] > nums[k]:
    					k += 1
    				res += k - j - 1
    	return res
