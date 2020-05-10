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
        dp = [[0]*(ls + 1) for _ in range((lt + 1))] # (lt+1)*(ls+1)
        dp[0][:] = [1]*(ls + 1)
        for i in range(1, lt+1):
            for j in range(1, ls+1):
                dp[i][j] = dp[i][j-1]
                if t[i-1] == s[j-1]:
                    dp[i][j] += dp[i-1][j-1]
        return dp[lt][ls]


    # TODO: huahua iterative dp with optimized space
    # S: O(N), N as length of t
    def numDistinct3(self, s: str, t: str) -> int:
        ls, lt = len(s), len(t)
        dp = [0]*(lt + 1)
        dp[0] = 1 # t as empty string
        for i in range(1, ls+1):
            prev = 1 # prev is the one in front of olddpi
            for j in range(1, lt+1):
                olddpj1 = dp[j] # olddpi is for last round dp[i], saved for next round, i.e., j+1
                if s[i-1] == t[j-1]:
                    dp[j] += prev
                prev = olddpj1
        return dp[lt]


    # TODO: official iterative dp (almost always faster than its
    #  recursive memoization-based counterpart.
    # similar to huahua's solution except for different padding
    def numDistinct2(self, s: str, t: str) -> int:
        M, N = len(s), len(t)

        # Dynamic Programming table
        dp = [[0 for i in range(N + 1)] for j in range(M + 1)]

        # Base case initialization
        for j in range(N + 1):
            dp[M][j] = 0

        # Base case initialization
        for i in range(M + 1):
            dp[i][N] = 1

        # Iterate over the strings in reverse so as to
        # satisfy the way we've modeled our recursive solution
        for i in range(M - 1, -1, -1):
            for j in range(N - 1, -1, -1):

                # Remember, we always need this result
                dp[i][j] = dp[i + 1][j]

                # If the characters match, we add the
                # result of the next recursion call (in this
                # case, the value of a cell in the dp table
                if s[i] == t[j]:
                    dp[i][j] += dp[i + 1][j + 1]

        return dp[0][0]


    # TODO: official recursive dp
    # T: O(N*M), as M and N as length. S: O(N*M) for the hash map
    def numDistinct(self, s: str, t: str) -> int:
        # t is the short one (to be matched)
        # Dictionary for memoization
        memo = {}

        def uniqueSubsequences(i, j):

            M, N = len(s), len(t)

            # Base case
            if i == M or j == N or M - i < N - j:
                # return 1 if we reached the end of t
                # return 0 if we have more of t than s left
                return int(j == N) #

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


sol = Solution()
print (sol.numDistinct3("babgbag", "bag"))
