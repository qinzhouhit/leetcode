class Solution:
	def numIslands(self, grid):
		if not any(grid):
			return 0

		ct = 0
		for i in range(len(grid)):
			for j in range(len(grid[0])):
				if grid[i][j] == 1:
					self.dfs(grid, i, j)
					ct += 1
		return ct

	def dfs(self, grid, i, j):
		if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != 1:
			return
		grid[i][j] = "#"
		self.dfs(grid, i+1, j)
		self.dfs(grid, i-1, j)
		self.dfs(grid, i, j+1)
		self.dfs(grid, i, j-1)

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
