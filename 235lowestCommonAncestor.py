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

# class Solution:


class Solution:
    # S: O(1)
    def lowestCommonAncestor1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val: # p, q on left subtree of root
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else: # p.val == root.val or q.val == root.val
                # p.val < root.val < q.val or p.val > root.val > q.val
                return root
            
    # O(N) for S and T        
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        if left and right:
            return root
        if not left:
            return right
        if not right:
            return left


