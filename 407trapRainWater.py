'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
The idea is that we maintain all the points of the current border in a min heap 
and always choose the point with the lowest length. This is actually an optimized
 searching strategy over the trivial brute force method: instead of dfs each point
  to find the lowest "border" of its connected component, we can always start a
   search from the lowest border and update the points adjacent to it.
https://leetcode.com/problems/trapping-rain-water-ii/discuss/89472/Visualization-No-Code
'''
class Solution:
	def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or not heightMap[0]:
            return 0
        
        import heapq    
        m, n = len(heightMap), len(heightMap[0])
        heap = []
        visited = [[0]*n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m-1 or j == n-1:
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1
        
        result = 0
        curMax = float("-inf")
        while heap:
            height, i, j = heapq.heappop(heap)  
            curMax = max(height, curMax)
            for x, y in ((i+1, j), (i-1, j), (i, j+1), (i, j-1)):
                if 0 <= x < m and 0 <= y < n and not visited[x][y]:
                	if curMax > heightMap[x][y]:
                    	result += curMax - heightMap[x][y] # only when curMax > heightMap[x][y]
                    heapq.heappush(heap, (heightMap[x][y], x, y))
                    visited[x][y] = 1
        return result
