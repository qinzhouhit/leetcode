'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

'''
Count of Subset Sum (hard)
Given a set of positive numbers, find the total number of subsets whose sum 
is equal to a given number ‘S’.

Input: {1, 1, 2, 3}, S=4
Output: 3
The given set has '3' subsets whose sum is '4': {1, 1, 2}, {1, 3}, {1, 3}
Note that we have two similar sets {1, 3}, because we have two '1' in our input.

upgraded version of the subset sum, since we need to cound how many instead of T/F
'''

# optimized space
def count_subsets3(nums, s):
	dp = [0] * (s+1)
	dp[0] = 1

	for i in range(1, s+1):
		dp[i] = 1 if nums[0] == i else 0

	for i in range(1, len(nums)):
		for j in range(s, -1, -1):
			if j >= nums[i]:
				dp[j] += dp[j-nums[i]]
	return dp[s]

# bottom up 
# S and T: O(N*S)
def count_subsets2(nums, s):
	dp = [[-1] * (s+1) for _ in range(len(nums)+1)]

	for i in range(n): # no number
		dp[i][0] = 0

	for j in range(1, s+1):
		# if not then 0 since we need to add all dp values later
		dp[0][j] = 1 if nums[0] == j else 0

	for i in range(1, n):
		for j in range(1, s+1):
			dp[i][j] = dp[i-1][j] 
			if nums[i] <= j: # notice that we need to add here
				dp[i][j] += dp[i-1][j-nums[i]]
	return dp[n-1][s]





# top-down
def count_subsets1(nums, s):
	memo = [[-1] * (s+1) for _ in range(len(nums)+1)]
	return helper1(nums, s, 0)

def helper1(nums, cur_sum, curIdx):
	if cur_sum == 0:
		return 1
	len(nums) = n
	if n == 0 or curIdx >= n:
		return 0
	if dp[curIdx][cur_sum] == -1:
		ct1 = 0
		if nums[curIdx] <= cur_sum:
			ct1 = helper1(nums, cur_sum-nums[curIdx], curIdx+1)
		ct2 = helper(nums, cur_sum, curIdx+1)
		dp[curIdx][cur_sum] = ct1 + ct2

	return dp[curIdx][cur_sum]




# T: O(2^n)
# S: O(n) for the recursion stack
def count_subsets(nums, s):
	return help(nums, s, 0)

def helper(nums, cur_sum, curIdx):
	if cur_sum == 0:
		return 1
	n = len(nums)
	if n == 0 or curIdx >= n:
		return 0

	# select the number at curIdx
	ct1 = 0
	# skip when the cur number is larger than cur_sum
	if nums[curIdx] <= cur_sum: 
		ct1 = helper(nums, cur_sum-nums[curIdx], curIdx+1)
	ct2 = helper(nums, cur_sum, curIdx+1) # exclude cur number
	return ct1 + ct2


