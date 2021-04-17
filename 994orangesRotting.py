'''
keys:
Solutions:
Similar:
T:
S:
'''

import collections
class Solution:
    # BFS: since you have to explore all neighbors first
    # T: O(N), N as size of grid
    # S: O(N), for queue, worst case (full of rotten oranges)
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = collections.deque()

        # build the initial set of rotten oranges
        fresh_ = 0
        rows, cols = len(grid), len(grid[0])
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    q.append((r, c))
                elif grid[r][c] == 1:
                    fresh_ += 1
        # mark the timestamp
        q.append((-1, -1))
        # start the rotting process via BFS
        minutes = -1 # since we have (-1, -1)
        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        while q:
            r, c = q.popleft()
            if r == -1: # We finish one round/level of processing
                minutes += 1
                if q: # (-1,-1) to separate different levels
                    # to avoid the endless loop
                    q.append((-1,-1))
            else: # rotten orange
                for d in directions:
                    neighbor_row, neighbor_col = r + d[0], c + d[1]
                    if 0 <= neighbor_row < rows and 0 <= neighbor_col < cols:
                        if grid[neighbor_row][neighbor_col] == 1:
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_ -= 1
                            q.append((neighbor_row, neighbor_col))
        return minutes if fresh_ == 0 else -1


    def orangesRotting1(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        q = collections.deque()

        fresh = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1: 
                    fresh += 1
                elif grid[r][c] == 2: 
                q.append((r, c)) # as starting point

        directions = [(-1,0), (0,1), (1,0), (0,-1)]
        minutes = 0
        while q and fresh:
            size = len(q) # how many nodes to expand
            while size:
                size -= 1
                r, c = q.popleft()
                for d in directions:
                    dx = r + d[0]; dy = c + d[1]
                    if (0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1):
                        fresh -= 1
                        grid[dx][dy] = 2
                        q.append((dx, dy))
            minutes += 1
        return minutes if not fresh else -1


					












