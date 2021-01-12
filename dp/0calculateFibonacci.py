'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

# top-down
def calculateFibonacci(n):
	memo = [-1] * (n+1)
	return helper(n, memo)

def helper(n, memo):
	if n < 2:
		return n
	if memo[n] != -1:
		return memo[n]

	memo[n] = helper(n-1, memo) + helper(n-2, memo)
	print (memo)
	return memo[n]


def main():
  print("5th Fibonacci is ---> " + str(calculateFibonacci(5)))
  # print("6th Fibonacci is ---> " + str(calculateFibonacci(6)))
  # print("7th Fibonacci is ---> " + str(calculateFibonacci(7)))

main()


# bottom-up
def calculateFibonacci(n):
	dp = [0, 1]
	for i in range(2, n+1):
		dp[i] = dp[i-1] + dp[i-2]
	return dp[n]




