'''
keys: iterative and recursively
Solutions:
Similar:
T: O(n)
S: O(1)
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# iterative
class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev

# recursive
class Solution1:
    def reverseList(self, head):
        return self.reverse(head)

    def reverse(self, node, prev=None):
        if not node:
            return prev
        n = node.next
        node.next = prev
        return self.reverse(n, node)


nd1 = ListNode(1)
nd2 = nd1.next = ListNode(2)
nd3 = nd2.next = ListNode(3)
nd4 = nd4.next = ListNode(4)
nd5 = nd5.next = ListNode(5)

sol = Solution1()
sol.reverseList(nd1)



