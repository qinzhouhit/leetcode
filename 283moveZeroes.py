'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # T: O(n); S: O(1)
    def moveZeroes(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        if not any(nums):
            return None

        zero_ind = 0
        for i in range(len(nums)):
            if nums[i] != 0:
                nums[i], nums[zero_ind] = nums[zero_ind], nums[i]
                zero_ind += 1


    def moveZeroes1(self, nums):
        if not any(nums):
            return None

        zero_ind = 0
        for num in nums:
            if num != 0:
                nums[zero_ind] = num
                zero_ind += 1
        while zero_ind < len(nums):
            nums[zero_ind] = 0
            zero_ind += 1
        # print (nums)


obj = Solution()
obj.moveZeroes1([3,2,1,5,0,6,8,0])
