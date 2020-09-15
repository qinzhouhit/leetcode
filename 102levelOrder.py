'''
keys:
Solutions:
Similar: 107
T: a O(N) or O(Nodes + Edges) solution
S:
'''
from typing import List
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder2(self, root):
        res = []
        if not root:
            return res
        
        level = 0
        queue = deque([root,])
        while queue:
            # start the current level
            res.append([])
            # number of elements in the current level 
            level_length = len(queue)
            
            for _ in range(level_length):
                node = queue.popleft()
                # fulfill the current level
                res[level].append(node.val)
                
                # add child nodes of the current level
                # in the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            
            # go to next level
            level += 1
        
        return res
    
    def levelOrder1(self, root):
        res = []
        if not root: return res

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
            res.append(currentNodes)
            level = nextLevel
        return res
    
    
    # recursion; T: O(N), S: O(N)
    def levelOrder1(self, root):
        if not root:
            return []
        
        def helper(node, level):
            # start the current level
            if len(self.res) == level:
                self.res.append([])
            
            # append the current node value
            self.res[level].append(node.val
                                )
            
            # process child nodes for the next level
            if node.left:
                helper(node.left, level+1)
            if node.right:
                helper(node.right, level+1)
        
        
        
        self.res = []
        helper(root, 0)
        return self.res


    def levelOrder0(self, root):
        res = []
        if not root: return res

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
            res.append(currentNodes)
            level = nextLevel
        return res




