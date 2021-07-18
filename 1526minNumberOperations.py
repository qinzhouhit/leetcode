""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/discuss/754674/JavaC%2B%2BPython-Comparison-of-Consecutive-Elements
	# T: O(N), S: O(1)
    def minNumberOperations(self, target: List[int]) -> int:
    	res = prev = 0
    	for num in target:
    		res += max(num - prev, 0)
    		prev = num
    	return res