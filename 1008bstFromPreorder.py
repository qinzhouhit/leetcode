'''
keys: can have inorder traversal by preorder and postorder
Solutions:
Similar:
T:
S:
'''


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    # TODO: iteration
    # T: O(N) for visiting each node once, S: O(N) to keep the stack for the entire tree
    def bstFromPreorder2(self, preorder) -> TreeNode:
        n = len(preorder)
        if not n: return None

        root = TreeNode(preorder[0])
        stack = [root,]

        for i in range(1, n):
            # take the last element of the stack as a parent
            # and create a child from the next preorder element
            node, child = stack[-1], TreeNode(preorder[i])
            # adjust the parent
            while stack and stack[-1].val < child.val:
                node = stack.pop()

            # follow BST logic to create a parent-child link
            if node.val < child.val:
                node.right = child
            else:
                node.left = child
            # add the child into stack
            stack.append(child)

        return root



    # TODO: recursion
    # T: O(N) for visiting each node once, S: O(N) to keep the entire tree
    def bstFromPreorder1(self, preorder) -> TreeNode:
        def helper(lower = float('-inf'), upper = float('inf')):
            nonlocal idx
            # if all elements from preorder are used
            # then the tree is constructed
            if idx == n:
                return None

            val = preorder[idx]
            # if the current element
            # couldn't be placed here to meet BST requirements
            if val < lower or val > upper:
                return None

            # place the current element
            # and recursively construct subtrees
            idx += 1
            root = TreeNode(val)
            root.left = helper(lower, val)
            root.right = helper(val, upper)
            return root

        idx = 0
        n = len(preorder)
        return helper()

    # TODO: Construct binary tree from preorder and inorder traversal
    # T: O(NlogN), for the sort
    # S: O(N) for inorder traversal and the tree
    def bstFromPreorder(self, preorder) -> TreeNode:
        def helper(in_left=0, in_right=len(preorder)):
            nonlocal pre_ind
            if in_left == in_right:
                return None

            # pick up pre_idx element as a root
            val = preorder[pre_ind]
            root = TreeNode(val)

            ind = ind_dict[val]
            pre_ind += 1  # recursion
            root.left = helper(in_left, ind)
            root.right = helper(ind+1, in_right)
            return root

        inorder = sorted(preorder)
        pre_ind = 0 # # start from first preorder element
        ind_dict = {val: ind for ind, val in enumerate(inorder)}
        return helper()

sol = Solution()
print (sol.bstFromPreorder2([8,5,1,7,10]))
