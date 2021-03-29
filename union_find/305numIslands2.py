'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



# union find
# T: O(L + m*n), O(m*n) for union find initialization, O(L) to process positions
# S: O(m*n)
# https://leetcode.com/problems/number-of-islands-ii/discuss/75459/JavaPython-clear-solution-with-UnionFind-Class-(Weighting-and-Path-compression)
# if the map is very big, then the initialization of the arrays can cost a 
# lot of time when mn is much larger than N. In this case we should consider
# using a hashmap/dictionary for the underlying data structure to avoid this overhead.
class DSU:
	def __init__(self): 
		self.id = {} # k: (r,c) of the point, v: its root
		self.size = {}
		self.count = 0 # number of connected components

	def add(self, p): # p here is the tuple (r, c)
		self.id[p] = p
		self.size[p] = 1
		self.count += 1

	def find(self, x): # find root, path compression
		while x != self.id[x]: # WHILE!!!
			self.id[x] = self.id[self.id[x]]
			x = self.id[x]
		return x

	def union(self, a, b): # optimized version, making smaller one part of bigger one
	# union by rank
		ra, rb = self.find(a), self.find(b)
		if ra == rb:
			return # in the same set
		if self.size[ra] > self.size[rb]:
			ra, rb = rb, ra # making a the flat one
		self.id[ra] = rb # making a part of b
		self.size[rb] += self.size[ra] # 
		self.count -= 1

class Solution:
	def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
		res = []
		islands = DSU()
		for p in map(tuple, positions):
			if p in islands.id: # repeated island
				res += [islands.count]
			else:
				islands.add(p)
				for dt in [(0,1), (0,-1), (1,0), (-1,0)]:
					q = (p[0] + dt[0], p[1] + dt[1]) # new point
					if q in islands.id:
						islands.union(p, q)
				res += [islands.count]
		return res



class Solution:
	# TLE: T: O(L * m * n), L as number of positions. 
	# S: O(m * n)
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        res = []
        grid = [["0"] * n for _ in range(m)]
        for r, c in positions:
            grid[r][c] = "1"
            tmp = copy.deepcopy(grid)
            res.append(self.numIslands200(tmp))
        return res

    def numIslands200(self, grid: List[List[str]]) -> int:
        if not any(grid):
            return 0

        ct = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    ct += 1
                    self.dfs(grid, i, j) # dfs here only marks all the connected 1s visited
        return ct

    def dfs(self, grid, i, j):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]) or grid[i][j] != "1":
            return
        grid[i][j] = "#"
        self.dfs(grid, i+1, j)
        self.dfs(grid, i-1, j)
        self.dfs(grid, i, j+1)
        self.dfs(grid, i, j-1)



