'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # official
    def rotateRight(self, head: 'ListNode', k: 'int') -> 'ListNode':
        # base cases
        if not head:
            return None
        if not head.next:
            return head
        # for 1->2->3->4->5
        # new_tail at n - k%n - 1 = 2 and new_head at n - k = 3 (idx from 0)
        # close the linked list into the ring
        old_tail = head
        n = 1
        while old_tail.next:
            old_tail = old_tail.next
            n += 1
        old_tail.next = head # form a loop
        # find new tail : (n - k % n - 1)th node
        # and new head : (n - k % n)th node
        new_tail = head
        for _ in range(n - k % n - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        
        # break the ring
        new_tail.next = None
        
        return new_head

    def rotateRight(self, head, k):
        if not head:
            return None
        if head.next == None:
            return head
        ct = 1; pt = head
        while pt.next:
            pt = pt.next
            ct += 1

        moves = k % ct

        if moves == 0:
            return head
        pre_head = cur_head = head

        for _ in range(moves):
            cur_head = cur_head.next # cur_head.val = 3

        while cur_head.next: # cur_head.val = 3, 4, 5
            cur_head = cur_head.next # cur_head.val = 4, 5
            pre_head = pre_head.next # pre_head.val = 2, 3

        tmp = pre_head.next
        pre_head.next = None
        cur_head.next = head
        head = tmp
        return head



