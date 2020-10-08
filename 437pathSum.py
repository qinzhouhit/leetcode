'''keys: prefix sumSolutions: https://leetcode.com/problems/path-sum-iii/discuss/141424/Python-step-by-step-walk-through.-Easy-to-understand.-Two-solutions-comparison.-%3A-)Similar: T:S:'''from typing import Listimport collections# Definition for a binary tree node.class TreeNode:    def __init__(self, val=0, left=None, right=None):        self.val = val        self.left = left        self.right = right        class Solution:    # O(N) for S and T    def pathSum2(self, root: TreeNode, sum: int) -> int:        def preorder(node: TreeNode, curr_sum) -> None:            nonlocal count            if not node:                return                         # current prefix sum            curr_sum += node.val                        # here is the sum we're looking for            if curr_sum == k:                count += 1                        # number of times the curr_sum − k has occurred already,             # determines the number of times a path with sum k             # has occurred up to the current node            count += h[curr_sum - k]                        # add the current sum into hashmap            # to use it during the child nodes processing            h[curr_sum] += 1                        # process left subtree            preorder(node.left, curr_sum)            # process right subtree            preorder(node.right, curr_sum)                        # remove the current sum from the hashmap            # in order not to use it during             # the parallel subtree processing            h[curr_sum] -= 1                    count, k = 0, sum        # key: sum; val: number of ways to reach this sum        h = collections.defaultdict(int)        preorder(root, 0)        return count            # memoization; O(n) for S and O(n) for T    def pathSum1(self, root: TreeNode, target: int) -> int:        # define global result and path        self.result = 0        cache = {0:1}                # recursive to get result        self.dfs1(root, target, 0, cache)                # return result        return self.result        def dfs1(self, root, target, currPathSum, cache):        # exit condition        if root is None:            return          # calculate currPathSum and required oldPathSum        currPathSum += root.val        oldPathSum = currPathSum - target        # update result and cache        self.result += cache.get(oldPathSum, 0)        cache[currPathSum] = cache.get(currPathSum, 0) + 1        # dfs breakdown        self.dfs1(root.left, target, currPathSum, cache)        self.dfs1(root.right, target, currPathSum, cache)        # when move to a different branch, the currPathSum is no longer available, hence remove one.         cache[currPathSum] -= 1                # T: O(nlogn) to O(n^2); O(n) for 1st dfs (going through all     # nodes); O(logn) (balanced tree) to O(n) (single sided tree)    # for 2nd dfs    # S: O(1)    def pathSum(self, root: TreeNode, sum: int) -> int:        self.numOfPaths = 0        self.dfs(root, sum)        return self.numOfPaths        def dfs(self, node, sum):        if not node:            return        self.test(node, sum) # you can move the line to any order, here is pre-order        self.dfs(node.left, sum)        self.dfs(node.right, sum)            def test(self, node, sum):        if not node:            return        if node.val == sum:            self.numOfPaths += 1        self.test(node.left, sum-node.val)        self.test(node.right, sum-node.val)                                        