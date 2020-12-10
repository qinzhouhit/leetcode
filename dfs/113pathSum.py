'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, s: int):
        if not root:
            return []
        # better use residue to determine since no need to sum every time
        stack = [(root, [root.val])]; res = []
        while stack:
            node, tmp = stack.pop()
            if not node.left and not node.right and sum(tmp) == s:
                res.append(tmp)
            if node.right:
                stack.append((node.right, tmp + [node.right.val]))
            if node.left:
                stack.append((node.left, tmp + [node.left.val]))
        return res

    def pathSum2(self, root: TreeNode, s: int):
        if not root:
            return []
        res = []
        stack = [(root, sum-root.val, [root.val])]
        while stack:
            curr, val, ls = stack.pop()
            if not curr.left and not curr.right and val == 0:
                res.append(ls)
            if curr.right:
                stack.append((curr.right, val-curr.right.val, ls+[curr.right.val]))
            if curr.left:
                stack.append((curr.left, val-curr.left.val, ls+[curr.left.val]))
        return res 

    # recursive
    # T: O(N^2), ‘N’ is the total number of nodes in the tree
    # S: O(N*logN) for recursion stack; the max list length is logn, and n/2 leafs
    # there can’t be more than (N+1)/2(N+1)/2 leaves in a binary tree
    # therefore the maximum number of elements in allPaths will be 
    # O((N+1)/2) = O(N)O((N+1)/2)=O(N)
    def recurseTree(self, node, remainingSum, pathNodes, pathsList):
        
        if not node:
            return 
        
        # Add the current node to the path's list
        pathNodes.append(node.val)
        # Check if the current node is a leaf and also, if it
        # equals our remaining sum. If it does, we add the path to
        # our list of paths
        if remainingSum == node.val and not node.left and not node.right:
            pathsList.append(list(pathNodes))
        else:    
            # Else, we will recurse on the left and the right children
            self.recurseTree(node.left, remainingSum - node.val, pathNodes, pathsList)
            self.recurseTree(node.right, remainingSum - node.val, pathNodes, pathsList)   
        # We need to pop the node once we are done processing ALL of it's
        # subtrees.
        pathNodes.pop()    
    
    def pathSum1(self, root: TreeNode, sum: int) -> List[List[int]]:
        pathsList = []
        self.recurseTree(root, sum, [], pathsList)
        return pathsList


node1 = TreeNode(5)
node2 = node1.left = TreeNode(4)
node4 = node1.right = TreeNode(8)
node3 = node2.left = TreeNode(11)
node3.left = TreeNode(7)
node3.right = TreeNode(2)
node4.left = TreeNode(13)
node5 = node4.right = TreeNode(4)
node5.left = TreeNode(5)
node5.right = TreeNode(1)
obj = Solution()
obj.pathSum(node1, 22)


