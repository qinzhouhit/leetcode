'''
keys: the transition from a recursive solution to an iterative one and finally,
 to a space optimized iterative solution
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # TODO: huahua
    # T: O(n^2). S: O(n^2)
    # dp[i][j] := num of subseq of s[1:j] equals t[1:i]
    def numDistinct1(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = [[0]*len(ls + 1) for _ in range(len(lt + 1))]
        dp[0][:] = [1]*len(ls + 1)
        for i in range(1, lt+1):
            for j in range(1, ls+1):
                if t[i-1] == s[j-1]:
                    dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i][j-1]
        return dp[lt][ls]


    def numDistinct(self, s: str, t: str) -> int:
        # t is the short one (to be matched)
        # Dictionary for memoization
        memo = {}

        def uniqueSubsequences(i, j):

            M, N = len(s), len(t)

            # Base case
            if i == M or j == N or M - i < N - j:
                return int(j == N)

            # Check if the result is already cached
            if (i, j) in memo:
                return memo[i,j]

            # Always make this recursive call
            ans = uniqueSubsequences(i + 1, j)

            # If the characters match, make the other
            # one and add the result to "ans"
            if s[i] == t[j]:
                ans += uniqueSubsequences(i + 1, j + 1)

            # Cache the answer and return
            memo[i, j] = ans
            return ans

        return uniqueSubsequences(0, 0)
