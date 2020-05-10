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
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # TODO: improved pointer (fast and slow)
    # O(1) for S and O(n) for T
    def detectCycle2(self, head):
        slow = head; fast = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                while slow != head:
                    slow = slow.next # it's actually the originial fast pointer
                    head = head.next # it's the head
                return slow
        return None


    # TODO: two pointer (fast and slow)
    # O(1) for S and O(n) for T
    def getIntersect(self, head):
        slow = head
        fast = head

        # A fast pointer will either loop around a cycle and meet the slow
        # pointer or reach the `null` at the end of a non-cyclic list.
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return slow

        return None

    def detectCycle1(self, head):
        if head is None:
            return None

        # If there is a cycle, the fast/slow pointers will intersect at some
        # node. Otherwise, there is no cycle, so we cannot find an entrance to
        # a cycle.
        intersect = self.getIntersect(head)
        if intersect is None:
            return None

        # To find the entrance to the cycle, we have two pointers traverse at
        # the same speed -- one from the front of the list, and the other from
        # the point of intersection.
        ptr1 = head
        ptr2 = intersect
        while ptr1 != ptr2:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        return ptr1


    # TODO: hashset
    # O(n) for S and T
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            else:
                visited.add(node)
                node = node.next
        return node
