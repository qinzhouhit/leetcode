'''
keys:
Solutions:
Similar:
T:
S:
'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    # recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.helper(root.left, root.right)

    def helper(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None or rightNode is None:
            return False

        if leftNode.val == rightNode.val:
            # return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
            outer = self.helper(leftNode.left, rightNode.right)
            inner = self.helper(leftNode.right, rightNode.left)
            return outer and inner
        else:
            return False

    # iterative
    def isSymmetric1(self, root):
        if root is None:
            return True
        stack = [(root.left, root.right)]
        while stack:
            left, right = stack.pop()
            if left is None and right is None:
                continue
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
