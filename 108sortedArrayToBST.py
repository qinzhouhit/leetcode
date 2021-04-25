'''
keys:
Solutions:
Similar: 109
T:
S:
'''
# in

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:


    # TODO: updated version choosing right middle node as a root
    def sortedArrayToBST1(self, nums: List[int]) -> TreeNode:
        def helper(left, right):
            if left > right:
                return None

            # always choose right middle node as a root
            p = (left + right) // 2
            if (left + right) % 2:
                p += 1

            # inorder traversal: left -> node -> right
            root = TreeNode(nums[p])
            root.left = helper(left, p - 1)
            root.right = helper(p + 1, right)
            return root

        return helper(0, len(nums) - 1)

    # solution from 109, T: O(N), S: O(N), for the output
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        def convert(l, r):
            if l > r:
                return None
            mid = (l+r)//2
            node = TreeNode(nums[mid])
            # if l == r: # it works w/wo it, since it doesn't matter to go to recursion if l==r
            #     return node
            node.left = convert(l, mid-1)
            node.right = convert(mid+1, r)
            return node
        return convert(0, len(nums)-1)


############################
# the version in algoexpert
############################

class BST:
    def __init__(self, value):
        self.value = value 
        self.left = None
        self.right = None

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)

# given sorted array of distinct integers
# construct a BST with minimum height and return the root


def minHeightBST(arr):
    return BSTconstruct(arr, None, 0, len(array)-1)

# solution 1: O(n) for S and T
def BSTconstruct(arr, node, startIdx, endIdx):
    if startIdx > endIdx:
        return
    midIdx = (startIdx + endIdx) // 2
    val = arr[midIdx] # value to add
    if not node:
        node = BST(val)
    else:
        node.insert(val)
    BSTconstruct(arr, node, startIdx, midIdx-1)
    BSTconstruct(arr, node, midIdx+1, endIdx)
    return node

# solution 2: O(n) for S and T
def BSTconstruct(arr, startIdx, endIdx):
    if startIdx > endIdx:
        return None
    midIdx = (startIdx + endIdx) // 2
    root = BST(arr[midIdx])
    root.left = BSTconstruct(arr, startIdx, midIdx-1)
    root.right = BSTconstruct(arr, midIdx+1, endIdx)
    return root



























