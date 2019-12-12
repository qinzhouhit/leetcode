class Solution:
    def longestIncreasingPath(self, matrix):
        def dfs(i, j):
            if not dp[i][j]:
                val=matrix[i][j]
                dp[i][j]=1+max(
                    dfs(i-1,j) if i and val>matrix[i-1][j] else 0,
                    dfs(i,j-1) if j and val>matrix[i][j-1] else 0,
                    dfs(i+1, j) if i<rows-1 and val>matrix[i+1][j] else 0,
                    dfs(i,j+1) if j<cols-1 and val>matrix[i][j+1] else 0
                )
            return dp[i][j]

        if not matrix or not matrix[0]:
            return 0

        rows, cols=len(matrix), len(matrix[0])
        dp=[[0]*cols for _ in range(rows)]
        # for i in range(rows):
        #     for j in range(cols):
        return (max(dfs(i, j) for i in range(rows) for j in range(cols)))
                # return (dfs(i, j))

a=[
  [9,9,4],
  [6,6,8],
  [2,1,1]
]
obj=Solution()
obj.longestIncreasingPath(a)


