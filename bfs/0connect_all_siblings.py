'''
Given a binary tree, connect each node with its level order successor. 
The last node of each level should point to the first node of the next level.
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

# official
def connect_all_siblings(root):
        if root is None:
            return

        queue = deque()
        queue.append(root)
        currentNode, previousNode = None, None
        while queue:
            currentNode = queue.popleft()
            if previousNode:
                previousNode.next = currentNode
            previousNode = currentNode

            # insert the children of current node in the queue
            if currentNode.left:
                queue.append(currentNode.left)
            if currentNode.right:
                queue.append(currentNode.right)


# my version
from collections import deque
def connect_all_siblings(root):
    # TODO: Write your code here
    if not root:
        return None
    q = deque([root])
    while q:
        len_ = len(q)
        for _ in range(len_):
            cur = q.popleft()

            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
    
            nxt = q[0] if q else None
            cur.next = nxt
    return




    