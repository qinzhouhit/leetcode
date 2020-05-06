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
            val = postorder.pop()
            root = TreeNode(val)
            idx = idx_dict[val]

            root.right = helper(idx+1, r)
            root.left = helper(l, idx-1)
            return root

        idx_dict = {val: inx for inx, val in enumerate(inorder)}
        return helper(0, len(inorder)-1)

        
