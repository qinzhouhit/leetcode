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
    def isBalanced(self, root):
        return self.helper(root) != -1

    def helper(self, root):
        if not root:
            return 0

        leftHeight = self.helper(root.left)
        if leftHeight == -1: return -1
        rightHeight = self.helper(root.left)
        if rightHeight == -1: return -1

        if abs(leftHeight - rightHeight) > 1: return -1
        return max((leftHeight, rightHeight)) + 1


node1 = TreeNode(1)
node2 = node1.left = TreeNode(2)
node1.right = TreeNode(2)
node3 = node2.left = TreeNode(3)
node2.right = TreeNode(3)

node3.left = TreeNode(4)
node3.right = TreeNode(4)
# node4.left = TreeNode(13)
# node5 = node4.right = TreeNode(4)
# node5.left = TreeNode(5)
# node5.right = TreeNode(1)
obj = Solution()
obj.isBalanced(node1)

