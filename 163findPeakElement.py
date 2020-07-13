'''keys: Solutions:Similar: T:S:'''from typing import Listclass Solution:    # iterative; O(logN) for T and O(1) for S    def findPeakElement2(self, nums: List[int]) -> int:        l, r = 0, len(nums)-1        while l < r:            mid = l + (r-l)//2            if nums[mid] > nums[mid+1]:                r = mid            else:                l = mid + 1        return l                     # recursive binary search    # O(logN) for S and T, N as the size of nums; S: stack depth    '''    why binary search works here:    Lets say you have a mid number at index x, nums[x]; if (num[x+1] > nums[x]),    that means a peak element HAS to exist on the right half of that array,     because (since every number is unique) 1. the numbers keep increasing on     the right side, and the peak will be the last element. 2. the numbers     stop increasing and there is a 'dip', or there exists somewhere a     number such that nums[y] < nums[y-1], which means number[x] is a peak     element.    This same logic can be applied to the left hand side (nums[x] < nums[x-1]).    '''    def findPeakElement1(self, nums: List[int]) -> int:        return self.helper(nums, 0, len(nums)-1)    def helper(self, nums, l, r):        if l == r:            return l        mid = l + (r-l)//2        if nums[mid] > nums[mid+1]: # descending subsequence            return self.helper(nums, l, mid) # search the left part (where the peak at)        else: # the peak is at the right part            return self.helper(nums, mid+1, r)                # linear scan    # O(N) for T and O(1) for S    def findPeakElement(self, nums: List[int]) -> int:        for i in range(len(nums)-1):            if nums[i] > nums[i+1]:                return i        return len(nums) - 1        