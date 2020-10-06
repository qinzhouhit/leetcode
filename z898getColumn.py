'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    """
    @param arr: The 2-dimension array
    @return: Return the column the leftmost one is located
    """
    # https://www.lintcode.com/problem/leftmost-one/note/206665
    # make use of the fact that the front part is all 0, the rest is all 1
    def hasOne(self, arr, col):
        return any(  arr[i][col] == 1 for i in range(len(arr))  ) 
    
    def getColumn(self, arr):
        n = len(arr[0])
        start, end = 0, n - 1 
        while start < end:
            mid = (start + end) // 2 
            if self.hasOne(arr, mid):
                end = mid
            else:
                start = mid + 1
        # start found, i.e., the first column with a 1
        return start if self.hasOne(arr, start) else end 
    
    
    # self-made, naive
    def getColumn1(self, arr):
        if not arr:
            return None
            
        res = float("inf")
        for row in arr:
            for c, val in enumerate(row):
                if val:
                    res = min(res, c)
                    
        return res