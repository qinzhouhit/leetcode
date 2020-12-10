'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # recursive; O(N) for S and T
    def sumNumbers2(self, root: TreeNode) -> int:
        return helper2(root, 0)

    def helper2(currentNode, pathSum):
        if currentNode is None:
            return 0
        # calculate the path number of the current node
        pathSum = 10 * pathSum + currentNode.val
        # if the current node is a leaf, return the current path sum
        if currentNode.left is None and currentNode.right is None:
            return pathSum
        # traverse the left and the right sub-tree
        return helper2(currentNode.left, pathSum) + helper2(currentNode.right, pathSum)

    # recursive
    def sumNumbers1(self, root: TreeNode) -> int:
        def helper(node, curPath, allPath):
            if not node:
                return
            curPath = curPath*10 + node.val
            if not node.left and not node.right:
                allPath.append(curPath)
            if node.left:
                helper(node.left, curPath, allPath)
            if node.right:
                helper(node.right, curPath, allPath)
        res = []
        helper(root, 0, res)
        return sum(res)


    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0

        stack = [(root, [root.val])]; res = []
        while stack:
            node, ls = stack.pop()
            if not node.left and not node.right:
                res.append(int("".join(str(v) for v in ls)))
            if node.left:
                stack.append((node.left, ls + [node.left.val]))
            if node.right:
                stack.append((node.right, ls + [node.right.val]))
        return sum(res)


    def sumNumbers1(self, root):
        if not root:
            return 0
        stack, res = [(root, root.val)], 0
        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    res += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))
        return res


