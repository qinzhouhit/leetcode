'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# dp[i][j] is the length of longest common subarray ending with A[i-1] and B[j-1]
	# dp[la][lb] is the length of longest common subarray ending with A[la-1] and B[lb-1]
    def findLength(self, A: List[int], B: List[int]) -> int:
    	la, lb = len(A), len(B)
        dp = [[0]*(lb+1) for _ in range(la+1)]
        for i in range(1, la+1): # when i == 0 or j == 0, dp[i][j]=0
            for j in range(1, lb+1): # since i==0 means no letter
                if A[i-1] == B[j-1]:
                    dp[i][j] = dp[i-1][j-1]+1
                # else:
                #     dp[i][j] = dp[i-1][j-1]
        return max([v for row in dp for v in row])
