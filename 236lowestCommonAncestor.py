'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        

class Solution:
    # O(N) for S and T, recursion
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        
        if root == p or root == q:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        
        if left and right: # parent is LCA
            return root
        if not left: 
            return right
        if not right:
            return left

    # iterative; O(N) for S and T
    def lowestCommonAncestor1(self, root, p, q):
        # Stack for tree traversal
        stack = [root]
        # Dictionary for parent pointers
        parent = {root: None}
        # Iterate until we find both the nodes p and q
        while p not in parent or q not in parent:
            node = stack.pop()
            # While traversing the tree, keep saving the parent pointers.
            if node.left:
                parent[node.left] = node
                stack.append(node.left)
            if node.right:
                parent[node.right] = node
                stack.append(node.right)

        # Ancestors set() for node p.
        ancestors = set()
        # Process all ancestors for node p using parent pointers.
        while p:
            ancestors.add(p)
            p = parent[p]
        # The first ancestor of q which appears in
        # p's ancestor set() is their lowest common ancestor.
        while q not in ancestors:
            q = parent[q]
        return q
    
    
    
    
    