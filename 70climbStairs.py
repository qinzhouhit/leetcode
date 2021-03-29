'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:

	# T: O(logn), S: O(1)
	# Fibonacci Formula
	def climbStairs(self, n: int) -> int:
		sqrt5 = math.sqrt(5)
		fibn = math.pow((1+sqrt5)/2, n+1) - math.pow((1-sqrt5)/2, n+1)
		return int(fibn / sqrt5)


	# T: O(n): S: O(1)
	def climbStairs(self, n: int) -> int:
		if n == 1:
			return 1
		first, second = 1, 2
		for i in range(3, n+1):
			third = first + second
			first = second
			second = third
		return second


	# dp, self-made, O(n) for S and T
	def climbStairs(self, n: int) -> int:
		if n == 1:
            return 1
        if n == 2:
            return 2
        
        dp = [0] * n # dp[i]: number of steps to reach i+1
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i-1] + dp[i-2]
    
        return dp[n-1]

    # memo
    def climbStairs(self, n: int) -> int:
    	def helper(i, n, memo):
    		if i > n:
    			return 0
    		if i == n: # i defines the current step 
    			return 1
    		if memo[i]:
    			return memo[i]
    		memo[i] = helper(i+1, n, memo) + helper(i+2, n, memo)
    		return memo[i]

    	memo = [0] * (n+1)
    	return helper(0, n, memo)



	# self-made, TLE, O(2^n)
    def climbStairs(self, n: int) -> int:
        
        def helper(remain):
            if remain < 0:
                return 0
            if remain == 0:
                return 1
            
            res = 0
            res += helper(remain-1)
            res += helper(remain-2)
            return res
        

        return helper(n)
obj=Solution()
print(obj.mySqrt(10))


