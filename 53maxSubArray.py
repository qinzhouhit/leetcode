'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    #####
    # dp, T: O(N); S: O(1)
    def maxSubArray(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i]+=nums[i-1]
        return max(nums)
    
    #####
    # divide and conquer
    def cross_sum(self, nums, left, right, p): 
            if left == right:
                return nums[left]

            left_subsum = float('-inf')
            curr_sum = 0
            for i in range(p, left - 1, -1):
                curr_sum += nums[i]
                left_subsum = max(left_subsum, curr_sum)

            right_subsum = float('-inf')
            curr_sum = 0
            for i in range(p + 1, right + 1):
                curr_sum += nums[i]
                right_subsum = max(right_subsum, curr_sum)

            return left_subsum + right_subsum   
    
    def helper(self, nums, left, right): 
        if left == right:
            return nums[left]
        
        p = (left + right) // 2
            
        left_sum = self.helper(nums, left, p)
        right_sum = self.helper(nums, p + 1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
        
    def maxSubArray1(self, nums: 'List[int]') -> 'int':
        return self.helper(nums, 0, len(nums) - 1)
    
    

obj=Solution()
print (obj.maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))
