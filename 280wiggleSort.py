'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    """
    @param: nums: A list of integers
    @return: nothing
    """
    def wiggleSort(self, nums):
        # write your code here
        if not nums:
            return None

        for i in range(1, len(nums)):
            if i % 2: # odd index
                should_swap = nums[i] < nums[i-1]
            else:
                should_swap = nums[i] > nums[i-1]

            if should_swap:
                nums[i], nums[i-1] = nums[i-1], nums[i]

        print (nums)


    def wiggleSort1(self, nums):
        # write your code here
        nums.sort()

        for i in range(0, len(nums)-1 , 2):
            nums[i], nums[i+1] = nums[i+1], nums[i]

        print(nums)


obj = Solution()
obj.wiggleSort1([1, 2, 3, 4])
