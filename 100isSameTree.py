# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q) -> bool:
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            elif None in [node1, node2]:
                return False
            else:
                if node1.val != node2.val:
                    return False
                stack.append((node1.right, node2.right))
                stack.append((node1.left, node2.left))
        return True

node1 = TreeNode(1)
node1.left = TreeNode(2)
node1.right = TreeNode(3)

nod1 = TreeNode(1)
nod1.left = TreeNode(2)
nod1.right = TreeNode(3)


obj = Solution()
print(obj.isSameTree(node1, nod1))

