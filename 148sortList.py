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
    # bottom up merge sort, divide and conquer
    def sortList1(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        len_ = 0
        cur = head
        while cur:
            len_ += 1
            cur = cur.next

        dummy = ListNode(None)
        dummy.next = head
        inc = 1
        for n in range(1, len_, inc): # logn times
            inc *= 2
            cur = dummy.next
            tail = dummy
            while cur:
                l = cur
                r = self.split(l, n)
                cur = self.split(r, n)
                merged = self.merge1(l, r)
                tail.next = merged[0]
                tail = merged[1]
        return dummy.next

    # split the list into two parts, first n elements and the rest
    # return the head of the rest
    def split(self, head, n):
        while n-1 and head:
            n = n - 1
            head = head.next
        rest = head if head.next else None
        if head: head.next = None
        return rest

    def merge1(self, h1, h2): # T: O(n), S: O(1)
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next

        tail.next = h1 or h2
        while tail.next: tail = tail.next
        return dummy.next, tail


    # a non-constant space solution, top-down, recursion
    # T: O(nlogn), S: O(logn) for recursion
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        pre, slow, fast = None, head, head
        while fast and fast.next: # slow will be the middle node
            pre, slow, fast = slow, slow.next, fast.next.next
        pre.next = None # break two sublists
        return self.merge(*map(self.sortList, (head, slow)))

    def merge(self, h1, h2): # T: O(n), S: O(1)
        dummy = tail = ListNode(None)
        while h1 and h2:
            if h1.val < h2.val:
                tail.next, h1 = h1, h1.next
            else:
                tail.next, h2 = h2, h2.next
            tail = tail.next

        tail.next = h1 or h2
        return dummy.next

node1 = ListNode(-1)
node2 = ListNode(5)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(0)
# node6 = ListNode(6)
# node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
# node5.next = node6
# node6.next = node7
obj = Solution()
print (obj.sortList1(node1))
