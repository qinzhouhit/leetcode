# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False

        stack = [(root, 0)]
        while stack:
            node, tmp = stack.pop()
            if node:
                tmp += node.val
                if node.left:
                    stack.append((node.left, tmp))
                if node.right:
                    stack.append((node.right, tmp))
            if not node.left and not node.right:
                if tmp == sum:
                    return True
        return False

