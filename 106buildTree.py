'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        def helper(l, r):
            if l > r:
                return None
            val = postorder.pop() # the last element
            root = TreeNode(val)
            idx = idx_dict[val]

            # the order matters, right -> left
            # Because in postorder you will first encounter the root of right subtree
            # unlike preorder where you visit root of left subtree first
            # (postorder:left->right->root)
            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root

        idx_dict = {val: inx for inx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)

        
