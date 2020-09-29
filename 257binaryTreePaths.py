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
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # O(N) for S and T
    # self-made, recursive
    def binaryTreePaths1(self, root: TreeNode) -> List[str]:
        def dfs(node, path):
            if node:
                path.append(node.val)
                if not node.left and not node.right:
                    res.append("->".join(map(str, path)))
                dfs(node.left, path)
                dfs(node.right, path)
                path.pop()
        
        res = []
        dfs(root, [])
        return res
    
    
    def binaryTreePaths2(self, root: TreeNode) -> List[str]:
        if not root: return []
        res = []
        stack = [(root, [])]
        while stack:
            node, path = stack.pop()
            if not node.left and not node.right:
                res.append("->".join(map(str, path + [node.val])))
            if node.right:
                stack.append((node.right, path + [node.val]))
            if node.left:
                stack.append((node.left, path + [node.val]))
        return res
    
    
    # iterative
    def binaryTreePaths(self, root):
        if root is None:
            return []

        stack, res = [(root, "")], []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(ls+str(node.val))
            if node.left:
                stack.append((node.left, ls + str(node.val) + "->"))
            if node.right:
                stack.append((node.right, ls + str(node.val) + "->"))
        return res


node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)
node1.left.right = TreeNode(5)
obj = Solution()
print(obj.binaryTreePaths(node1))
