# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def levelOrderBottom(self, root):
        import collections

        if not root:
            return []

        queue, res = ([(root, 0)]), []
        while queue:
            node, level = queue.pop(0)
            if node:
                if level == len(res):
                    res.append([])
                res[level].append(node.val)
                queue.append((node.left, level+1))
                queue.append((node.right, level+1))
        return res[::-1]


node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.levelOrderBottom(node1))
