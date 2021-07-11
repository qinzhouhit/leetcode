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
    # T: O(N), S: O(1)
    def partition(self, head, x):
        head1 = p1 = ListNode(0) # for nodes smaller than x
        head2 = p2 = ListNode(0)
        while head:
            if head.val < x:
                p1.next = head
                p1 = p1.next
            else:
                p2.next = head
                p2 = p2.next
            head = head.next # advance head along original list
        p2.next = None
        p1.next = head2.next
        return head1.next


    def partition(self, head, x):
        # before and after are the two dummy pointers used to create two list
        # before_head and after_head are used to save the heads of the two lists.
        # All of these are initialized with the dummy nodes created.
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            # If the original list node is lesser than the given x,
            # assign it to the before list.
            if head.val < x:
                before.next = head
                before = before.next
            else:
                # If the original list node is greater or equal to the given x,
                # assign it to the after list.
                after.next = head
                after = after.next

            # move ahead in the original list
            head = head.next

        ### right now, before and after are the last nodes of two sublists
        # Last node of "after" list would also be ending node of the reformed list
        # we have to cut the after from the rest of nodes (belonging to before list)
        after.next = None
        # Once all the nodes are correctly assigned to the two lists,
        # combine them to form a single list which would be returned.
        before.next = after_head.next

        return before_head.next
