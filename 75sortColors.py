'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # two pointers, T: O(N); S: O(1)
    def sortColors(self, nums: List[int]) -> None:
        """
        Dutch National Flag problem solution.
        """
        # for all idx < p0 : nums[idx < p0] = 0
        # curr is an index of element under consideration
        p0 = curr = 0
        # for all idx > p2 : nums[idx > p2] = 2
        p2 = len(nums) - 1

        while curr <= p2:
            if nums[curr] == 0:
                nums[p0], nums[curr] = nums[curr], nums[p0]
                p0 += 1
                curr += 1
            elif nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            else:
                curr += 1
                
                # 
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if not nums: return
        l,r = 0,len(nums) - 1
        for i in range(len(nums)):
            while nums[i] == 2 and i < r:
                nums[i], nums[r] = nums[r], nums[i]
                r -= 1
            while nums[i] == 0 and i > l:
                nums[i], nums[l] = nums[l], nums[i]
                l += 1
        print (nums)

obj=Solution()
print(obj.sortColors([1,2,0]))
