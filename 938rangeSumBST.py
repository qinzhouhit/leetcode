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

	def rangeSumBST1(self, root: TreeNode, L: int, R: int) -> int:
		def dfs(root):
			if root:
				if L <= root.val <= R:
					self.ans += root.val
				if L < root.val:
					dfs(root.left)
				if R > root.val:
					dfs(root.right)
    	self.ans = 0
    	dfs(root)
    	return self.ans



    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
    	ans = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if L <= node.val <= R:
                    ans += node.val
                if L < node.val: # make use of BST
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
        return ans
