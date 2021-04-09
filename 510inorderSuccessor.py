'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
	# T: O(H), S: O(1)
    def inorderSuccessor(self, node: 'Node') -> 'Node':
        # the successor is somewhere lower in the right subtree
        if node.right:
            node = node.right
            while node.left:
                node = node.left
            return node
        
        # the successor is somewhere upper in the tree
        # make sure the node is the right child node of parent
        # until we hit the parent of the whole left subtree
        # then that parent is the successor
        while node.parent and node == node.parent.right:
            node = node.parent
        return node.parent