'''
keys:
Solutions:
Similar: 124, 543
T:
S:
'''
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    # T: O(N), N as # of nodes
    # S: O(log(N)), recursion stack as size of tree height
    def longestUnivaluePath(self, root: TreeNode) -> int:
        # if not root: return 0
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, node):
        if not node: return 0
        l = self.helper(node.left) # univaluePath length of left subtree
        r = self.helper(node.right)
        pl = 0; pr = 0 # path length (including the subtree to the cur root)
        if node.left and node.val == node.left.val:
            pl = l + 1
        if node.right and node.val == node.right.val:
            pr = r + 1
        self.ans = max(self.ans, pl + pr)
        return max(pl, pr)

