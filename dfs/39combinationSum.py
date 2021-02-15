'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
    # T: O(N^(T/M + 1)), T as target, M as min val of candidates, 
    # N as number of candidates
    # S: O(T/M) for the recursion stack, i.e., height of tree
    '''
    The execution of the backtracking is unfolded as a DFS traversal in a n-ary tree
    The total number of steps during the backtracking would be the number of nodes in the tree.
    The time complexity is linear to the number of nodes of the execution tree.
    
    The fan-out of each node would be bounded to N
    The maximal depth of the tree, would be T/M
    The maximal number of nodes in N-ary tree of depth T/M: N^(T/M + 1)
    '''
    # >>> dfs
    def combinationSum(self, candidates, target):
        res = []
        candidates.sort()
        self.dfs(candidates, target, 0, [], res)
        return res

    def dfs(self, nums, target, index, path, res):
        if target < 0:
            return  # backtracking
        if target == 0:
            res.append(path)
            return 
        for i in range(index, len(nums)):
            self.dfs(nums, target-nums[i], i, path+[nums[i]], res)


    # >>> typical version, no sort
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:

        def dfs(residue, idx, comb):
            if residue < 0:
                return
            if residue == 0:
                res.append(comb[:])
            for i in range(idx, len(candidates)):
                comb.append(candidates[i])
                dfs(residue - candidates[i], i, comb)
                comb.pop()

        res = []
        dfs(target, 0, [])
        return res

        



    # >>> self-made
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        def dfs(residue, idx, path):
            if residue < 0:
                return
            if residue == 0:
                res.append(path[:])
            for i in range(idx, len(candidates)):
                dfs(residue-candidates[i], i, path+[candidates[i]])
        
        
        candidates.sort()
        res = []
        dfs(target, 0, [])
        return res

obj=Solution()
obj.combinationSum([2,3,6,7], 7)
