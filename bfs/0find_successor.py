'''
Level Order Successor:
Given a binary tree and a node, find the level order successor of the given node in the tree.
 The level order successor is the node that appears right after the given node in the level order traversal.
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


# official, so elegant...
# O(N) for S and T
def find_successor(root, key):
    if root is None:
    	  return None

  	queue = deque()
  	queue.append(root)
  	while queue:
    	  currentNode = queue.popleft()
    	  # insert the children of current node in the queue
    	  if currentNode.left:
      		  queue.append(currentNode.left)
    	  if currentNode.right:
      		  queue.append(currentNode.right)

    	  # break if we have found the key
    	  if currentNode.val == key:
      		  break

  	return queue[0] if queue else None


# my version
def find_successor(root, key):
  	# TODO: Write your code here
    if not root:
    	  return None
  	q = deque([root])
  	flag = False
  	while q:
    	  len_ = len(q)
    	  for _ in range(len_):
      		  node = q.popleft()
      		  if flag:
        		    return node
      		  if node.val == key:
        		    flag = True

      		  if node.left:
        		    q.append(node.left)
      		  if node.right:
        		    q.append(node.right)

  	return None




