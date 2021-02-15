'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
	'''
    https://leetcode.com/problems/largest-bst-subtree/discuss/78899/Very-Short-Simple-Java-O(N)-Solution
	return array for each node: 
    //     [0] --> min of the subtree (inclusive)
    //     [1] --> max
    //     [2] --> largest BST in its subtree(inclusive)
	'''
    def largestBSTSubtree(self, root: TreeNode) -> int:

    	def helper(node):
    		if not node:
    			return [float("inf"), float("-inf"), 0]
    		l = helper(node.left)
    		r = helper(node.right)
    		if l[1] < node.val < r[0]: # check if node can be the root for two subtrees
    		# i.e., node.val larger than max val in left subtree, and smaller than min val in right subtree
    			return [min(node.val, l[0]), max(node.val, r[1]), l[2]+r[2]+1]
    		else: # node can not be part of BST, but we still maintain the maxNode from its subtrees
    			return [float("-inf"), float("inf"), max(l[2], r[2])]

        res = helper(root)
        return res[2]



