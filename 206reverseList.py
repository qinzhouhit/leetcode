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
    # self-made
    def reverseList2(self, head: ListNode) -> ListNode:
        tmp = None # name "tmp" as cur head or sth
        while head:
            nxt = head.next
            head.next = tmp
            tmp = head
            head = nxt
        return tmp


    # keep a referece (curr) to head and pass along the head to the next
    def reverseList(self, head):
        prev = None
        while head:
            curr = head
            head = head.next
            curr.next = prev
            prev = curr
        return prev
 

    # recursive
    def reverseList1(self, head):
        return self.reverse(head)

    def reverse(self, node, prev=None):
        if not node:
            return prev
        nxt = node.next
        node.next = prev
        return self.reverse(nxt, node)


nd1 = ListNode(1)
nd2 = nd1.next = ListNode(2)
nd3 = nd2.next = ListNode(3)
nd4 = nd4.next = ListNode(4)
nd5 = nd5.next = ListNode(5)

sol = Solution1()
sol.reverseList(nd1)



