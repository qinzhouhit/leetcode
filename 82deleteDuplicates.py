'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head):
        dummy=pre=ListNode(0)
        dummy.next=head
        while head.next and head:
            if head.val==head.next.val:
                while head and head.next and \
                    head.val==head.next.val:
                    head=head.next
                head=head.next
                pre.next=head
            else:
                pre=pre.next
                head=head.next
        return dummy.next

n1=ListNode(1)
n2=ListNode(2)
n3=ListNode(3)
n4=ListNode(3)
n5=ListNode(4)
n6=ListNode(4)
n7=ListNode(5)
n1.next=n2
n2.next=n3
n3.next=n4
n4.next=n5
n5.next=n6
n6.next=n7
obj=Solution()
print(obj.deleteDuplicates(n1))





