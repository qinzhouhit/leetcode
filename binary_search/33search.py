'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # advanced version, where duplicates in nums
    def search2(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid
        # the only difference from the previous solution,
        # if numbers at indexes start, mid, and end are same, we can't choose a side
        # the best we can do, is to skip one number from both ends as key != arr[mid]
            if nums[l] == nums[mid] == nums[r]:
                l += 1
                r -= 1
            if nums[l] <= nums[r]: # left side is ascending
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else: # target > nums[mid]
                    l = mid + 1
            else: # right side is ascending
                if nums[mid] <= target <= nums[r]: # dealing with right side
                    l = mid + 1
                else: # target > nums[r]
                    r = mid - 1
        return -1


    # one-pass binary search
    # T: O(logN); S: O(1)
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            if target == nums[mid]:
                return mid

            if nums[l] <= nums[r]: # left side is ascending
                if nums[l] <= target <= nums[mid]:
                    r = mid - 1
                else: # target > nums[mid]
                    l = mid + 1
            else: # right side is ascending
                if nums[mid] <= target <= nums[r]: # dealing with right side
                    l = mid + 1
                else: # target > nums[r]
                    r = mid - 1
        return -1

    
    # two-pass binary search, one for finding pivot, one for search in subarray
    def search1(self, nums: List[int], target: int) -> int:
        n = len(nums)
        if n == 1:
            return 0 if nums[0] == target else -1

        def find_rotate_idx(l, r):
            if nums[l] < nums[r]: # whole array ascending
                return 0 
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else: 
                    if nums[mid] < nums[l]: # peak at left part
                        r = mid - 1
                    else:
                        l = mid + 1

        def helper(l, r):
            while l <= r:
                mid = l + (r - l) // 2
                if nums[mid] == target:
                    return mid
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    r = mid - 1
            return -1

        rotate_idx = find_rotate_idx(0, n-1)
        if nums[rotate_idx] == target:
            return rotate_idx
        if rotate_idx == 0:
            return helper(0, n-1)
        if target < nums[0]:
            return helper(rotate_idx, n-1)
        else:
            return helper(0, rotate_idx)

    

obj=Solution()
print (obj.search([4,5,6,7,0,1,2], 0))

