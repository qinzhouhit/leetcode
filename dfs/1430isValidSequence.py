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
	# use recursion, iterative is not convenient since we have
	# to terminate earlier if one number does not match
	# T: O(min(2^m, n))
	# S: O(n), n as nodes number and m = len(arr)
    def isValidSequence(self, root: TreeNode, arr: List[int]) -> bool:
    	n = len(arr)
        def dfs(node, idx):
            if not node or idx == n or arr[idx] != node.val:
                return False
            if idx == n-1 and not node.left and not node.right:
                return True
            return dfs(node.left, idx+1) or dfs(node.right, idx+1)

        return dfs(root, 0)

    # educative.io 
    def isValidSequence1(self, root: TreeNode, arr: List[int]) -> bool:
        def helper(node, arr, idx):
            if node is None:
                return False

            seqLen = len(arr)
            if idx >= seqLen or node.val != arr[idx]:
                return False
      # if the current node is a leaf, add it is the end of the sequence, we have found a path!
            if node.left is None and node.right is None and idx == seqLen - 1:
                return True
      # recursively call to traverse the left and right sub-tree
      # return true if any of the two recursive call return true
            return helper(node.left, arr, idx + 1) or helper(node.right, arr, idx + 1)
        if not root:
            return len(arr) == 0
        return helper(root, arr, 0)
        
