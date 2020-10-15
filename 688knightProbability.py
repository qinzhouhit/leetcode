'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

# https://www.youtube.com/watch?v=MyJvMydR2G4
# dp[k][i][j] := number of ways to (j, i) after k steps
# dp[k][i][j] = sum(dp[k-1][y][x]) for all (x,y) can move to (j, i)
class Solution:
    
    # T: O(K*N^2); S: O(N^2)
    # final dp[r][c]: probability of on (r,c) after k steps
    # summing up across all cells: the probability of remaining on the board
    def knightProbability(self, N: int, K: int, r: int, c: int) -> float:
        dp = [[0] * N for _ in range(N)]
        dp[r][c] = 1 # one way, i.e., no hop
        for _ in range(K):
            dp2 = [[0] * N for _ in range(N)]
            for r, row in enumerate(dp):
                for c, val in enumerate(row):
                    for dr, dc in ((2,1),(2,-1),(-2,1),(-2,-1),
                                   (1,2),(1,-2),(-1,2),(-1,-2)):
                        if 0 <= r + dr < N and 0 <= c + dc < N:
                            # 1/8 means each probability of each step
                            dp2[r+dr][c+dc] += val / 8.0
            dp = dp2

        return sum(map(sum, dp))


