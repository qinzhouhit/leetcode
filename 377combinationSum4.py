'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

import time
class Solution:
    

    # bottom-up dp, improved
    # https://leetcode.com/problems/combination-sum-iv/discuss/85041/7-liner-in-Python-and-follow-up-question
    def combinationSum44(self, nums: List[int], target: int) -> int:
        nums, combs = sorted(nums), [1] + [0] * (target)
        for i in range(target + 1):
            for num in nums:
                if num  > i: 
                    break
                combs[i] += combs[i - num]
        return combs[target]
    
    
    # dp; dp[i]: number of combinations summing to i
    def combinationSum43(self, nums: List[int], target: int) -> int:
        
        nums, combs = sorted(nums), [0] * (target+1)
        for i in range(target + 1):
            for num in nums:
                if num  > i: break
                if num == i: combs[i] += 1
                if num  < i: combs[i] += combs[i - num]
        return combs[target]


    # recursion + memo; TLE
    def combinationSum42(self, nums: List[int], target: int) -> int:
        
        def helper(nums, target):
            if dp[target] != 0:
                return dp[target]
            
            res = 0
            for i in range(len(nums)):
                if target >= nums[i]:
                    res += helper(nums, target - nums[i])
            
            dp[target] = res
            return res
        
        dp = [1] + [0] * target
        return helper(nums, target)

    
    # recursion, TLE
    def combinationSum4(self, nums: List[int], target: int) -> int:
        def dfs(nums, target, path, res):
            if target < 0:
                return
            if target == 0:
                self.res.append(path[:])
            for i in range(len(nums)):
                dfs(nums, target - nums[i], path + [nums[i]], self.res)
            return self.res

        self.res = []
        dfs(nums, target, [], [])
        return len(self.res)
    
    # recursion, TLE
    def combinationSum40(self, nums: List[int], target: int) -> int:
        if target == 0: return 0
        
        res = 0
        for i in range(len(nums)):
            if target >= nums[i]:
                res += self.combinationSum40(nums, target - nums[i])
        return res
        
        

obj = Solution()
print (obj.combinationSum4([1,2,3], 4))

