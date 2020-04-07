'''
keys: recursion or iterative inorder traverse
Solutions:
Similar:
T: O(n)
S: O(1)
'''

class Solution:
    # recursion; O(n) for S and T
    def isValidBST(self, root, floor = float('-inf'), ceiling = float('inf')):
        if not root:
            return True

        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceiling)


    # inorder traversal
    def isValidBST1(self, root):
        if not root:
            return True

        output = []
        self.inOrder(root, output)
        for i in range(1, len(output)):
            if output[i-1] >= output[i]:
                return False
        return True

        # another check
        # return output == sorted(output) and len(set(output)) == len(output)


    def inOrder(self, root, output):
        if not root:
            return

        self.inOrder(root.left, output)
        output.append(root.val)
        self.inOrder(root.right, output)
