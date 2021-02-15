'''
keys:
Solutions:
Similar:
T:
S:
'''


# Definition for a Node.
class TreeLinkNode:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    # >>> O(1)
    # https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/discuss/37828/O(1)-space-O(n)-complexity-Iterative-Solution
    def connect(self, root: 'Node') -> 'Node':
        node = root
        levelHead = TreeLinkNode(0)
        
        while node: # loop for each level
            needle = levelHead
            
            while node: # loop for current level
                if node.left:
                    # since needle and levelHead points to the same object. That means after needle.next = node.left. 
                    # Same for levelHead.next = node.left. 
                    # this is how levelHead move to next level
                    needle.next = node.left 
                    
                    # needle now points to a different object, not same as levelHead anymore (we reassign needle)
                    # needle is at node's left child
                    needle = needle.next 
                    
                if node.right:
                    # connect node's left child to right child
                    needle.next = node.right
                    # needle moves to node's right child
                    needle = needle.next
                
                # node moves to its neighbor in the current level
                node = node.next
            
            # this is key part. as said before, levelHead.next = node.left
            # so that node moves to its upper level's leftmost node's left child. meaning the head of this next level
            node = levelHead.next
            
            # levelHead.next is used above, make it to none so that next time it won't grab the same level head again.
            levelHead.next = None





    # >>> official O(1)
    def processChild(self, childNode, prev, leftmost):
        if childNode:
            
            # If the "prev" pointer is alread set i.e. if we
            # already found atleast one node on the next level,
            # setup its next pointer
            if prev:
                prev.next = childNode
            else:    
                # Else it means this child node is the first node
                # we have encountered on the next level, so, we
                # set the leftmost pointer
                leftmost = childNode
            prev = childNode 
        return prev, leftmost
    
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # The root node is the only node on the first level
        # and hence its the leftmost node for that level
        leftmost = root
        
        # We have no idea about the structure of the tree,
        # so, we keep going until we do find the last level.
        # The nodes on the last level won't have any children
        while leftmost:
            
            # "prev" tracks the latest node on the "next" level
            # while "curr" tracks the latest node on the current
            # level.
            prev, curr = None, leftmost
            
            # We reset this so that we can re-assign it to the leftmost
            # node of the next level. Also, if there isn't one, this
            # would help break us out of the outermost loop.
            leftmost = None
            
            # Iterate on the nodes in the current level using
            # the next pointers already established.
            while curr:
                
                # Process both the children and update the prev
                # and leftmost pointers as necessary.
                prev, leftmost = self.processChild(curr.left, prev, leftmost)
                prev, leftmost = self.processChild(curr.right, prev, leftmost)
                
                # Move onto the next node.
                curr = curr.next
                
        return root 


    # >>> level-order O(N)
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root
        q = deque([root])
        
        prev = None
        while q:
            for i in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
                if prev:
                    prev.next = node
                if i == len(q)-1:
                    node.next = None
                prev = node
            prev = None
        return root


    # >>> official level-order
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        Q = collections.deque([root])
        while Q:
            size = len(Q)
            for i in range(size):
                node = Q.popleft()
                if i < size - 1:
                    node.next = Q[0]
                if node.left:
                    Q.append(node.left)
                if node.right:
                    Q.append(node.right)
        return root




