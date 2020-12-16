'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
    # binary search; T: O(logN), S: O(1)
    def searchRange2(self, nums: List[int], target: int) -> List[int]:
        def helper(nums, target, findMaxIdx):
            keyIdx = -1
            l, r = 0, len(nums) - 1
            while l <= r:
                mid = l + (r-l) // 2
                if target < nums[mid]:
                    r = mid - 1
                elif target > nums[mid]:
                    l = mid + 1
                else:
                    keyIdx = mid
                    if findMaxIdx:
                        l = mid + 1 # search ahead to find the last index of 'key'
                    else:
                        r = mid - 1 # search behind to find the first index of 'key'
            return keyIdx

        res = [-1, -1]
        res[0] = helper(nums, target, False)
        if res[0] != -1:
            res[1] = helper(nums, target, True)
        return res




    # linear scan, O(n) for T and O(1) for S 
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            if nums[i] == target:
                left_idx = i
                break # break the fore loop
        # if the for loop breaks, then the ELSE will not be excuted
        else: # finishes the for loop and jumps to the ELSE
            return [-1, -1]

        for j in range(len(nums)-1, -1, -1):
            if nums[j] == target:
                right_idx = j
                break
        return [left_idx, right_idx]




    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(lo, hi):
            if nums[lo] == target == nums[hi]:
                return [lo, hi]
            if nums[lo] <= target <= nums[hi]:
                mid = (lo + hi) // 2
                l = search(lo, mid)
                r = search(mid+1, hi)
                return max(l, r) if -1 in l + r else [l[0], r[1]]
            return [-1, -1]
        return search(0, len(nums)-1)

obj=Solution()
print (obj.searchRange([], 0))
