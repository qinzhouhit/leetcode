'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


'''
Target Sum (hard) #
You are given a set of positive numbers and a target sum ‘S’. Each 
number should be assigned either a ‘+’ or ‘-’ sign. We need to find 
the total ways to assign symbols to make the sum of the numbers equal
 to the target ‘S’.

Input: {1, 1, 2, 3}, S=1
Output: 3
Explanation: The given set has '3' ways to make a sum of '1': 
{+1-1-2+3} & {-1+1-2+3} & {+1+1+2-3}

essentially is to find two subsets with sum difference as s
s1 - s2 = s
s1 + s2 = sum(nums)
adding them => s1 = (s+sum(nums))/2
i.e., finding count of subsets of the given numbers whose sum is equal to (S + Sum(num)) / 2
'''



# S: O(S)
def find_target_subsets1(nums, s):
	totalSum = sum(nums)
	if totalSum < s or (s+totalSum) % 2:
		return 0
	return helper1(nums, (s+totalSum)//2)

def helper1(nums, s): # s is the target sum
	n = len(nums)
	dp = [0] for (s+1)
	dp[0] = 1 # obtaining sum of 0
	for j in range(1, s+1):
		dp[j] = nums[0] == j
	for i in range(1, n):
		for j in range(s, -1, -1):
			if j >= nums[i]:
				dp[j] += dp[j-nums[i]]
	return dp[s]



# dp; S and T: O(N*S)
def find_target_subsets(nums, s):
	totalSum = sum(nums)
	if totalSum < s or (s+totalSum) % 2:
		return 0
	return helper(nums, (s+totalSum)//2)

def helper(nums, s): # s is the target sum
	n = len(nums)
	dp = [[0] * (s+1) for _ in range(n)]

	for i in range(n):
		dp[i][0] = 1
	for j in range(1, s+1):
		dp[0][j] = nums[0] == j
	for i in range(1, n):
		for j in range(1, s+1):
			dp[i][j] = dp[i-1][j]
			if nums[i] <= j:
				dp[i][j] += dp[i-1][j-nums[i]]
	return dp[n-1][s]



















