""" 
keys: 
Solutions:
Similar:
T:
S:
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
	# notice the flip operation means choosing ANY node
	# so you should compare different subtree pairs
    def flipEquiv(self, root1: TreeNode, root2: TreeNode) -> bool:
    	if root1 == None and root2 == None:
            return True
        if not root1 or not root2 or root1.val != root2.val:
            return False
        
        # now the two nodes are not None and having equal values
        # compare their children recursively
        return (self.flipEquiv(root1.left, root2.left) and \
        		self.flipEquiv(root1.right, root2.right) \
               	or \
                self.flipEquiv(root1.left, root2.right) and \
                self.flipEquiv(root1.right, root2.left))