'''
keys:
Solutions:
Similar: 23
T: 
S:
'''

# one can also direclty use solution of LC 23

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next

    # recursively
    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


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

