'''
keys:
Solutions:
Similar:
T:
S:
'''
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        

class Solution:
    # level traversal
    def isSymmetric2(self, root: TreeNode) -> bool:
        if not root:
            return True
        q = deque([root])
        while q:
            len_ = len(q)
            level = []
            for _ in range(len_):
                node = q.popleft()
                level.append(node.val if node else "#")
                if node:
                    q.append(node.left)
                    q.append(node.right)
            if level != level[::-1]:
                return False
        return True
                
            
    # recursive
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        else:
            return self.helper(root.left, root.right)

    def helper(self, leftNode, rightNode):
        if leftNode is None and rightNode is None:
            return True
        if leftNode is None or rightNode is None:
            return False

        if leftNode.val == rightNode.val:
            # return self.helper(node1.left, node2.right) and self.helper(node1.right, node2.left)
            outer = self.helper(leftNode.left, rightNode.right)
            inner = self.helper(leftNode.right, rightNode.left)
            return outer and inner
        else:
            return False
            

    # iterative
    def isSymmetric1(self, root):
        if root is None:
            return True
        stack = deque([(root.left, root.right)])
        while stack:
            left, right = stack.popleft()
            if left is None and right is None:
                continue # attention here!!!
            if left is None or right is None:
                return False
            if left.val == right.val:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
            else:
                return False
        return True
    

# advanced triple node
class TriNode:
    def __init__(self, val=0, left=None, right=None, mid=None):
        self.val = val
        self.left = left
        self.right = right
        self.mid= mid
    
class Solution1:
    def isSymmetric(self, root):
        if not root:
            return True
        q = deque([root.left, root.right])
        while q:
            node1 = q.popleft()
            node2 = q.popleft()
            if node1 is None and node2 is None:
                continue
            if node1 is None or node2 is None or node1.val != node2.val:
                return False
            if node1.val == node2.val:
                q.append(node1.left)
                q.append(node2.right)
                q.append(node1.right)
                q.append(node2.left)
                q.append(node1.mid)
                q.append(node2.mid)
            
    
    
    
    
    
    
    
    
