'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root):
        if root is None:
            return []

        stack, res = [(root, "")], []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
        return res


node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)
node1.left.right = TreeNode(5)
obj = Solution()
print(obj.binaryTreePaths(node1))
