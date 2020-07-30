'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
#class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:

class Solution:
    # O(N+M) for T, O(1) for S
    # Start at Top Right, Move Only Left and Down
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()

        # Set pointers to the top-right corner.
        current_row = 0
        current_col = cols - 1

        # Repeat the search until it goes off the grid.
        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        # If we never left the last column, it must have been all 0's.
        return current_col + 1 if current_col != cols - 1 else -1



    # binary search
    # O(NlogM) for T and O(1) for S
    def leftMostColumnWithOne1(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest = cols
        for row in range(rows):
            l, h = 0, cols-1
            while l < h: # search until l == h
                mid = l + (h-l)//2
                if binaryMatrix.get(row, mid) == 0:
                    l = mid + 1
                else:
                    h = mid
            if binaryMatrix.get(row, l) == 1:
                smallest = min(smallest, cols)
            return -1 if smallest == cols else smallest


    # brute force, TLE
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimensions()
        smallest_index = cols
        # Go through each of the rows.
        for row in range(rows):
            # Linear seach for the first 1 in this row.
            for col in range(cols):
                if binaryMatrix.get(row, col) == 1:
                    smallest_index = min(smallest_index, col)
                    break
        # If we found an index, we should return it. Otherwise, return -1.
        return -1 if smallest_index == cols else smallest_index
