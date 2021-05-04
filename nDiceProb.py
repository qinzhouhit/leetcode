'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


# https://leetcode-cn.com/problems/nge-tou-zi-de-dian-shu-lcof/solution/nge-tou-zi-de-dian-shu-dong-tai-gui-hua-ji-qi-yo-3/

# dp[i][j]: the number of appearance of total sum j after using i dices
class Solution:
    def dicesProbability(self, n: int) -> List[float]:
    	dp = [[0] * 66 for _ in range(12)]
    	for i in range(1, 7):
    		dp[1][j] = 1 # using 1 dice, you can get value of 1 to 6 once

    	for i in range(2, n+1):
    		for j in range(i, 6*i + 1):
    			for cur in range(1, 7):
    				if j - cur <= 0:
    					break
    				dp[i][j] += dp[i - 1][j - cur]
    	all_combs = 6 ** n
    	res = []
    	for i in range(n, 6*n + 1):
    		res.append(dp[n][i] / all_combs)
    	return res


