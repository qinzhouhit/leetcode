'''
keys:
Solutions:
Similar: 543, 687
T:
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # T: O(N), N as # of nodes
    # S: O(log(N)), recursion stack as size of tree height
    # should be O(H), since it may skewed binary tree
    # https://leetcode.com/problems/binary-tree-maximum-path-sum/discuss/603423/Python-Recursion-stack-thinking-process-diagram
    def maxPathSum1(self, root: TreeNode) -> int:
        self.ans = float("-inf") # ans is the maximum path sum including one node
        self.helper(root)
        return self.ans

    def helper(self, root):
        if not root: 
            return float("-inf")
        # ignore any path which has an overall negative sum.
        # 0 is like giving up the path, i.e., not go through it
        l = max(0, self.helper(root.left)) # max(0,): since the ans may be negative
        r = max(0, self.helper(root.right))
        self.ans = max(self.ans, root.val + l + r)
        return root.val + max(l, r)


    # The only difference will be to ignore the paths with negative sums.
    def maxPathSum(self, root: TreeNode) -> int:
        def helper(node):
            nonlocal max_sum # making the maxsum the same, or use self.max_sum
            if not node: 
                return 0
            left_gain = max(helper(node.left), 0)
            right_gain = max(helper(node.right), 0)

            price_newpath = node.val + left_gain + right_gain
            max_sum = max(max_sum, price_newpath)
            return node.val + max(left_gain, right_gain)

        max_sum = float("-inf")
        helper(root)
        return max_sum
