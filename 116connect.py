# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root):
        if not root: return []
        import collections
        queue, res = collections.deque([root]), []
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                # if node:
                tmp+=[node.val]
                if node.left: queue+=[node.left]
                if node.right: queue+=[node.right]
            res+=[v for v in tmp]
            res+=['#']
        return res




node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.zigzagLevelOrder(node1))
