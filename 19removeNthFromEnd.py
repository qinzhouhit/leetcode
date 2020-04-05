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
    def len_(self, head):
        count=0
        while head:
            count+=1
            head=head.next
        return count

    def removeNthFromEnd(self, head, n):
        list_len=self.len_(head)
        head_bf=head
        if list_len==n:
            head=head.next
            return head
        i=1
        while i<list_len-n:
            head=head.next
            i+=1
        if head.next.next:
            head.next=head.next.next
        else:
            head.next=None
        return head_bf


