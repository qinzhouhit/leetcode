'''
keys: dijkstra
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:
	# T: O(m*n*log(m*n)), O(m*n) to visit the matrix, O(log(m*n)) to re-sort the heap
	# S: O(m*n) for the heap
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows = len(heights)
        cols = len(heights[0])
        difference_matrix = [[float("inf")]*cols for _ in range(rows)]
        difference_matrix[0][0] = 0
        visited = [[False]*cols for _ in range(rows)]
        heap = [(0, 0, 0)]  # difference, x, y
        while heap:
            difference, x, y = heapq.heappop(heap)
            visited[x][y] = True
            for dx, dy in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
                nx = x + dx # next x and y to visit
                ny = y + dy
                if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                    cur_difference = abs(heights[nx][ny] - heights[x][y])
                    max_difference = max(cur_difference, difference_matrix[x][y])
                    if max_difference < difference_matrix[nx][ny]:
                        difference_matrix[nx][ny] = max_difference
                        heapq.heappush(heap, (max_difference, nx, ny))
        return difference_matrix[-1][-1]