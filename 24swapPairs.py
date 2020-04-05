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
    def swapPairs(self, head: ListNode) -> ListNode:
        dummy=tmp=ListNode(0)
        tmp.next=head
        while tmp.next and tmp.next.next:
            a=tmp.next
            b=tmp.next.next
            tmp.next, a.next, b.next = b, b.next, a
            tmp = a
        return dummy

e1=ListNode(1)
e2=ListNode(2)
e3=ListNode(3)
e4=ListNode(5)
e1.next=e2
e2.next=e3
e3.next=e4

obj=Solution()
print (obj.swapPairs(e1))
