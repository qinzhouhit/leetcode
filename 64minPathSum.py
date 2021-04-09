'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def minPathSum(self, grid):
        r, c = len(grid), len(grid[0])
        dp = [grid[0][0]] * r
        for i in range(1, r):
            dp[i] = dp[i-1] + grid[i][0]
        for j in range(1, c):
            dp[0] += grid[0][j]
            for i in range(1,r):
                # dp[i-1]: above cell, dp[i]: left cell
                dp[i] = min(dp[i-1], dp[i]) + grid[i][j];
        return dp[-1]


    # 
    def minPathSum(self, grid):
        rows, cols = len(grid), len(grid[0])
        dp = [[0] * cols for _ in range(rows)]
        for r in range(rows-1, -1, -1):
            for c in range(cols-1, -1, -1):
                if r == rows-1 and c != cols-1:
                    dp[r][c] = grid[r][c] + dp[r][c+1]
                elif r != rows-1 and c == cols-1:
                    dp[r][c] = grid[r][c] + dp[r+1][c]
                elif r != rows-1 and c != cols-1:
                    dp[r][c] = grid[r][c] + min(dp[r+1][c], dp[r][c+1])
                else:
                    dp[r][c] = grid[r][c]
        return dp[0][0]


obj=Solution()
print(obj.minPathSum([
  [1,3,1],
  [1,5,1],
  [4,2,1]
]))
