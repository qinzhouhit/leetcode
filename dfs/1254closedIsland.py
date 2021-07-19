""" 
keys: 
Solutions:
Similar:
T:
S:
"""

class Solution:
	# https://leetcode.com/problems/number-of-closed-islands/discuss/425122/Python-easy-understand-DFS-solution
	# O(N) for S and T
    def closedIsland(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
        	return 0
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c, val):
        	if 0 <= r < rows and 0 <= c < cols and grid[r][c] == 0:
        		grid[r][c] = val  # flood the land (0s) by water (1s)
        		dfs(r, c+1, val)
        		dfs(r, c-1, val)
        		dfs(r+1, c, val)
        		dfs(r-1, c, val)
        		

        # remove all land connected to the edges using flood fill
        # since there won't be a closed island according to definition
        for r in range(rows):
        	for c in range(cols):
        		if (r == 0 or c == 0 or r == rows-1 or c == cols-1) and grid[r][c] == 0:
        			dfs(r, c, 1)

        # traverse the grid again, find enclosed island and 
        # populate the zeros into ones
        res = 0
        for r in range(rows):
        	for c in range(cols):
        		if grid[r][c] == 0:
        			dfs(r, c, 1)
        			res += 1

        return res
