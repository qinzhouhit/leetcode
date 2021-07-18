""" 
keys: 
Solutions:
Similar:
T:
S:
"""

class Solution:
	"""
	Alice first. A means stoneValue.
	dp[i] means, max relative score current player can get if the 
	game starts at i-th stone (ignore previous stones)

	There are three option for Alice to choose.
	Take A[i], win (take - dp[i+1])
	Take (A[i] + A[i+1]), win (take - dp[i+2])
	Take (A[i] + A[i+1] + A[i+2]), win (take - dp[i+3])
	dp[i] equals the best outcome of these three solutions.

	so dp[i+1] mean how many score the component can win over 
	the current player. So for the player at step/stone i, the
	winning score is A[i] - dp[i+1]

	O(N) for S and T
	"""
	# bottom-up for Python due to maximum recursion limit
    def stoneGameIII(self, stoneValue: List[int]) -> str:
    	n = len(stoneValue)
    	dp = [float("-inf")] * (n + 1)  # padding extra two for i+1 and i+2
    	dp[-1] = 0  # at the beginning
    	for i in range(n - 1, -1, -1):  # backwards, since 
    		take = 0
            for k in range(i, min(n, i + 3)):
                take += stoneValue[k]
                # when calculating dp[i] for Alice, dp[i+1] should be 
    			# viewed as the amount Bob wins over Alice.
                dp[i] = max(dp[i], take - dp[k + 1])

    	if dp[0] > 0:  # dp[0]: Alice - Bob
    		return "Alice"
    	if dp[0] < 0:
    		return "Bob"
    	return "Tie"


    # huahua explicit
    def stoneGameIII(self, stoneValue: List[int]) -> str:
    	n = len(stoneValue)
    	stoneValue += [0, 0, 0]  # padding
    	dp = [float("-inf")] * n + [0, 0, 0]
    	for i in range(n - 1, -1, -1):
    		for k in [1, 2, 3]:
    			dp[i] = max(dp[i], sum(stoneValue[i: i+k]) - dp[i+k])
    	return "Alice" if dp[0] > 0 else "Bob" if dp[0] < 0 else "Tie"


    # top-down, TLE
    def stoneGameIII(self, stoneValue: List[int]) -> str:
    	n = len(stoneValue)
    	memo = [float("-inf")] * n

    	def dp(i):
    		if i >= n:
    			return 0  # 0 score
    		if memo[i] != float("-inf"):
    			return memo[i]
    		k = 0; take = 0
    		while k < 3 and k + i < n:
    			take += stoneValue[k]
    			memo[i] = max(memo[i], take - memo[i + k + 1])
    		return memo[i]

    	score = dp(0)
    	return ["Tie", "Alice", "Bob"][cmp[score, 0]]



    # super concise
    # cmp(a, b)
    # 	a < b: return -1
    #	a == b: return 0
    #	a > b: return 1
    def stoneGameIII(self, stoneValue: List[int]) -> str:
    	dp = [0] * 3
        for i in range(len(stoneValue) - 1, -1, -1):
            dp[i % 3] = max(sum(stoneValue[i:i + k]) - dp[(i + k) % 3] for k in (1, 2, 3))
        return ["Tie", "Alice", "Bob"][cmp(dp[0], 0)]
