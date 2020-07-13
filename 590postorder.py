'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for a Node.class Node:    def __init__(self, val=None, children=None):        self.val = val        self.children = childrenclass Solution:    # O(N) for S and T    def postorder(self, root: 'Node') -> List[int]:        if not root:            return []                stack = [root]        res = []        while stack:            node = stack.pop()            res.append(node.val)            stack.extend(node.children)        return res        # recursive    def postorder1(self, root: 'Node') -> List[int]:        res = []        if root == None:             return res        def recursion(root, res):            for child in root.children:                recursion(child, res)            res.append(root.val)        recursion(root, res)        return res        # recursive 2    def postorder2(self, root: 'Node') -> List[int]:        result = []        if root:            res = []            for child in root.children:                res += self.postorder2(child)            result += res            result.append(root.val)        return result