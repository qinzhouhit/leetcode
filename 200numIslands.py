'''
keys: visit an "1", then explore the all the 1s connected to this 1, mark as visited. ct += 1, go to next 1.
Solutions:
Similar:
T:
S:
'''
from typing import List
import numpy as np

class Solution:
    # T: O(M*N) for S and T, S: stacks
    # https://leetcode.com/problems/number-of-islands/discuss/56340/Python-Simple-DFS-Solution
	def numIslands2(self, grid: List[List[str]]) -> int:
		if not any(grid):
			return 0

		ct = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == "1":
					self.dfs(grid, i, j)
					ct += 1
		return ct

	def dfs(self, grid, i, j):
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
			return
		grid[i][j] = "#"
		# print (i, j)
		# print (np.matrix(grid))
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)
        
    # BFS, T: O(M*N); S: O(min(M, N))
    def numIslands1(self, grid: List[List[str]]) -> int:
        if not any(grid):
            return 0

        res = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    res += 1
                    grid[r][c] == "*"
                    neighbors = deque([(r, c)])
                    while neighbors:
                        r1, c1 = neighbors.popleft()
                        if r1 > 0 and grid[r1-1][c1] == "1":
                            neighbors.append((r1-1, c1))
                            grid[r1-1][c1] = "*"
                        if r1 < rows-1 and grid[r1+1][c1] == "1":
                            neighbors.append((r1+1, c1))
                            grid[r1+1][c1] = "*"
                        if c1 > 0 and grid[r1][c1-1] == "1":
                            neighbors.append((r1, c1-1))
                            grid[r1][c1-1] = "*"
                        if c1 < cols-1 and grid[r1][c1+1] == "1":
                            neighbors.append((r1, c1+1))
                            grid[r1][c1+1] = "*"
        return res
        

tar = [[1, 1, 1, 1, 0],
[1, 1, 0, 1, 0],
[1, 1, 0, 0, 0],
[0, 0, 0, 0, 0]]
tar = [[1, 1, 0, 0, 0],
[1, 1, 0, 0, 0],
[0, 0, 1, 0, 0],
[0, 0, 0, 1, 1]]
obj = Solution()
print (obj.numIslands(tar))
