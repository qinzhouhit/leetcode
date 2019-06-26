# import collections
# class Solution:
#     def removeDuplicates(self, nums):
#         count=collections.defaultdict(int)
#         for i in range(len(nums)):
#             count[nums[i]]+=1
#             if count[nums[i]]>2:
#                 nums[i]=-1
#         nums.remove(-1)
#         return nums


class Solution:
    def removeDuplicates(self, nums):
        i=0
        for num in nums:
            if i < 2 or num > nums[i-2]:
                nums[i] = num
                i += 1
        return i

obj=Solution()
print(obj.removeDuplicates([1,1,1,2,2,3]))
