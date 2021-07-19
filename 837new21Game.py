""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	"""
	# https://leetcode.com/problems/new-21-game/discuss/132334/One-Pass-DP-O(N)
	# dp, O(N) for S and T
	dp[i] is the probability that we get points i at some moment.
	In another word:
	1 - dp[i]is the probability that we skip the points i.
	"""
	def new21Game(self, n: int, k: int, maxPts: int) -> float:
		if k == 0 or n >= k + maxPts:
			return 1 
		dp = [1.0] + [0.0] * n
        Wsum = 1.0
        for i in range(1, n + 1):
            dp[i] = Wsum / maxPts
            if i < k: 
            	Wsum += dp[i]
            if i - maxPts >= 0: 
            	Wsum -= dp[i - maxPts]
        return sum(dp[k:])



	"""
	https://leetcode.com/problems/new-21-game/discuss/228406/Logical-Thinking
	point total range [0, K + W - 1]
	TLE
	"""
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
    	if k == 0:  # just dont draw
    		return 1 
		maxPoint = k - 1 + maxPts
		# probability[i] is probability of getting point i.
		probability = [0] * (maxPoint + 1)  

		probability[0] = 1
		for i in range(1, maxPoint + 1):  # i as the total point you get in the final
			for w in range(1, maxPts + 1):  # w as the point you draw
				if 0 <= i - w < k:
					probability[i] += probability[i - w] / maxPts

		targetProb = 0
		for i in range(k, n + 1):  # starts from k since if k-1, Alice can still draw
			targetProb += probability[i]
		return targetProb



