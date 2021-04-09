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
        # that the algorithm starts with a call to the helper function
        # with the root node as the input
        self.stack = []
        self._leftmost_inorder(root)

    def _leftmost_inorder(self, root):
        # For a given node, add all the elements in the leftmost branch 
        # of the tree under it to the stack.
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int: # @return the next smallest number
        # T: O(1), Node at the top of the stack is the next smallest element
        topmost_node = self.stack.pop()

        # Need to maintain the invariant. If the node has a right child, call the
        # helper function for the right child
        # the amortized (average) time complexity for this function would still be O(1)
        if topmost_node.right:
            # T: O(1), each node gets pushed and popped exactly once in next()
            # when iterating over all N nodes.
            # That comes out to 2N * O(1) over N calls to next(),
            # making it O(1) on average, or O(1) amortized.
            self._leftmost_inorder(topmost_node.right) # then you push right subtree to stack
            # so next time it pops out from stack, the right subtree will be processed, i.e., 
            # inorder => left, root, right
        return topmost_node.val

    # T: O(1)
    def hasNext(self) -> bool: # @return whether we have a next smallest number
        return len(self.stack) > 0 # self.stack



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





