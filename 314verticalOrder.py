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
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    # easy to avoid the sorting, use max_ and min_
    def verticalOrder(self, root):
        # write your code here
        if not root: return []

        import collections
        queue, res = collections.deque([(root, 0)]), collections.defaultdict(list)
        while queue:
            node, col = queue.popleft()
            if node:
                res[col].append(node.val)
                if node.left:
                    queue.append((node.left, col - 1)) # left column
                if node.right:
                    queue.append((node.right, col + 1)) # right column
        # sorted(res): return the sorted keys
        return [res[i] for i in sorted(res)]
