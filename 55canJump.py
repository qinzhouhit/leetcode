'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def canJump(self, nums):
        goal=len(nums)-1
        for i in range(len(nums))[::-1]:
            if i+nums[i]>=goal:
                goal=i
        return not goal


obj=Solution()
print(obj.canJump([2,3,1,1,4]))
