'''
keys:
Solutions:
Similar: 124, 687
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
    # O(N) for S and T, N as number of nodes
    # https://leetcode.com/problems/diameter-of-binary-tree/discuss/101145/Simple-Python
    def diameterOfBinaryTree1(self, root: TreeNode) -> int:
        
        def depth(p):
            if not p: return 0
            left, right = depth(p.left), depth(p.right)
            self.ans = max(self.ans, left+right)
            return 1 + max(left, right)
        
        self.ans = 0
        depth(root)
        return self.ans
    
    
    # T: O(N), N as # of nodes
    # S: O(log(N)), recursion stack as size of tree height
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, node):
        if node == None: return -1
        l = self.helper(node.left) # l: diamater of left subtree
        r = self.helper(node.right)
        self.ans = max(l + 1 + r + 1, self.ans) # l+r+2: leftTree+root+rightTree
        return max(l, r) + 1


