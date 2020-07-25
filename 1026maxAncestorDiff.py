'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
	'''
	We pass the minimum and maximum values to the children, 
	At the leaf node, we return max - min through the path 
	from the root to the leaf.
	'''
    def maxAncestorDiff(self, root: TreeNode) -> int:
    	return self.dfs(root, root.val, root.val)
    	
    def dfs(root, mx, mn):
    	if not root: return 0
    	mx = max(root.val, mx)
    	mn = min(root.val, mn)
    	l = self.dfs(root.left, mx, mn) # l for maximum diff in left subtree
    	r = self.dfs(root.right, mx, mn)
    	# compare all super/sub differences to get result.
    	return max(mx - mn, max(l, r)) 


     def maxAncestorDiff1(self, root, mn=100000, mx=0):
        return max(self.maxAncestorDiff(root.left, min(mn, root.val), max(mx, root.val)), \
            self.maxAncestorDiff(root.right, min(mn, root.val), max(mx, root.val))) \
            if root else mx - mn




