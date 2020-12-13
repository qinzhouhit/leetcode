'''
keys: https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # time complexity is O(n x n!) instead of O(n!), since you will have n! permutation.
    # And, for each permutation, you run exact n recursive call to reach it.
    # insert a number into a permutation of size ‘N’ will take O(N)
    # a total of N!N! permutations of a set with ‘N’ numbers
    def permute3(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        self.helper(nums, 0, [])
        return self.res

    def helper(self, nums, idx, cur_perm):
        if idx == len(nums):
            self.res.append(cur_perm[:])
        else:
            for i in range(len(cur_perm)+1):
                new_perm = list(cur_perm)
                new_perm.insert(i, nums[idx])
                self.helper(nums, idx+1, new_perm)


    # educative.io
    # this is actually fast...
    def permute2(self, nums: List[int]) -> List[List[int]]:
        nums_len = len(nums)
        res = []
        perms = deque([[]])
        for num in nums:
            # we will take all existing permutations and add the current number to create 
            # new permutations
            n = len(perms)
            for _ in range(n):
                prev_perm = perms.popleft()
                # create a new permutation by adding the current number at every position
                for j in range(len(prev_perm)+1): # len_+1 positions for len_ length
                    new_perm = list(prev_perm)
                    new_perm.insert(j, num)
                    if len(new_perm) == nums_len:
                        res.append(new_perm)
                    else:
                        perms.append(new_perm)
        return res

        
    # remember this one 
    def permute1(self, nums: List[int]) -> List[List[int]]:
        res = []
        self.dfs(nums, [], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)
            return # backtracking
        for i in range(len(nums)):
            # nums[:i]+nums[i+1:] will be nums excluding i
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)

    # T: see solution
    # S: O(N!), N as then number of elements
    def permute(self, nums: List[int]) -> List[List[int]]:
        self.res = []
        def dfs(nums, tmp):
            if len(path) == len(nums):
                self.res.append(path[:]) # deep copy

            for i in range(len(nums)):
                if nums[i] in path:
                    continue
                path.append(nums[i])
                dfs(nums, path)
                path.pop()
        dfs(nums,[])
        return self.res

obj=Solution()
print(obj.permute([1,2,3]))
