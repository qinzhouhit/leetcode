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


'''
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-postorder-traversal/discuss/161268/C%2B%2BJavaPython-One-Pass-Real-O(N)
real O(N) solution
'''

class Solution:
	# O(N^2) for S and T, N as the number of nodes
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        
        if not pre: return None
        root = TreeNode(pre[0])
        if len(pre) == 1: return root
        '''
        Let's say the left branch has L nodes. We know the head node of that left 
        branch is pre[1], but it also occurs last in the postorder representation 
        of the left branch. So pre[1] = post[L-1] (because of uniqueness of the 
        node values.) Hence, L = post.indexOf(pre[1]) + 1.
        '''
        L = post.index(pre[1]) + 1 # this is O(N)
        root.left = self.constructFromPrePost(pre[1:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1]) # the last node is root
        return root