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

	# some nice dfs
	def isCousins(self, root: TreeNode, x: int, y: int) -> bool:

	    def dfs(node: TreeNode, parent: TreeNode, depth: int):
	        if not node or len(results) == 2:
	            return
	        else:
	            if node.val == x or node.val == y:
	                results.append((parent, depth))
	            dfs(node.left, node, depth + 1)
	            dfs(node.right, node, depth + 1)

	    results = []
	    dfs(root, None, 0)

	    return results[0][0] != results[1][0] and results[0][1] == results[1][1]


	# my version
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if not root: return False
        
        q = deque([(root, None, 0)])
        x1 = []; y1 = []
        while q:
            cur, parent, depth = q.popleft()
            if cur.val == x:
                x1 = [parent, depth]
            elif cur.val == y:
                y1 = [parent, depth]
            if x1 and y1:
                return x1[1] == y1[1] and x1[0] != y1[0]
            if cur.left:
                q.append([cur.left, cur, depth+1])
            if cur.right:
                q.append([cur.right, cur, depth+1])
        return False
                
                
    
    
