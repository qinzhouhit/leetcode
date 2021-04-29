'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # dp, O(n) space
    def uniquePaths4(self, m, n):
        dp = [1] * n
        for i in range(1, m):
            for j in range(1, n):
                # dp[j] is acutally dp[i-1][j]
                # dp[j-1] is actually dp[i][j-1]
                dp[j] = dp[j] + dp[j-1]
        return dp[n-1]
    
    
    # dp, O(m*n)
    # dp[i][j]: number of paths reaching grid[i][j]
    def uniquePaths3(self, m, n):
        # initialize them as 1 since it takes one step to be on boarder
        # dp[0][0] does not matter since it will not be accessed
        dp = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    
    # dfs
    def uniquePaths1(self, m: int, n: int) -> int:
        self.rows = m-1
        self.cols = n-1
        self.memo = {}
        return self.check_path()
    
    def check_path(self, r=0,c=0):
        if r == self.rows and c == self.cols:
            return 1
        if r > self.rows or c > self.cols:
            return 0
        # check down and right
        # notice that tuple key can be accessed directly by (r,c)
        if (r,c) not in self.memo:
            self.memo[r,c] = self.check_path(r+1,c) + self.check_path(r,c+1)
        return self.memo[r,c]

    # self-made, starting from right-bottom corner
    def uniquePaths(self, m: int, n: int) -> int:

        def helper(r, c):
            if (r, c) in memo:
                return memo[(r, c)]
            
            if r == 1 or c == 1:
                memo[(r, c)] = 1
            else:
                memo[(r, c)] = helper(r-1, c) + helper(r, c-1)
            return memo[(r, c)]
    
        memo = {}
        return helper(m, n)
    
    
    # recursive
    @lru_cache(None)
    def uniquePaths2(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
