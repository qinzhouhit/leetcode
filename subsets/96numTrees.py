'''
keys: dp
Solutions:
Similar: 95
T: O(N^2)
S: O(N)
'''

class Solution:
    # educative.io
    # Estimated time complexity will be O(n*2^n) but the actual time complexity 
    # O(4^n/sqrt(n)) is bounded by the Catalan number and is beyond the scope of a coding interview. See more details here.

    def numTrees2(self, n: int) -> int:
        if n <= 1: return 1
        ct = 0
        for i in range(1, n+1):
            # making "i" as root of the tree
            ctOfLeftSubtrees = self.numTrees2(i-1)
            ctOfRightSubtrees = self.numTrees2(n-i)
            ct += (ctOfLeftSubtrees * ctOfRightSubtrees)
        return ct

    # educative.io, memo
    @lru_cache(typed=False)
    def numTrees3(self, n: int) -> int:
        if n <= 1: return 1
        ct = 0
        for i in range(1, n+1):
            # making "i" as root of the tree
            ctOfLeftSubtrees = self.numTrees2(i-1)
            ctOfRightSubtrees = self.numTrees2(n-i)
            ct += (ctOfLeftSubtrees * ctOfRightSubtrees)
        return ct

    # dp, https://leetcode.com/problems/unique-binary-search-trees/discuss/31666/DP-Solution-in-6-lines-with-explanation.-F(i-n)-G(i-1)-*-G(n-i)
    # T: O(N^2), S: O(N)
    def numTrees(self, n: int) -> int:
        G = [0]*(n+1)
        G[0] = 1
        for i in range(1, n+1):
            for j in range(i):
                G[i] += G[j]*G[i-j-1]
        return G[n]

    # T: O(N), S: O(1), math
    def numTrees1(self, n: int) -> int:
        # simplify the calculation
        c = 1
        for i in range(n):
            c = c*2*(2*i+1)/(i+2)
        return int(c)

    
