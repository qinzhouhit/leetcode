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
    # T: O(N), S: O(1), reverse the second half
    # and compare the two halves
    def isPalindrome1(self, head):
        fast = slow = head
        # find the mid node, i.e., slow
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        # reverse the second half, slow is middle node now if odd # nodes
        # slow is the beginning of second half, if even # nodes
        node = None # head of the reversed half, working similarly to prev
        while slow:
            nxt = slow.next # nxt is tmp node
            slow.next = node # for the 1st loop, slow.next = None
            node = slow # move the node to the slow
            slow = nxt
        # compare the first and second half nodes
        while node: # while node and head:
            if node.val != head.val:
                return False
            node = node.next
            head = head.next
        return True
    
    # ?
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


    # recursive version, O(n) for S and T
    def isPalindrome(self, head: ListNode) -> bool:

        self.front_pointer = head

        def recursively_check(current_node=head):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False
                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check()
    

    # O(N) for S and T: converting to list
    def isPalindrome2(self, head: ListNode) -> bool:
        vals = []
        current_node = head
        while current_node is not None:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]




    

