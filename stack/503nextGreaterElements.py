'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
	# O(n) for S and T
	# https://leetcode.com/problems/next-greater-element-ii/solution/251306
	# https://leetcode.com/problems/next-greater-element-ii/solution/
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        n = len(nums)
        res = [0] * n
        h = {}
        for i in range(2*n-1, -1, -1):
        	# try to make cur_num < nums[stack[-1]] since we want to find next greater one
            while stack and nums[i % n] >= nums[stack[-1]]:
                stack.pop()
            res[i % n] = nums[stack[-1]] if stack else -1
            stack.append(i % n)
        return res