'''
keys: recursive, first node in preorder is root of tree/subtree
Solutions:
Similar:
T: O(n)
S: O(n)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder, inorder) -> TreeNode:
        from collections import deque
        queue = deque(preorder)
        return self.helper(queue, inorder)

    def helper(self, preorder, inorder):
        if inorder:
            ind = inorder.index(preorder.popleft())
            root = TreeNode(inorder[ind])
            root.left = self.helper(preorder, inorder[:ind])
            root.right = self.helper(preorder, inorder[ind+1:])
            return root

node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.buildTree([3,9,20,15,7], [9,3,15,20,7]))
