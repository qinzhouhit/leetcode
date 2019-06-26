# class Solution:
#     def subsetsWithDup(self, nums):
#         res=[[]]
#         nums.sort()
#         for i in range(len(nums)):
#             if i == 0 or nums[i] != nums[i - 1]:
#                 l = len(res)
#             for j in range(len(res) - l, len(res)):
#                 res.append(res[j] + [nums[i]])
#         return res

class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        res=[]; tmp=[]
        self.helper(res, tmp, 0, nums)
        return res

    def helper(self, res, tmp, start, nums):
        res.append(tmp)
        for i in range(start, len(nums)):
            if i!=start and nums[i]==nums[i-1]:
                continue
            tmp.append(nums[i])
            self.helper(nums, tmp, i+1, nums)
            tmp.pop()

obj=Solution()
print (obj.subsetsWithDup([1,2,2]))

# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]
