'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for a binary tree node.class TreeNode:    def __init__(self, val=0, left=None, right=None):        self.val = val        self.left = left        self.right = right        class Solution:    # tracking information    def rob2(self, root: TreeNode) -> int:        '''        the first element of which denotes the maximum amount of         money that can be robbed if root is not robbed, while the         second element signifies the maximum amount of money robbed        if it is robbed.        '''        res = self.robSub1(root)        return max(res[0], res[1])        def robSub1(self, root):        if not root:            return [0, 0]        left = self.robSub1(root.left)        right = self.robSub1(root.right)        res = [0, 0]                # root not robbed, the max of subleft and subright        res[0] = max(left[0], left[1]) + max(right[0], right[1])        # root is robbed, then root.left and root.right are not robbed        res[1] = root.val + left[0] + right[0]                return res                    # DP    def rob1(self, root: TreeNode) -> int:        return self.robSub(root, {})        def robSub(self, root, dict_):        if not root:            return 0        if root in dict_:            return dict_[root]             res = 0        if root.left:            res += self.robSub(root.left.left, dict_) \                + self.robSub(root.left.right, dict_)        if root.right:            res += self.robSub(root.right.left, dict_) \                + self.robSub(root.right.right, dict_)        res = max(res + root.val, self.robSub(root.left, dict_) \                   + self.robSub(root.right, dict_))        dict_[root] = res        return res                            # TLE    def rob(self, root: TreeNode) -> int:        if not root:            return 0                res = 0        if root.left:            res += self.rob(root.left.left) \                + self.rob(root.left.right)                    if root.right:            res += self.rob(root.right.left) \                + self.rob(root.right.right)                return max(res + root.val, self.rob(root.left) \                   + self.rob(root.right))