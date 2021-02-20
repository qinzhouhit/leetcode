'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



# notice that the greater number may not be right next to the num


class Solution:
	# monotonous stack
	# O(m+n) for S and T
	def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
		stack = []
        h = {}
        res = [0] * len(nums1)
        for i, val in enumerate(nums2):
            while stack and val > stack[-1]:
                h[stack.pop()] = val
            stack.append(val)
        while stack:
            h[stack.pop()] = -1
        for i, val in enumerate(nums1):
            res[i] = h[val]
        return res


	# brute force
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
    	len1, len2 = len(nums1), len(nums2)
    	res = [0] * len1
    	for i in range(len1):
    		found = False
    		for j in range(len2):
    			if found and nums2[j] > nums1[i]:
    				res[i] = nums2[j]
    				break
    			if nums2[j] == nums1[i]:
    				found = True
    		if j == len1:
    			res[i] = -1
    	return res