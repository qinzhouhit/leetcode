'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def minPathSum(self, grid):
        r,c=len(grid), len(grid[0])
        dp=[grid[0][0]]*r
        for i in range(1,r):
            dp[i]=dp[i-1]+grid[i][0]
        for j in range(1,c):
            dp[0]+=grid[0][j]
            for i in range(1,r):
                # dp[i-1]: above cell, dp[i]: left cell
                dp[i]=min(dp[i-1], dp[i])+grid[i][j];
        return dp[-1]

obj=Solution()
print(obj.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
