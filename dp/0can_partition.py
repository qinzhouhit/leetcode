'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


'''
Given a set of positive numbers, determine if a subset exists whose sum is equal
 to a given number ‘S’.

Input: {1, 2, 3, 7}, S=6
Output: True
The given set has a subset whose sum is '6': {1, 2, 3}
'''

# bottom up
def can_partition(nums, s):
	# dp as the number of values needed for s (sum)
	dp = [[False] * (s+1) for _ in range(len(nums)+1)]
	n = len(nums)

	for i in range(n+1): # 1st row or col initialization
		dp[i][0] = True 
	for c in range(s+1):
		dp[0][c] = True if nums[0] == c else False
	




