'''
keys: recursion, hash table
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
class Solution:
    # T: O(N), S: O(logN), N as node count
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        if not root: return []

        def dfs(node):
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            ct[s] += 1
            return s

        ct = collections.defaultdict(int)
        dfs(root)
        maxCt = max(ct.values())
        return [s for s in ct if ct[s] == maxCt]
