'''
keys:
Solutions:
Similar:
T:
S:
'''

"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    # easy to avoid the sorting, use max_ and min_
    # BFS; T: O(NlogN); S: O(N), N as number of nodes in the tree
    def verticalOrder(self, root):
        if not root: return []

        import collections
        queue = collections.deque([(root, 0)])
        res = collections.defaultdict(list)
        while queue:
            node, col = queue.popleft()
            if node:
                res[col].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1)) # left column
                if node.right:
                    queue.append((node.right, col + 1)) # right column
        # sorted(res): return the sorted keys (ascending)
        return [res[i] for i in sorted(res)]
