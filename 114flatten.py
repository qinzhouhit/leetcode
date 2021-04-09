'''
keys: all the way to the rightmost
Solutions: right, left, root.right = prev
Similar:
T: O(n)
S:
'''

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def __init__(self):
        self.prev = None

    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return None
        self.flatten(root.right)
        self.flatten(root.left)
        root.right = self.prev
        root.left = None
        self.prev = root


    ##### iterative
    def flatten(self, root: TreeNode) -> None:
        if not root:
            return
    
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            if node:
                stack.append(node.right)
                stack.append(node.left)
                if prev:
                    prev.right = node
                    prev.left = None
                    node.left = None # you aleady store the node.left in the stack
                prev = node

    ##### 
    def flatten(self, root: TreeNode) -> None:
        node = root
        while node:
            # If the node has a left child
            if node.left:
                # Find the rightmost node
                rightmost = node.left
                while rightmost.right:
                    rightmost = rightmost.right
                # rewire the connections
                rightmost.right = node.right
                node.right = node.left
                node.left = None
            # move on to the right side of the tree
            node = node.right


    ##### official
    def helper(self, node):
        
        # Handle the null scenario
        if not node:
            return None
        
        # For a leaf node, we simply return the
        # node as is.
        if not node.left and not node.right:
            return node
        
        # Recursively flatten the left subtree
        leftTail = self.helper(node.left)
        
        # Recursively flatten the right subtree
        rightTail = self.helper(node.right)
        
        # If there was a left subtree, we shuffle the connections
        # around so that there is nothing on the left side anymore
        if leftTail:
            leftTail.right = node.right
            node.right = node.left
            node.left = None
        
        # We need to return the "rightmost" node after we are
        # done wiring the new connections. 
        return rightTail if rightTail else leftTail
    
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        
        self.helper(root)



node1 = TreeNode(1)
node2 = node1.left = TreeNode(2)
node2.left = TreeNode(3)
node2.right = TreeNode(4)
node3 = node1.right = TreeNode(5)
node3.right = TreeNode(6)




obj = Solution()
print(obj.flatten(node1))
obj.printPostorder(node1)
