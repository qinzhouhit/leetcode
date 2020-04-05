'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]; res = []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(int("".join(str(v) for v in ls)))
            if node.left:
                stack.append((node.left, ls + [node.left.val]))
            if node.right:
                stack.append((node.right, ls + [node.right.val]))
        return sum(res)


    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res


