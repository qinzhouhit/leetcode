'''
keys: backtracking and DP
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # TODO: improved dp, S: O(n) now
    # dp[i] := min cuts for s[0:i]
    def minCut1(self, s: str) -> int:
        n = len(s)
        dp = [n]*n
        for m in range(n):
            for d in range(2):
                j = m + d
                for i in range(m, -1, -1):
                    if j < n and s[i] == s[j]:
                        dp[j] = min(dp[j], (dp[i-1]+1) if i else 0)
                    j += 1
        print (dp)
        return dp[n-1]


    # TODO: dp. T: O(n^2) for processing valid and cut exploration
    # S: O(n^2) for valid
    # dp[i] := min cuts for s[0:i]
    # s[0:i] cut into s[0:j] and s[j:i], making s[j:i] a palindrome and
    # solve subproblem s[0:j]
    def minCut(self, s: str) -> int:
        n = len(s)
        # valid[i][j] = 1 := s[i:j] is palindrome
        valid = [[True]*n for _ in range(n)]
        dp = [n]*n

        # processing valid
        for l in range(2, n+1): # starting from 2 since string of length 1 is always palindrome
            for i in range(n):
                j = i + l - 1
                if j < n:
                    valid[i][j] = (s[i] == s[j] and valid[i+1][j-1])
                    # valid[i][j] = self.isPar(s[i:j+1]) # slower
                j += 1

        # for cuts
        for i in range(n): # choose cut index
            if valid[0][i]: # s[0:i] already a palindrome
                dp[i] = 0 # no cut needed
                continue
            for j in range(i): # s[0:i] not a palindrome, cut it
                if valid[j+1][i]: # if right substring is palindrome
                    dp[i] = min(dp[i], dp[j] + 1)
        return dp[n-1]

    def isPar(self, s):
        return s == s[::-1]

sol = Solution()
print (sol.minCut1("cabababcbc"))
