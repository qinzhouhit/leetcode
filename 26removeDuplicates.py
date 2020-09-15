'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # official, two pointer, T: O(N), S: O(1)
    def removeDuplicates1(self, nums: List[int]) -> int:
        l = 0
        for r in range(1, len(nums)):
            if nums[r] != nums[l]:
                l += 1
                nums[l] = nums[r]
        return l + 1
    
    
    def removeDuplicates(self, nums: List[int]) -> int:
        ind = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[ind]:
                ind += 1
                nums[ind] = nums[i]
        for i in range(ind+1, len(nums)):
            nums.pop(-1)
        return len(nums)

obj=Solution()
print (obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
