""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:

    # concise version
    # O(m * n) for S and T
    # https://leetcode.com/problems/number-of-enclaves/discuss/265534/Python-clean-DFS-solution
    def numEnclaves(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            grid[i][j] = 0  # set those 1s on/connected to boundaries as 0
            for x, y in (i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1):
                if 0 <= x < m and 0 <= y < n and A[x][y]:
                    dfs(x, y)

        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and (i == 0 or j == 0 or i == m - 1 or j == n - 1):
                    dfs(i, j)
        return sum(sum(row) for row in grid)



	# revised based on LC1020
    def numEnclaves(self, grid: List[List[int]]) -> int:
    	if not grid or not grid[0]:
            return 0
        rows, cols = len(grid), len(grid[0])
        res = 0

        def dfs(r, c, val, isBoundry):
            nonlocal res
            if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 1:
                grid[r][c] = val  # flood the land (0s) by water (1s)
                if not isBoundry:
                    res += 1
                dfs(r, c+1, val, isBoundry)
                dfs(r, c-1, val, isBoundry)
                dfs(r+1, c, val, isBoundry)
                dfs(r-1, c, val, isBoundry)

        # remove all land connected to the edges using flood fill
        # since there won't be a closed island according to definition
        for r in range(rows):
            for c in range(cols):
                if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and grid[r][c] == 1:
                    dfs(r, c, 0, True)

        # traverse the grid again, find enclosed island and 
        # populate the zeros into ones

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    dfs(r, c, 0, False)

        return res

