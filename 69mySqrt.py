'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from math import e, log

class Solution:
    # Newton method, iteration
    # T: O(logN); S: O(1), fastest
    # define that error should be less than 1 and proceed iteratively.
    # x_1 = (x_0 + x/x_0) / 2
    def mySqrt4(self, x):
        if x < 2:
            return x
        
        x0 = x
        x1 = (x0 + x / x0) / 2
        while abs(x0 - x1) >= 1:
            x0 = x1
            x1 = (x0 + x / x0) / 2        
            
        return int(x1)
    
    
    
    # concise Newton one
    def mySqrt3(self, x):
        r = x
        while r * r > x:
            r = int((r + x/r) / 2)
        return r
    
    
    # binary search
    # T: O(logN); S: O(1)
    def mySqrt2(self, x):
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            pivot = left + (right - left) // 2
            num = pivot * pivot
            if num > x:
                right = pivot -1
            elif num < x:
                left = pivot + 1
            else:
                return pivot
            
        # the while loop breaks when left > right, so it returns right
        # it's the same as left-1, since before it, left==right
        return right 
    
    
    # pocket calculator 
    # sqrt(x) = e^(0.5*logx)
    # O(1) for S and T
    def mySqrt1(self, x):
        if x < 2:
            return x
        # default log: log_e
        left = int(e**(0.5 * log(x)))
        right = left + 1 # dealing with decimal, e.g., sqrt(8)=2.8...
        return left if right * right > x else right

obj=Solution()
print(obj.mySqrt(10))

