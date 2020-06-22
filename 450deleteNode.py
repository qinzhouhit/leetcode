'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for a binary tree node.class TreeNode:    def __init__(self, val=0, left=None, right=None):        self.val = val        self.left = left        self.right = right                class Solution:    # use min right subtree val to replace    def deleteNode2(self, root: TreeNode, key: int) -> TreeNode:        if not root: # if root doesn't exist, just return it            return        if root.val > key: # if key value is less than root value, find the node in the left subtree            root.left = self.deleteNode2(root.left, key)        elif root.val < key: # if key value is greater than root value, find the node in right subtree            root.right= self.deleteNode2(root.right, key)        else: #if we found the node (root.value == key), start to delete it            if not root.right: # if it doesn't have right children, we delete the node then new root would be root.left                return root.left            if not root.left: # if it has no left children, we delete the node then new root would be root.right                return root.right       # if the node have both left and right children,  we replace its value with the minmimum value in the right subtree and then delete that minimum node in the right subtree            temp = root.right            mini = temp.val            while temp.left:                temp = temp.left                mini = temp.val            root.val = mini # replace value            root.right = self.deleteNode2(root.right, root.val) # delete the minimum node in right subtree        return root        # use max left subtree val to replace    def deleteNode1(self, root: TreeNode, key: int) -> TreeNode:        if not root:            return                # we always want to delete the node when it is the root of a subtree,        # so we handle left or right according to the val.        # if the node does not exist, we will hit the very first if statement and return None.        if key > root.val: # if key value is greater than root value, find the node in right subtree            root.right = self.deleteNode(root.right, key)                    elif key < root.val: # if key value is less than root value, find the node in the left subtree            root.left = self.deleteNode(root.left, key)                 #if we found the node (root.value == key), start to delete it        else:            # if the subtree does not have a left child, we just return its right child            # to its father, and they will be connected on the higher level recursion.            if not root.left:                return root.right                        # if it has a left child, we want to find the max val on the left subtree to             # replace the node we want to delete.            else:                # try to find the max value on the left subtree                tmp = root.left                while tmp.right:                    tmp = tmp.right                                    # replace                root.val = tmp.val                                # since we have replaced the node we want to delete with the tmp, now we don't                # want to keep the tmp on this tree, so we just use our function to delete it.                # pass the val of tmp to the left subtree and repeat the whole approach.                root.left = self.deleteNode(root.left, tmp.val)                return root        # T: O(logN), O(H1) for find the node to delete, i.e., from root to the     # node to be deleted; O(H2) for the deletion, i.e., from the deleted node     # to the leaf. H1 + H2 = logN    # S: O(logN) for the stack    def successor(self, root):        # go to the successor of root        # one step right and then always left        root = root.right        while root.left:            root = root.left        return root.val        def predecessor(self, root):        # go to the predecessor of root        # one step left and then always right        root = root.left        while root.right:            root = root.right        return root.val        def deleteNode(self, root: TreeNode, key: int) -> TreeNode:        if not root:            return None                # delete from the right subtree        if key > root.val:            root.right = self.deleteNode(root.right, key)        # delete from the left subtree        if key < root.val:            root.right = self.deleteNode(root.left, key)        # delete the current node        else:            # the node is the leaf            if not root.left or root.right:                root = None            # the node is not a leaf and has a right child            elif root.right:                # making the current node val as the val of successor                root.val = self.successor(root)                # delete the found successor                root.right = self.deleteNode(root.right, root.val)            # the node is not a leaf and has no right child, and has a             # left child            else:                root.val = self.predecessor(root)                root.left = self.deleteNode(root.left, root.val)                        return root                                                                                        