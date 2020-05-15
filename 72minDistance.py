'''keys: dpSolutions: Similar:T: O(l1*l2)S: O(l1*l2) -> O(min(l1, l2))'''from typing import Listimport collectionsclass Solution:    # https://leetcode.com/problems/edit-distance/discuss/159295/Python-solutions-and-intuition    # iterative with dp    def minDistance3(self, word1: str, word2: str) -> int:        l1 = len(word1)        l2 = len(word2)        # table = [[0] * (l2 + 1) for _ in range(l1 + 1)]        dp = [[0] * (l2+1)] * (l1+1) # with padding        for i in range(l1 + 1):            dp[i][0] = i        for j in range(l2 + 1):            dp[0][j] = j        for i in range(1, l1 + 1):            for j in range(1, l2 + 1):                if word1[i - 1] == word2[j - 1]:                    dp[i][j] = dp[i - 1][j - 1]                else:                    dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])        return dp[-1][-1]    # recursive with dp    #  a recursive approach with caching is "top-down" and    #  an iterative solution using a 2D/1D array is "bottom-up"    def minDistance2(self, word1: str, word2: str) -> int:        return self.helper1(word1, word2, 0, 0, {})    def helper1(self, word1, word2, i, j, memo):        """Memoized solution"""        if i == len(word1) and j == len(word2):            return 0        if i == len(word1):            return len(word2) - j        if j == len(word2):            return len(word1) - i        if (i, j) not in memo:            if word1[i] == word2[j]:                ans = self.helper1(word1, word2, i + 1, j + 1, memo)            else:                insert = 1 + self.helper1(word1, word2, i, j + 1, memo)                delete = 1 + self.helper1(word1, word2, i + 1, j, memo)                replace = 1 + self.helper1(word1, word2, i + 1, j + 1, memo)                ans = min(insert, delete, replace)            memo[(i, j)] = ans        # print (i, j, memo[(i, j)])        return memo[(i, j)]    # naive recursive but TLE    def minDistance1(self, word1: str, word2: str) -> int:        if not word1 and not word2:            return 0        if not word1:            return len(word2)        if not word2:            return len(word1)        if word1[0] == word2[0]:            return self.minDistance1(word1[1:], word2[1:])        insert = 1 + self.minDistance1(word1, word2[1:])        delete = 1 + self.minDistance1(word1[1:], word2)        replace = 1 + self.minDistance1(word1[1:], word2[1:])        return min(insert, delete, replace)    # not working, not sure why?    '''    dp[i][j] := minDistance(word1[0...i-1], word2[0...j-1])    dp[i][j] = 1) i if j == 0; 2) j if i == 0; 3) dp[i-1][j-1]    if word1[i-1] == word2[j-1]    4) min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1    '''    def minDistance(self, word1: str, word2: str) -> int:        l1, l2 = len(word1), len(word2)        dp = [[-1] * (l2+1)] * (l1+1) # with padding        return self.helper(word1, word2, l1, l2, dp)    # minDistance from word1[0:l1-1] to word2[0:l2-1]    def helper(self, word1, word2, l1, l2, dp):        if l1 == 0: return l2        if l2 == 0: return l1        if dp[l1][l2] >= 0:            return dp[l1][l2]        res = 0        if word1[l1-1] == word2[l2-1]:            res = self.helper(word1, word2, l1-1, l2-1, dp)        else:            res = min(self.helper(word1, word2, l1-1, l2-1, dp),                      self.helper(word1, word2, l1-1, l2, dp),                      self.helper(word1, word2, l1, l2-1, dp)) + 1 # replace/insert/delete            # res1 = self.helper(word1, word2, l1-1, l2-1, dp)            # res2 = self.helper(word1, word2, l1-1, l2, dp)            # res3 = self.helper(word1, word2, l1, l2-1, dp)            # print (res1, res2, res3)            # res = min(res1, res2, res3) + 1        # print (dp)        dp[l1][l2] = res        return dp[l1][l2]sol = Solution()print (sol.minDistance3("horse", "ros"))                        