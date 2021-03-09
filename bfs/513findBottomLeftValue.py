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
	# self-made
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        
        q = deque([root])
        while q:
            res = []
            for _ in range(len(q)):
                node = q.popleft()
                res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res[0]
            

    # concise
    # BFS from right to left
    # https://leetcode.com/problems/find-bottom-left-tree-value/discuss/98779/Right-to-Left-BFS-(Python-%2B-Java)
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root:
            return -1
        q = [root]
        for node in q:
            if node.right:
                q.append(node.right)
            if node.left:
                q.append(node.left)
        return node.val

    # even shorter
    def findLeftMostNode(self, root):
	    queue = [root]
	    for node in queue:
	        queue += filter(None, (node.right, node.left))
	    return node.val
