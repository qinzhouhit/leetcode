'''
keys: reverse the first half and compare it to the remaining half
Solutions:
Similar:
T: O(n)
S: O(1)
'''
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome1(self, head):
        fast = slow = head
        # find the mid node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half
        node = None
        while slow:
            nxt = slow.next
            slow.next = node
            node = slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
    
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # rev = slow # this is wrong since rev is assigned to the slow that will modify the slow value.
            # rev.next = rev
            # slow = slow.next
        if fast: # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        while rev and slow.val == rev.val:
            rev = rev.next
            slow = slow.next
        return not rev

