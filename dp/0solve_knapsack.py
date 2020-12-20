'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
'''
Given the weights and profits of ‘N’ items, we are asked to put these items in a knapsack with a capacity ‘C.’ The goal is to get the maximum profit out of the knapsack items. Each item can only be selected once, as we don’t have multiple quantities of any item.

Let’s take Merry’s example, who wants to carry some fruits in the knapsack to get maximum profit. Here are the weights and profits of the fruits:

Items: { Apple, Orange, Banana, Melon }
Weights: { 2, 3, 1, 4 }
Profits: { 4, 5, 3, 7 }
Knapsack capacity: 5

0/1 knapsack problem: for each step, we can choose one item or skip it
'''

# recursion
# T: O(2^n), n as the total number of items
# S: O(n) for the recursive stack since it is dfs
def solve_knapsack(profits, weights, capacity):
	return helper(profits, weights, capacity, 0)

def helper(profits, weights, capacity, curIdx):
	if capacity <= 0 or curIdx >= len(profits):
		return 0

	profit_include = 0
	if weights[curIdx] <= capacity: # including the curIdx
		profit_include = profits[curIdx] + helper(profits, weights, \
			capacity-weights[curIdx], curIdx+1)
	# exclduing the curIdx item
	profit_exclude = helper(profits, weights, capacity, curIdx+1)
	return max(profit_include, profit_exclude)


# top-down, i.e., memoization
# track the changing parameters in the the recursive functions
# T and S: O(N*C), N as number of items and C as capacity
def solve_knapsack1(profits, weights, capacity):
	# padding capacity is because we can actually reach idx at "capacity"
	memo = [[-1 for _ in range(capacity+1)] for _ in range(len(profits))]
	return helper(profits, weights, capacity, 0, memo)

def helper1(profits, weights, capacity, curIdx, memo):
	if capacity <= 0 or curIdx >= len(profits):
		return 0
	if memo[curIdx][capacity] != -1:
		return memo[curIdx][capacity]

	profit_include = 0
	if weights[curIdx] <= capacity: # including the curIdx
		profit_include = profits[curIdx] + helper(profits, weights, \
			capacity-weights[curIdx], curIdx+1)
	# exclduing the curIdx item
	profit_exclude = helper(profits, weights, capacity, curIdx+1)
	memo[curIdx][capacity] = max(profit_include, profit_exclude)
	return memo[curIdx][capacity]


# bottom-up, i.e., find the transition function to update from the initialization
# dp[i][c]: the max profit for capacity c from the first i items
# two choice: 1) slip the one, dp[i-1][c]; 2) take it, profit[i]+dp[i-1][c-weight[i]]
def solve_knapsack2(profits, weights, capacity):
	dp = [[0]*(capacity+1) for _ in range(len(profits))]
	# first col will be 0 since no capacity for any item
	# first row will be profit[0] since one item/ weight
	for c in range(capacity+1):
		if weights[0] <= c: # 0 is because we update the 0-th row
			dp[0][c] = profits[0]

	for i in range(1, len(profits)):
		for c in range(1, capacity+1): # starting from one item
			profit1, profit2 = 0, 0
			if weights[i] <= c: # has to determine to include the item
				profit1 = profits[i]+dp[i-1][capacity-weights[i]]
			profit2 = dp[i-1][c] # skip the item
			dp[i][c] = max(profit1, profit2)
	trace_back(dp, profits, weights, capacity)
	return dp[-1][-1]

def trace_back(dp, profits, weights, capacity):
	n = len(weights)
	totalProfit = dp[n-1][capacity]
	res = []
	for i in range(n-1, 0, -1):
		if totalProfit != dp[i][capacity]:
			res.append(weights[i])
			totalProfit -= profits[i]
			capacity -= weights[i]
	if totalProfit != 0:
		res.append(weights[0])
	print ("Trace:", " ".join(res))


# one dimension dp
# only need the profits from last column
def solve_knapsack3(profits, weights, capacity):
	dp = [0]*(capacity+1)
	for c in range(capacity):
		if weights[0] <= c:
			dp[c] = profits[0]
	print (dp)
	for i in range(1, len(profits)):
		for c in range(capacity, 0, -1): # or include 0, does not matter
		# for c in range(0, capacity+1): # this is wrong since one increases capacity every time..
			profit1, profit2 = 0, 0
			if weights[i] <= c:
				profit1 = profits[i] + dp[c - weights[i]]
			profit2 = dp[c]
			dp[c] = max(profit1, profit2)
			print (dp, i, c)
	return dp[c]

# print (solve_knapsack3([1, 6, 10, 16], [1, 2, 3, 5], 7))
print (solve_knapsack3([1, 6, 10, 16], [1, 2, 3, 5], 6))




























