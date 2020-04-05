'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def nextPermutation(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        len_, pivot = len(nums), -1
        for i in reversed(range(len_-1)):
            if nums[i+1] > nums[i]:
                pivot = i
                break
        if pivot != -1:
            s = -1
            for i in reversed(range(pivot+1, len_)):
                if nums[i] > nums[pivot]:
                    s = i
                    break
            tmp = nums[pivot]
            nums[pivot], nums[s] = nums[s], tmp
            nums[pivot+1:] = reversed(nums[pivot+1:])
        else:
            nums.sort()

obj=Solution()
print (obj.nextPermutation([1,2,3]))
