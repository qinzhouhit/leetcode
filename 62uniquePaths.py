'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def uniquePaths(self, m, n):
        mat=[[1 for x in range(n)] for x in range(m)]
        for i in range(1,m):
            for j in range(1,n):
                mat[i][j]=mat[i-1][j]+mat[i][j-1]
        return mat[-1][-1]
