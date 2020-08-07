'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # bfs    # O(n^2) for S and T    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:        n = len(grid)        if grid[0][0] or grid[n-1][n-1]: return -1        q = [(0, 0, 1)]        for r, c, d in q:            if r == n-1 and c == n-1: return d            for x, y in ((r-1,c-1),(r-1,c),(r-1,c+1),(r,c-1),(r,c+1),\                         (r+1,c-1),(r+1,c),(r+1,c+1)):                if 0 <= x < n and 0 <= y < n and not grid[x][y]:                    grid[x][y] = 1 # mark as visited                    q.append(x, y, d+1)        return -1