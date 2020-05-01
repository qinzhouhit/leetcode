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

# https://leetcode.com/problems/binary-tree-cameras/discuss/211180/JavaC%2B%2BPython-Greedy-DFS
class Solution:
    # Return 0 if it's a leaf.
    # Return 1 if it's a parent of a leaf, with a camera on this node.
    # Return 2 if it's coverd, without a camera on this node.
    #
    # For each node,
    # if it has a child, which is leaf (node 0), then it needs camera.
    # if it has a child, which is the parent of a leaf (node 1), then it's covered.
    #
    # If it needs camera, then res++ and we return 1.
    # If it's covered, we return 2.
    # Otherwise, we return 0.
    def minCameraCover(self, root: TreeNode) -> int:
        self.res = 0
        def dfs(node):
            if not node: return 2
            l = dfs(node.left)
            r = dfs(node.right)
            if l == r == 2: # (l != 1 and r != 1)
                return 0 # leaf node covered wo camera
            if l == 0 or r == 0:
                self.res += 1
                return 1 # need a camera
            if l == 1 or r == 1:
                return 2 # covered
        return (dfs(root) == 0) + self.res


