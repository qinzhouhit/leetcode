'''
keys:
Solutions:
Similar: 107
T: a O(N) or O(Nodes + Edges) solution
S:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root):
        ret = []

        level = [root]

        while root and level:
            currentNodes = []
            nextLevel = []
            for node in level:
                currentNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNodes)
            level = nextLevel
        return ret





