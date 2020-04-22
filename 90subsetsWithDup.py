'''
keys:
Solutions:
Similar: 78 (distinct nums)
90: duplicate nums
T:
S:
'''

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
        res.append(list(tmp))
        for i in range(start, len(nums)):
            # if S[i] is same to S[i - 1], then it needn't to be added to
            # all of the subset, just add it to the last l subsets
            # which are created by adding S[i - 1]
            if i > start and nums[i]==nums[i-1]:
                continue
            tmp.append(nums[i])
            self.helper(res, tmp, i+1, nums)
            tmp.pop()


    def subsetsWithDup1(self, nums):
        if not nums:
            return []
        nums.sort()
        res, cur = [[]], []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                cur = [item + [nums[i]] for item in cur]
            else:
                cur = [item + [nums[i]] for item in res]
            res += cur
        return res

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
