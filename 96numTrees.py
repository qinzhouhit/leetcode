'''
keys: dp
Solutions:
Similar:
T: O(N^2)
S: O(N)
'''

class Solution:
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                G[i] += G[j]*G[i-1-j]
        return G[n]

    def numTrees1(self, n: int) -> int:
        # simplify the calculation
        c = 1
        for i in range(n):
            c = c*2*(2*i+1)/(i+2)
        return int(c)
