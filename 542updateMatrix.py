'''
keys:
Solutions:
Similar:
T:
S:
'''

import collections
class Solution:
    # T: O(r*c), S: O(r*c)
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        rows, cols = len(matrix), len(matrix[0])

        queue = collections.deque()
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    queue.append([r, c])
                elif matrix[r][c] == 1:
                    matrix[r][c] = float("inf")

        dirs = [[-1,0], [1,0], [0,-1], [0,1]]

        while queue:
            r, c = queue.popleft()
            for dir in dirs:
                dr = r + dir[0]
                dc = c + dir[1]
                if 0 <= dr < rows and 0 <= dc < cols and \
                    matrix[dr][dc] > 0 and \
                    matrix[dr][dc] > (matrix[r][c] + 1):
                    matrix[dr][dc] = matrix[r][c] + 1
                    queue.append([dr, dc])
        return matrix

            
