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
    def rotateRight(self, head, k):
        if not head:
            return None
        if head.next==None:
            return head
        ct=1; pt=head
        while pt.next:
            pt=pt.next
            ct+=1

        rt_times=k%ct

        if rt_times==0:
            return head

        pre_head=cur_head=head

        for _ in range(rt_times):
            cur_head=cur_head.next

        while cur_head.next:
            cur_head=cur_head.next
            pre_head=pre_head.next

        tmp=pre_head.next
        pre_head.next=None
        cur_head.next=head
        head=tmp
        return head



