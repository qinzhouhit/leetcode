'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


# controlled recursion
# T: O(1), S: (h)
class BSTIterator:
    def __init__(self, root: TreeNode):
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        """
        @return the next smallest number
        """
        # T: O(1)
        topmost_node = self.stack.pop()

        # the amortized (average) time complexity for this function would still be O(1)
        if topmost_node.right:
            # T: O(1), each node gets pushed and popped exactly once in next()
            # when iterating over all N nodes.
            # That comes out to 2N * O(1) over N calls to next(),
            # making it O(1) on average, or O(1) amortized.
            self._leftmost_inorder(topmost_node.right)
        return topmost_node.val

    # T: O(1)
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0



# method 1: inorder traverse
# inorder traverse the tree and flatten it
# T: O(N), S: O(N) for the nodes_sorted, compromise the condition of O(h)
class BSTIterator1:

    def __init__(self, root: TreeNode):
        self.nodes_sorted = []
        self.index = -1
        self._inorder(root)
    #  the recursion stack for the inorder traversal also occupies space
    #  but that is limited to O(h), h the height of tree

    def _inorder(self, root):
        if not root:
            return
        self._inorder(self, root.left)
        self.nodes_sorted.append(root.val)
        self._inorder(self, root.right)

    # T: O(1)
    def next(self) -> int:
        """
        @return the next smallest number
        """
        self.index += 1
        return self.nodes_sorted[self.index]

    # T: O(1)
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return self.index + 1 < len(self.nodes_sorted)
