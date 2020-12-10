'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
	# T: O(N); S: O(1)
    def middleNode(self, head: ListNode) -> ListNode:
    	if not head:
            return None
        
        fast, slow = head, head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow