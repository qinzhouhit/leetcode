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
    def uniquePaths3(self, m, n):
        dp = [[1 for x in range(n)] for x in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

    
    # dfs
    def uniquePaths1(self, m: int, n: int) -> int:
        
        self.r_max = m-1
        self.c_max = n-1
        self.memo = dict()
        
        return self.check_path()
    
    def check_path(self, r=0,c=0):
        if r == self.r_max and c == self.c_max:
            return 1
        if r > self.r_max or c > self.c_max:
            return 0
        # check down and right
        # notice that tuple key can be accessed directly by (r,c)
        if (r,c) not in self.memo:
            self.memo[r,c] = self.check_path(r+1,c) + self.check_path(r,c+1)
        return self.memo[r,c]
    
    # recursive
    def uniquePaths2(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1
        
        return self.uniquePaths(m - 1, n) + self.uniquePaths(m, n - 1)
