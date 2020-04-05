'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def wiggleMaxLength(self, nums):
        if len(nums) == 0:
            return 0

        up = [1] + [0]*(len(nums) - 1)
        down = [1] + [0]*(len(nums) - 1)

        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                up[i] = down[i-1] + 1
                down[i] = down[i-1]
            elif nums[i] < nums[i-1]:
                down[i] = up[i-1] + 1
                up[i] = up[i-1]
            else:
                down[i] = down[i-1]
                up[i] = up[i-1]


        return max(down[-1], up[-1])


obj = Solution()
print (obj.wiggleMaxLength([0, 0]))
