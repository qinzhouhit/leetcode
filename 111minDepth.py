'''
keys:
Solutions:
Similar:
T: O(V+E), number of vertices and edges
S: BFS: O(w), w as the maximum width of the tree
DFS: O(h), h as the maximum height of the tree, h = logN
'''

import collections
import sys
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # DFS
    def minDepth2(self, root: TreeNode) -> int:
        if not root:
            return 0
        res, stack = sys.maxint, [(root, 1)]
        while stack:
            node, level = stack.pop()
            if node and not node.left and not node.right:
                res = min(res, level)
            if node:
                stack.append((node.left, level+1))
                stack.append((node.right, level+1))
        return res


    # a beautiful recursion
    def minDepth5(self, root: TreeNode) -> int:
        if not root: return 0
        if not root.left: return self.minDepth5(root.right) + 1
        if not root.right: return self.minDepth5(root.left) + 1
        return min(self.minDepth5(root.left), self.minDepth5(root.right)) + 1


    # official recursion, T: O(N), S: O(logN)
    def minDepth3(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        children = [root.left, root.right]
        # if we're at leaf node, scalable for n-ary tree
        if not any(children):
            return 1

        min_depth = float('inf')
        for c in children:
            if c:
                min_depth = min(self.minDepth(c), min_depth)
        return min_depth + 1

    # official DFS iterationm. T: O(N), S: O(N) (keep entire tree)
    def minDepth4(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            stack, min_depth = [(1, root)], float("inf")

        while stack:
            depth, node = stack.pop()
            children = [root.left, root.right]
            if not any(children):
                min_depth = min(depth, min_depth)
            for c in children:
                if c:
                    stack.append((depth+1, c))
        return min_depth

    

    # DFS (dont understand...)
    def minDepth1(self, root: TreeNode) -> int:
        if not root:
            return 0
        if None in [root.left, root.right]:
            return max(self.minDepth1(root.left), self.minDepth1(root.right)) + 1
        else:
            return min(self.minDepth1(root.left), self.minDepth1(root.right)) + 1


    # BFS. S: O(N), T: O(N), visited N/2 (visit the tree up to the height for balanced tree)
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        queue = collections.deque([(root, 1)])
        while queue:
            node, level = queue.popleft()
            if node:
                if not node.left and not node.right:
                    return level
                else:
                    queue.append((node.left, level+1))
                    queue.append((node.right, level+1))





