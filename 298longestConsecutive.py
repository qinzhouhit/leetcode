"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        if not root:
            return 0
        res = [0]
        self.helper(root, 0, root.val, res)
        return res[0]

    def helper(self, root, curLen, expected, res):
        if not root:
            return

        if root.val == expected:
            curLen += 1
        else:
            curLen = 1

        res[0] = max(res[0], curLen)

        self.helper(root.left, curLen, root.val + 1, res)
        self.helper(root.right, curLen, root.val + 1, res)

