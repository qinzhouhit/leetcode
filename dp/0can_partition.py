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
# S and T: O(N*S), N as number of nums
def can_partition(nums, s):
	# dp[i][j]: the first i numbers adding to sum as j
	n = len(nums)
	dp = [[False] * (s+1) for _ in range(len(nums))]

	for i in range(n): # with sum as 0, always true
		dp[i][0] = True 
	# with one number, starting from 1 since dp[0][0] 
	# is already processed in above
	for c in range(1, s+1): 
		dp[0][c] = nums[0] == c
	for i in range(1, n): # numbers
		for j in range(1, s+1): # sum
			if dp[i-1][j]: # already achieved sum j with i-1 numbers
				dp[i][j] = dp[i-1][j] # don't need cur number
			elif nums[i] <= j: # including cur number
				dp[i][j] = dp[i-1][j-nums[i]]
	return dp[n-1][s]


# one dimension 
def can_partition1(nums, s):
	n = len(nums)
	dp = [False] * (s+1)
	dp[0] = True
	for i in range(1, s+1):
		dp[i] = nums[0] == i
	for i in range(1, n):
		for j in range(1, s+1):
			if not dp[j] and j >= nums[i]:
				dp[j] = dp[j-nums[i]]
	return dp[s]













	




