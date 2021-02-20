'''
keys: use some tricky algorithm...
Solutions:
Similar:
T:
S:
'''

class Solution:
    # T: O(n), S: O(1)
    # https://leetcode.com/problems/next-permutation/discuss/13867/C%2B%2B-from-Wikipedia
    # https://leetcode.com/problems/next-permutation/discuss/14054/Python-solution-with-comments.
    '''
    if subarray is descending, then impossible to find next permutation
    one has to find a "ascending" number to swap with one number in the descending subarray
    '''
    def nextPermutation1(self, nums: List[int]) -> None:
        i = j = len(nums) - 1
        # until we find i that nums[i-1] < nums[i], all nums to the right of
        # nums[i-1] are sorted in descending order
        while i > 0 and nums[i-1] >= nums[i]: 
            i -= 1 
        if i == 0: # all nums are in descending order
            nums.reverse() # then it is impossible to find next permutation
            return # return the reversed one as required
        k = i - 1 # find the last "ascending" position, when nums[i-1] < nums[i]
        while nums[j] <= nums[k]: 
            j -= 1 # until we have nums[j] > nums[i-1]
        nums[k], nums[j] = nums[j], nums[k] # swap j-th and k-th, wont affect the right subarray being descending
        l, r = k+1, len(nums)-1  # reverse the second part
        while l < r: # reverse the right subarray to make it minimal
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1


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
