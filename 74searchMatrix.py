'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # binary search, T: O(log(MN)); S: O(1)
    def searchMatrix(self, matrix, target):
        if not matrix:
            return False
        
        row, col=len(matrix), len(matrix[0])
        l, r = 0, row*col
        while l < r:
            mid = l + (r - l)//2 
            val = matrix[mid // col][mid % col]
            if target > val:
                l = mid+1
            elif target < val:
                r = mid
            else: # target == val
                return True
        return False


obj=Solution()
print(obj.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,50]], 13))
