'''
keys:
Solutions:
Similar:
T:
S:
'''


class Solution:
    """
    @param: nums: An ineger array
    @return: An integer
    """
    def removeDuplicates(self, nums):
        # write your code here
        # if not nums:
        #     return 0
        # else:
        #     return len(list(set(nums)))
        i = 0
        while i < len(nums) - 1:
            if nums[i+1] == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)


obj = Solution()
obj.removeDuplicates([1,2,2,3,4])
