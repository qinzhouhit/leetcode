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
    # my version
    def hasPathSum1(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return None
        stack = [(root, root.val)]
        while stack:
            node, pathsum = stack.pop()
            if node.left:
                stack.append((node.left, pathsum+node.left.val))
            if node.right:
                stack.append((node.right, pathsum+node.right.val))
            if not node.left and not node.right:
                if pathsum == sum:
                    return True
        return False

    # official, recursion
    def hasPathSum2(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:  # if reach a leaf
            return sum == 0
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)


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

