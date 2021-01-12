'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # dp, O(N) for S and T
    # dp[i] = Number of ways of decoding substring s[:i]
    def numDecodings(self, s: str) -> int:
        if not s: return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != "0" else 0
        for i in range(2, len(s)+1):
            s1 = int(s[i-1: i]) # letter encoded as 1-digit
            s2 = int(s[i-2: i]) # letter encoded as 2-digit
            if 1 <= s1 <= 9:
                dp[i] += dp[i-1]
            if 10 <= s2 <= 26:
                dp[i] += dp[i-2]
        return dp[-1]


    # recursion with memo
    # O(N) for T, memo prunes the tree and devcode each index only once
    # O(N) for S, for the memo dictionary and recursion stack, N = len(s)
    memo = {}
    def numDecodings1(self, s: str) -> int:
        if not s:
            return 0
        return self.helper(s, 0)

    def helper(self, s, idx):
        if idx == len(s): 
            return 1 # as success
        if s[idx] == "0":
            return 0 # can't decode with starting 0
        if idx == len(s)-1:
            return 1
        if idx in self.memo:
            return self.memo[idx]
        res = self.helper(s, idx+1) + \
            (self.helper(s, idx+2) if int(s[idx:idx+2]) <= 26 else 0)
        self.memo[idx] = res
        return res




obj=Solution()
print (obj.numDecodings("0"))




