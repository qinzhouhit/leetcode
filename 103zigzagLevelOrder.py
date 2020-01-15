# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def zigzagLevelOrder(self, root):
        import collections
        if not root: return []
        queue, res = collections.deque([root]), []
        flag = 1
        while queue:
            tmp = []
            for _ in range(len(queue)):
                node = queue.popleft()
                tmp+=[node.val]
                if node.left: queue+=[node.left]
                if node.right: queue+=[node.right]
            res += [tmp[::flag]]
            flag*=-1
        return res

node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.zigzagLevelOrder(node1))
