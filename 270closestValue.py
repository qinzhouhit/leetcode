'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for a binary tree node.class TreeNode:    def __init__(self, val=0, left=None, right=None):        self.val = val        self.left = left        self.right = right        class Solution:    # binary search, O(H) for T    def closestValue12(self, root: TreeNode, target: float) -> int:        closest = root.val        while root:            closest = min(root.val, closest, key = lambda x: abs(target-x))            root = root.left if target < root.val else root.right        return closest                # O(k) for T,     # O(H) for S,     def closestValue1(self, root: TreeNode, target: float) -> int:        stack, pred = [], float("-inf")        while stack or root:            while root:                stack.append(root)                root = root.left            root = stack.pop()                        if pred <= target and target < root.val:                return min(pred, root.val, key = lambda x: abs(target - x))                        pred = root.val            root = root.right        return pred                # O(N) for S and T, recursive    def closestValue(self, root: TreeNode, target: float) -> int:        def inorder(node):            return inorder(node.left) + [node.val] + inorder(node.right)                return min(inorder(root), key = lambda x: abs(target - x))                