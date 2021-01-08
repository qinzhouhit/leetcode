'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List



# minimum subset sum difference
# Given a set of positive numbers, partition the set into two subsets 
# with minimum difference between their subset sums.
'''
Input: {1, 2, 3, 9}
Output: 3
Explanation: We can partition the given set into two subsets where minimum absolute difference 
between the sum of numbers is '3'. Following are the two subsets: {1, 2, 3} & {9}.
'''

# bottom up dp
# we try to find a subset with sum as close to s//2
# S and T: O(N*S)
def can_partition1(nums):
	s = sum(nums)
	n = len(num)
	dp = [[False] * (s//2+1) for _ in range(n)]
	# populate the s=0 column
	for i in range(n):
		dp[i][0] = True
	# with only one number, i.e., 0 means the first 1 number
	for j in range(1, s//2+1):
		dp[0][j] = nums[0] == j

	for i in range(1, n): # cur number is at index i
		for j in range(1, s//2+1):
			if dp[i-1][j]: # exclude cur number to see
			# if we can get the sum j by i-1 numbers
				dp[i][j] = dp[i-1][j]
			elif j >= num[i]:
				dp[i][j] = dp[i-1][j-nums[i]]
	sum1 = 0
	for i in range(s//2, -1, -1): # find sum1 
		if dp[n-1][i]: # if such sum1 exist by using the first n numbers
			sum1 = i
			break
	sum2 = s - sum1
	return abs(sum1 - sum2)




# brute force
def can_partition(nums):
	return helper(nums, 0, 0, 0)

def helper(nums, curIdx, sum1, sum2):
	# sum1 is for the first subset, sum2 for the second
	# base case check
	if curIdx == len(nums):
		return abs(sum1 - sum2)
	# recursive call after ioncluding cur in the first subset
	diff1 = helper(nums, curIdx+1, sum1+nums[curIdx], sum2)
	# recursive call after ioncluding cur in the second subset
	diff1 = helper(nums, curIdx+1, sum1, sum2+nums[curIdx])

	return min(diff1, diff2)

	