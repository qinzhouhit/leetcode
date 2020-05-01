'''
keys:
Solutions:
Similar: 543, 687
T:
S:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    # T: O(N), N as # of nodes
    # S: O(log(N)), recursion stack as size of tree height
    # should be O(H), since it may skewed binary tree

    def maxPathSum1(self, root: TreeNode) -> int:
        self.ans = float("-inf") # must use -inf, since the ans may be negative
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: return 0
        l = max(0, self.helper(root.left))
        r = max(0, self.helper(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)



    def maxPathSum(self, root: TreeNode) -> int:
        def max_gain(node):
            nonlocal max_sum # making the maxsum the same
            if not node: return 0
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        max_gain(root)
        return max_sum
