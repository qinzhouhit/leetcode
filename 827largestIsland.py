'''
keys:
Solutions:
Similar:
T:
S:
'''
from collections import deque


class Solution:
    # official
    # T: O(N^4), S: O(N^2)
    def largestIsland(self, grid: List[List[int]]) -> int:
        n = len(grid)

        def helper(r, c):
            stack = [(r, c)]
            seen = {(r, c)}
            while stack:
                r1, c1 = stack.pop()
                for dr, dc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                    nr = r1 + dr; nc = c1 + dc
                    if (nr, nc) not in seen and 0 <= nr < len(grid) and 0 <= nc < len(grid) and grid[nr][nc]:
                        stack.append((nr, nc))
                        seen.add((nr, nc))
            return len(seen)

        res = float("-inf")
        hasZero = False
        for r in range(n):
            for c in range(n):
                if grid[r][c] == 0:
                    hasZero = True
                    grid[r][c] = 1
                    area = helper(r, c)
                    res = max(res, area)
                    grid[r][c] = 0
        return res if hasZero else n*n


    # https://leetcode.com/problems/making-a-large-island/discuss/127032/C%2B%2BJavaPython-Straight-Forward-O(N2)-with-Explanations
    def largestIsland1(self, grid: List[List[int]]) -> int:
    	N = len(grid)

        def move(x, y):
            for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                if 0 <= x + i < N and 0 <= y + j < N:
                    yield x + i, y + j

        def dfs(x, y, index):
            res = 0
            grid[x][y] = index
            for i, j in move(x, y):
                if grid[i][j] == 1:
                    res += dfs(i, j, index)
            return res + 1

        # DFS every island and give it an index of island
        index = 2
        areas = {0: 0}
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 1:
                    areas[index] = dfs(x, y, index)
                    index += 1

        # traverse every 0 cell and count biggest island it can conntect
        res = max(areas.values())
        for x in range(N):
            for y in range(N):
                if grid[x][y] == 0:
                    possible = set(grid[i][j] for i, j in move(x, y))
                    res = max(res, sum(areas[index] for index in possible) + 1)
        return res








