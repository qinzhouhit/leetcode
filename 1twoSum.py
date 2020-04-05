'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution(object):
    def twoSum(self, nums, target):
        if len(nums) <= 1:
            return False
        buff_dict = {}
        for i in range(len(nums)):
            if nums[i] in buff_dict:
                return [buff_dict[nums[i]], i]
            else:
                buff_dict[target - nums[i]] = i

obj=Solution()
nums=[2,7,11,15]
target=10
obj.twoSum(nums, target)


