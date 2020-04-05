'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                G[i] += G[j]*G[i-1-j]
        return G[n]
