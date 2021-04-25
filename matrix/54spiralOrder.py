'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # the best solution
    def spiralOrder2(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]: 
            return res
        
        startRow = 0; endRow = len(matrix) - 1 # those are reachable idx
        startCol = 0; endCol = len(matrix[0]) - 1
        direction = 0
        
        while startRow <= endRow and startCol <= endCol:
            # right direction
            if direction == 0: 
                for col in range(startCol, endCol+1):
                    res.append(matrix[startRow][col])
                startRow += 1
            # down
            if direction == 1: 
                for row in range(startRow, endRow+1):
                    res.append(matrix[row][endCol])
                endCol -= 1
            # left
            if direction == 2:
                for col in range(endCol, startCol-1, -1):
                    res.append(matrix[endRow][col])
                endRow -= 1
            # up
            if direction == 3: 
                for row in range(endRow, startRow-1, -1):
                    res.append(matrix[row][startCol])
                startCol += 1
            direction =(direction + 1) % 4
        return res
        
        
    
    
    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:
        res = []
        if not matrix or not matrix[0]: return res
        
        rowBegin = 0; rowEnd = len(matrix) - 1
        colBegin = 0; colEnd = len(matrix[0]) - 1
        
        while rowBegin <= rowEnd and colBegin <= colEnd:
            # traverse right
            for j in range(colBegin, colEnd+1):
                res.append(matrix[rowBegin][j])
            rowBegin += 1 # goes to lower row
            # traverse down
            for j in range(rowBegin, rowEnd+1):
                res.append(matrix[j][colEnd])
            colEnd -= 1 # goes to left col
            # traverse left
            for j in range(colEnd, colBegin-1, -1):
                res.append(matrix[rowEnd][j])
            rowEnd -= 1 # goes to upper row
            # traverse right
            for j in range(rowEnd, rowBegin-1, -1):
                res.append(matrix[j][colBegin])
            colBegin += 1
            
        return res[:len(matrix)*len(matrix[0])] # prevent duplicates
            
        
    
    # not recommend since pop(0)
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ret = []
        while matrix:
            ret += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    ret.append(row.pop())
            if matrix:
                ret += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for row in matrix[::-1]:
                    ret.append(row.pop(0))
        return ret

    # def spiralOrder(self, matrix):
    #     return matrix and [*matrix.pop(0)] + \
    #            self.spiralOrder([*zip(*matrix)][::-1])

obj=Solution()
print(obj.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12],
  [13,14,15,16]
]))
