'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    def sortColors(self, nums):
        """
        Do not return anything, modify nums in-place instead.
        """
        l,r=0,len(nums)-1
        for i in range(len(nums)):
            while nums[i]==2 and i<r:
                tmp=nums[i]
                nums[i]=nums[r]
                nums[r]=tmp
                r-=1
            while nums[i]==0 and i>l:
                tmp=nums[i]
                nums[i]=nums[l]
                nums[l]=tmp
                l+=1
        print (nums)

obj=Solution()
print(obj.sortColors([1,2,0]))
