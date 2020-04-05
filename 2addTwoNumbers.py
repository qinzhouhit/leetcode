'''
keys:
Solutions:
Similar:
T:
S:
'''

class ListNode():
    def __init__(self, x):
        self.val=x
        self.next=None

class Solution():
    def addTwoNumbers(self, l1, l2):
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next

e1=ListNode(2)
e2=ListNode(4)
e3=ListNode(3)
e1.next=e2
e2.next=e3

f1=ListNode(5)
f2=ListNode(6)
f3=ListNode(4)
f1.next=f2
f2.next=f3

obj=Solution()
obj.addTwoNumbers(e1, f1)

