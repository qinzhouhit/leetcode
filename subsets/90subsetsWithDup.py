'''
keys:
Solutions:
Similar: 78 (distinct nums)
90: duplicate nums
T:
S:
'''
from typing import List

# class Solution:



class Solution:
    # educative.io, bfs
    # O(N*2^N) for S and T
    def subsetsWithDup4(self, nums):
        nums.sort()
        subsets = [[]]
        start, end = 0, 0
        for i in range(len(nums)):
            start = 0
            # if current and the previous elements are same, create new subsets 
            # only from the subsets added in the previous step
            if i > 0 and nums[i] == nums[i-1]:
                print (start, end, subsets)
                start = end
            end = len(subsets)
            for j in range(start, end):
                tmp = list(subsets[j])
                tmp.append(nums[i])
                subsets.append(tmp)
        return subsets
             

    #####
    # recommended, just skip repeated element
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
            
    #####
    # self-made, based on subsets
    def subsetsWithDup2(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        nums.sort() # essential
        self.dfs(nums, [], 0)
        return self.res
    
        
    def dfs(self, nums, path, idx):
        if path not in self.res:
            self.res.append(path[:])
            
        for i in range(idx, len(nums)):
            path.append(nums[i])
            self.dfs(nums, path, i + 1)
            path.pop()

    #####
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
    
    #####
    def subsetsWithDup3(self, nums):
        res=[[]]
        nums.sort()
        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i - 1]:
                l = len(res)
            for j in range(len(res) - l, len(res)):
                res.append(res[j] + [nums[i]])
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
