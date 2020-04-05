'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if matrix == None or len(matrix)<1 or len(matrix[0])<1:
            return False
        col_ = len(matrix[0])-1
        row_ = 0
        while col_ >= 0 and row_ <= len(matrix)-1:
            if target == matrix[row_][col_]:
                return True
            elif target < matrix[row_][col_]:
                col_ -= 1
            elif target > matrix[row_][col_]:
                row_ += 1
        return False

a = [[1,4,7,11,15],
[2,5,8,12,19],
[3,6,9,16,22],
[10,13,14,17,24],
[18,21,23,26,30]]

target = 20
obj = Solution()
obj.searchMatrix(a, target)
