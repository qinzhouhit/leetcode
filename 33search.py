'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # one-pass binary search
    # T: O(logN); S: O(1)
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high-low)//2
            if target == nums[mid]:
                return mid

            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
    # two-pass binary search, one for finding pivot, one for 
    

obj=Solution()
print (obj.search([4,5,6,7,0,1,2], 0))

