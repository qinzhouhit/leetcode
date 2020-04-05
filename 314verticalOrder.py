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
    def verticalOrder(self, root):
        # write your code here
        if not root: return []

        import collections
        queue, res = collections.deque([(root, 0)]), collections.defaultdict(list)
        while queue:
            node, val = queue.popleft()
            if node:
                res[val].append(node.val)
                if node.left:
                    queue.append((node.left, val - 1))
                if node.right:
                    queue.append((node.right, val + 1))
        return [res[i] for i in sorted(res)]
