'''
keys: recursive, first node in preorder is root of tree/subtree
Solutions:
Similar:
T: O(n)
S: O(n)
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution.
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution./32947

    def buildTree(self, preorder, inorder) -> TreeNode:
        from collections import deque

        def helper(preorder, inorder):
            if inorder:
                ind = inorder.index(preorder.popleft()) # ind is the root idx in inorder
                root = TreeNode(inorder[ind])
                root.left = helper(preorder, inorder[:ind]) # inorder[:ind] left subtree
                root.right = helper(preorder, inorder[ind+1:])
                return root

        preorder = deque(preorder)
        return helper(preorder, inorder)


    # iterative version
    # https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34555/The-iterative-solution-is-easier-than-you-think!
    def buildTree(self, preorder, inorder) -> TreeNode:
        if not preorder:
            return None

        h_inorder = {}
        for idx, num in enumerate(inorder):
            h_inorder[num] = idx # val: idx

        root = TreeNode(preorder[0])
        stack = [root]

        for val in preorder[1:]:
            node = TreeNode(val)
            if h_inorder[val] < stack[0].val:
                # the new node is on the left of the last node,
                # so it must be its left child (that's the way preorder works)
                stack[0].left = node
            else:
                # the new node is on the right of the last node,
                # so it must be the right child of either the last node
                # or one of the last node's ancestors.
                # pop the stack until we either run out of ancestors
                # or the node at the top of the stack is to the right of the new node
                parent = None
                while stack and h_inorder[val] > h_inorder[stack[0].val]:
                    parent = stack.pop()
                parent.right = node
            stack.append(node)
        return root



    


node1 = TreeNode(3)
node1.left = TreeNode(9)
node2 = node1.right = TreeNode(20)
node2.left = TreeNode(15)
node2.right = TreeNode(7)

obj = Solution()
print(obj.buildTree([3,9,20,15,7], [9,3,15,20,7]))






