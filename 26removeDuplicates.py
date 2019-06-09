class Solution:
    def removeDuplicates(self, nums):
        ind=0
        for i in range(1, len(nums)):
            if nums[i]!=nums[ind]:
                ind+=1
                nums[ind]=nums[i]
        for i in range(ind+1, len(nums)):
            nums.pop(-1)
        return len(nums)

obj=Solution()
print (obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
