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
    def partition(self, head, x):
        head1=p1=ListNode(0)
        head2=p2=ListNode(0)
        while head:
            if head.val<x:
                p1.next=head
                p1=p1.next
            else:
                p2.next=head
                p2=p2.next
            head=head.next
        p2.next=None
        p1.next=head2.next
        return head1.next
