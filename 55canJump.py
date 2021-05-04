'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
	# https://leetcode.com/problems/jump-game/discuss/596454/Python-Simple-solution-with-thinking-process-Runtime-O(n)
	# O(n)
    def canJump(self, nums):
        goal = len(nums)-1
        for i in range(len(nums))[::-1]:
        	# notice the nums[i] denotes the MAXIMUM jump length
        	# you can choose the jump length from 0 to nums[i] 
            if i + nums[i] >= goal: 
                goal = i
        return not goal


obj=Solution()
print(obj.canJump([2,3,1,1,4]))
