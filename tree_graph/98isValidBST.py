'''
keys: recursion or iterative inorder traverse
Solutions:
Similar:
T: O(n)
S: O(1)
'''
from typing import List

class Solution:

    # >>> iterative traversal with valid range
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True

        stack = [(root, -math.inf, math.inf)]
        while stack:
            node, lower, upper = stack.pop()
            if not node:
                continue
            val = node.val
            if not (lower < val < upper):
                return False
            stack.append((node.right, val, upper)) # order not matter
            stack.append((node.left, lower, val))
        return True

    # >>> Recursive Traversal with Valid Range; O(n) for S and T
    def isValidBST(self, root, floor = float('-inf'), ceiling = float('inf')):
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceiling)


    # >>> iterative inorder traversal
    def isValidBST(self, root: TreeNode) -> bool:
        stack, prev = [], -math.inf

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= prev:
                return False
            prev = root.val
            root = root.right

        return True
        

    #  >>> inorder traversal
    def isValidBST1(self, root):
        if not root:
            return True

        output = []
        self.inOrder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True

        # another check
        # return output == sorted(output) and len(set(output)) == len(output)
    def inOrder(self, root, output):
        if not root:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)

    # >>> self-made
    def isValidBST(self, root: TreeNode) -> bool:

        def helper(node, lower=float("-inf"), upper=float("inf")):
            if not node:
                return True
            if not ( lower < node.val < upper):
                return False
            return helper(node.left, lower, node.val) and \
                    helper(node.right, node.val, upper)
            
        return helper(root)


    #  >>> self-made, not optimal
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        
        def helper(node):
            if not node:
                return
            helper(node.left)
            vals.append(node.val)
            helper(node.right)
        
        vals = []
        helper(root)
        return vals == sorted(vals) and len(set(vals)) == len(vals)
