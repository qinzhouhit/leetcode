# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        first=tmp=ListNode(0)
        while l1 and l2:
            if l1.val<l2.val:
                tmp.next=l1
                l1=l1.next
            else:
                tmp.next=l2
                l2=l2.next
            tmp=tmp.next
        tmp.next=l1 or l2
        return first.next


e1=ListNode(1)
e2=ListNode(2)
e3=ListNode(4)
e4=ListNode(5)
e1.next=e2
e2.next=e3
e3.next=e4

f1=ListNode(1)
f2=ListNode(3)
f3=ListNode(4)
f1.next=f2
f2.next=f3

obj=Solution()
obj.mergeTwoLists(e1, f1)

