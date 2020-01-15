# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int):
        if not root:
            return []

        stack = [(root, [root.val])]; res = []
        while stack:
            node, tmp = stack.pop()
            if not node.left and not node.right and sum(tmp) == s:
                res.append(tmp)
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))
            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
        return res


node1 = TreeNode(5)
node2 = node1.left = TreeNode(4)
node4 = node1.right = TreeNode(8)
node3 = node2.left = TreeNode(11)
node3.left = TreeNode(7)
node3.right = TreeNode(2)
node4.left = TreeNode(13)
node5 = node4.right = TreeNode(4)
node5.left = TreeNode(5)
node5.right = TreeNode(1)
obj = Solution()
obj.pathSum(node1, 22)


