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
	# Record the maximum value along the path from the root to the node.
	# https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/635258/JavaPython-3-Simple-recursion-w-brief-explanation-and-analysis.# T: O(N)
	# S: O(height), n and h are the number and height of the binary tree

    def goodNodes(self, root: TreeNode) -> int:
       
        def count(node: TreeNode, v: int) -> int:
            if node is None:
                return 0
            mx = max(node.val, v)
            return (node.val >= v) + count(node.left, mx) + count(node.right, mx)
        
        return count(root, root.val)


    # one-liner
    # https://leetcode.com/problems/count-good-nodes-in-binary-tree/discuss/635259/JavaC%2B%2BPython-One-line
    def goodNodes(self, r, ma=-10000):  # ma for max
        return self.goodNodes(r.left, max(ma, r.val)) + \
        		self.goodNodes(r.right, max(ma, r.val)) + \
        			(r.val >= ma) if r else 0

        
