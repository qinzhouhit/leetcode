'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
#     def subsets(self, nums):
#         ret = [[]]
#         for n in nums:
#             ret += [r + [n] for r in ret]
#         return ret

    # def subsets(self, nums):
    #     all_subsets = [[]]
    #     if not nums:
    #         return all_subsets
    #     for num in nums:
    #         for idx in range(len(all_subsets)):
    #             all_subsets.append(all_subsets[idx]+[num])
    #     return all_subsets

    # TODO: backtracking
    def subsets(self, nums):
        res=[]; tmp=[]
        self.helper(res, tmp, 0, nums)
        return res
    def helper(self, res, tmp, start, nums):
        res.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(i)
            self.helper(res, tmp, i+1, nums)
            tmp.pop()

obj=Solution()
print(obj.subsets([1,2,3]))
