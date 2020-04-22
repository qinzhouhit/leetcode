'''
keys: store information at the first element of each columns and rows.
If a column contains a 0, it's first element will be 0. Same for rows.
Solutions:
Similar:
T:
S: O(1)
'''

class Solution:
    def setZeroes(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        isZeroCol, isZeroRow=False, False
        row_, col_=len(matrix), len(matrix[0])
        # However, both first column and first row use matrix[0][0]
        # which is problematic so she creates another variable for first column,
        # col0. So we consider first row and col separately
        for i in range(0,row_): # check first column
            if matrix[i][0]==0:
                isZeroCol=True
                break

        for j in range(0,col_): # check first row
            if matrix[0][j]==0:
                isZeroRow=True
                break

        for i in range(1, row_): # check except 1st col and row
            for j in range(1, col_):
                if matrix[i][j]==0:
                    matrix[i][0]=0
                    matrix[0][j]=0

        for i in range(1, row_): # process except 1st col and row
            for j in range(1, col_):
                if matrix[i][0]==0 or matrix[0][j]==0:
                    matrix[i][j]=0

        if isZeroCol: # handle 1st col
            for i in range(0, row_):
                matrix[i][0]=0

        if isZeroRow: # handle 1st row
            for i in range(0, col_):
                matrix[0][i]=0
        # print (matrix)

obj=Solution()
print(obj.setZeroes([
  [0,1,2,0],
  [3,4,0,2],
  [1,3,1,5]
]))

