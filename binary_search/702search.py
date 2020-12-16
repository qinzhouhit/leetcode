'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

# """
# This is ArrayReader's API interface.
# You should not implement it, or speculate about its implementation
# """
#class ArrayReader:
#    def get(self, index: int) -> int:


'''
An efficient way to find the proper bounds is to start at the beginning of the array 
with the bound’s size as ‘1’ and exponentially increase the bound’s size (i.e., 
double it) until we find the bounds that can have the key.
'''

class Solution:
    # T: O(logT), where T is an index of target value.
    # 2^k < T <= 2^(k+1) That means one needs k=logT steps to setup the boundaries
    # S: O(1)
    def search(self, reader, target):
        """
        :type reader: ArrayReader
        :type target: int
        :rtype: int
        """
        l, r = 0, 1
        # expanding the search range exponentially 
        while reader.get(r) < target:
        	newL = r + 1
        	r += (r - l + 1) * 2
        	l = newL
        return self.helper(reader, target, l, r)

    def helper(self, reader, target, l, r):
    	while l <= r:
    		mid = l + (r - l) // 2
    		if target < reader.get(mid):
    			r = mid - 1
    		elif target > reader.get(mid):
    			l = mid + 1
    		else:
    			return mid
    	return -1


    # official lc one
    def search1(self, reader, target):
        if reader.get(0) == target:
            return 0
        
        # search boundaries
        left, right = 0, 1
        while reader.get(right) < target:
            left = right
            right <<= 1
        
        # binary search
        while left <= right:
            pivot = left + ((right - left) >> 1)
            num = reader.get(pivot)
            
            if num == target:
                return pivot
            if num > target:
                right = pivot - 1
            else:
                left = pivot + 1
        # there is no target element
        return -1











