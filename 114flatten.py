'''
keys: all the way to the rightmost
Solutions: right, left, root.right = prev
Similar:
T: O(n)
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root



node1 = TreeNode(1)
node2 = node1.left = TreeNode(2)
node2.left = TreeNode(3)
node2.right = TreeNode(4)
node3 = node1.right = TreeNode(5)
node3.right = TreeNode(6)




obj = Solution()
print(obj.flatten(node1))
obj.printPostorder(node1)
