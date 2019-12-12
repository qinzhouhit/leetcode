

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # def __init__(self, node):
    #     self.root=node

    def inorderTraversal(self, root):
        res = []
        self.helper(root, res)
        print (res)
        return res

    def helper(self, root, res):
        if root:
            self.helper(root.left, res)
            res.append(root.val)
            self.helper(root.right, res)

    def inorderIterative(self, root):
        res, stack= [], []
        while stack or root:
            if root:
                stack.append(root)
                root=root.left
            else:
                tmp=stack.pop()
                res.append(tmp.val)
                root=tmp.right
        return res

e1=TreeNode(1)
e2=TreeNode(2)
e3=TreeNode(3)
e1.right=e2
e2.left=e3
obj=Solution()
# obj.inorderTraversal(e1)
obj.inorderIterative(e1)
