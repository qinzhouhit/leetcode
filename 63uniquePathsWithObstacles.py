class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        col=len(obstacleGrid[0])
        dp=[0]*col
        dp[0]=1
        for row in obstacleGrid:
            for i in range(col):
                if row[i]==1:
                    dp[i]=0
                elif i>0:
                    dp[i]+=dp[i-1]
        return dp[-1]

obj=Solution()
obj.uniquePathsWithObstacles([
  [0,0,0],
  [0,1,0],
  [0,0,0]
])
