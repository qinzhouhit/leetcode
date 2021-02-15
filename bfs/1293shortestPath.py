'''
keys: for each step, we always choose the path with least obstacles to deal with
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import deque


class Solution:

	# ACed
	# https://leetcode.com/problems/shortest-path-in-a-grid-with-obstacles-elimination/discuss/451832/Python-Short-BFS-Solution
	def shortestPath1(self, grid: List[List[int]], k: int) -> int:
		m, n = len(grid), len(grid[0])
        queue = collections.deque([[0, 0, 0]])    # row, col, num of obstables met so far
        visited = {(0, 0): 0}                 # row, col   =>   num of obstables met so far
        steps = 0
        
        while queue:
            for _ in range(queue): # cur layer of bfs
                r, c, obs = queue.popleft()
                if obs > k: # run out of elimination quote
                	continue
                if r == m - 1 and c == n - 1: 
                    return steps
                for nr, nc in [(r+1, c), (r-1, c), (r, c+1), (r, c-1)]:
                    if 0 <= nr < m and 0 <= nc < n:
                        next_obs = obs + 1 if grid[nr][nc] == 1 else obs
                        # > If having smaller obstacles eliminated, then we continue with the case/path 
                        # with fewer obstacles, since we have more quota left for future elimination
                        # > We enqueue a neighbor if we have not visited it before or we 
                        # visited it before with less quota remaining. 
                        # > Greedy here, i.e., using eliminate when we see obstacle
                        # > We only care about cases regarding steps to reach target instead of number of
                        # different paths.
                        if next_obs < visited.get((nr, nc), float('inf')):
                            visited[(nr, nc)] = next_obs # for next layer of bfs
                            queue.append([nr, nc, next_obs])
            steps += 1 # for each layer of expansion (advancing to next layer)
        return -1




	# TLE
	# O(m*n*k) for S and T, m as rows, n as cols
	# for every cell (m*n), worst case we put the cell into the queue/bfs k times
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
    	rows, cols = len(grid), len(grid[0])
        if rows == 1 and cols == 1:
        	return 0 # only one cell

        queue = deque([(0, 0, k, 0)]) # r-idx, c-idx, elimination unused, steps so far
        visited = set([(0, 0, k)]) # if visit seen cell, the steps will be larger

        if k > rows - 1 + cols - 1: # we can just take the diagonal
        	return rows - 1 + cols - 1 # by eliminating all obstacles on the diagoal

        while queue:
        	r, c, eli_residue, steps = queue.popleft()
        	for nr, nc in [(r-1, c), (r+1, c), (r, c-1), (r, c+1)]: # new_r
        		if 0 <= nr < rows and 0 <= nc < cols:
        			if grid[nr][nc] == 1 and eli_residue > 0 and (nr, nc, eli_residue-1) not in visited:
        				visited.add((nr, nc, eli_residue))
        				queue.append((nr, nc, eli_residue-1, steps+1))
        			# two ifs are sequential, since the case we can eliminate the cell and visit it
        			if grid[nr][nc] == 0 and (nr, nc, eli_residue) not in visited:
        				if nr == rows-1 and nc == cols-1:
        					return steps + 1
        				visited.add((nr, nc, eli_residue)) # not using elimination
        				queue.append((nr, nc, eli_residue, steps+1))
        return -1



