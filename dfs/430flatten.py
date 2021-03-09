'''
keys: flatten a doubly linked list
Solutions:
Similar:
T:
S:
'''
from typing import List


"""
# Definition for a Node.
"""
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child

class Solution:

	# O(N) for S and T, iteration
	def flatten1(self, head: 'Node') -> 'Node':
		if not head:
			return 

		dummyNode = Node(0, None, head, None)
        prev = dummyNode # prev of head
		self.helper(prev, head)
		dummyNode.next.prev = None
		return dummyNode.next

	def helper(self, prev, cur):
		if not cur:
			return prev
		prev.next = cur
		cur.prev = prev
		nxt = cur.next # keep it here
		tail = self.helper(cur, cur.child) # deal with child first
		cur.child = None
        # no child => equal to self.helper(cur, cur.next)
		return self.helper(tail, nxt) # no child, then deal with tmp (next node)



	# O(N) for S and T, iteration
    def flatten(self, head: 'Node') -> 'Node':
        if not head:
            return 
        dummyNode = Node(0, None, head, None)
        prev = dummyNode # prev of head
        
        stack = [head]
        while stack: 
            cur = stock.pop()
            prev.next = cur # prev/cur step
            cur.prev = prev
            
            if cur.next:
                stack.append(cur.next)
            
            if cur.child: # append child later so we pop child first
                stack.append(cur.child)
                cur.child = None # required
            
            prev = cur
        # detach the dummyHead from the res since we doubly connect them in the prev/cur step
        dummyNode.next.prev = None
        return dummyNode.next




