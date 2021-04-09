'''
keys: 
Solutions:
Similar: 41
T:
S:
'''
from typing import List


class Solution:

	# O(N) for T and O(1) for S
	def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
                
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        idx = 1
        # find idx such that 
        # missing(idx - 1) < k <= missing(idx)
        while missing(idx) < k:
            idx += 1
        
        # kth missing number is greater than nums[idx - 1]
        # and less than nums[idx]
        return nums[idx - 1] + k - missing(idx - 1)



    # binary search
    # T: O(logN); S: O(1)
    def missingElement(self, nums: List[int], k: int) -> int:
        # Return how many numbers are missing until nums[idx]
        missing = lambda idx: nums[idx] - nums[0] - idx
            
        n = len(nums)
        # If kth missing number is larger than 
        # the last element of the array
        if k > missing(n - 1):
            return nums[-1] + k - missing(n - 1) 
        
        left, right = 0, n - 1
        # find left = right index such that 
        # missing(left - 1) < k <= missing(left)
        while left <= right:
            pivot = left + (right - left) // 2
            
            if missing(pivot) < k:
                left = pivot + 1
            else:
                right = pivot - 1
        
        # kth missing number is greater than nums[left - 1]
        # and less than nums[left], or use right, it's the same
        # since left = right + 1 when breaks out the while loop
        return nums[left - 1] + k - missing(left - 1) 



	# TLE
    def missingElement(self, nums: List[int], k: int) -> int:
    	tmp = list(range(min(nums), max(nums)))
        residue = list(set(tmp) - set(nums))
        if k-1 <= len(residue):
            return sorted(residue)[k-1]
        else:
            return max(nums) + k - len(residue)