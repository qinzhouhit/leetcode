'''
keys:
Solutions:
Similar:
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
	# O(N) for S and T
	# S: the queue holds no more than two levels of nodes.
    def widthOfBinaryTree(self, root: TreeNode) -> int:
        if not root:
            return 0
        
        q = deque([(root, 0)])
        res = float("-inf")
        while q:
            cur = []
            _, level_head_idx = q[0]
            for _ in range(len(q)):
                node, col_idx = q.popleft()
                if node.left:
                    q.append((node.left, 2 * col_idx))
                if node.right:
                    q.append((node.right, 2 * col_idx + 1))
            res = max(res, col_idx - level_head_idx + 1)
        return res
