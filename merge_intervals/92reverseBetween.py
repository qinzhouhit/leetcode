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
    # self-made; T: O(N), S: O(1)
    def reverseBetween1(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        
        ptr = 1
        prev, cur = None, head
        while cur and ptr < m:
            prev = cur
            cur = cur.next
            ptr += 1
        
        last_node_1st_part = prev
        last_node_sublist = cur # the end of reversed sublist
        # now ptr == m
        while cur and ptr <= n:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
            ptr += 1
        # print (last_node_1st_part.val, prev.val, last_node_sublist.val, cur.val)
        # 1 4 2 5
        # prev now is the head of the sublist
        if last_node_1st_part:
            last_node_1st_part.next = prev
        else:
            head = prev
        # cur is the 1st node of the 3rd part (after the sublist)
        last_node_sublist.next = cur
        return head
        
        
            
            

    def reverseBetween(self, head, m, n):
        if not head:
            return None

        dummy = pre = ListNode(0)
        dummy.next = head
        for _ in range(m-1): # m-1 operations
            pre = pre.next

        start = pre.next # 1st node in sublist
        then = start.next # node to be reversed

        for _ in range(0, n-m):
            # now: pre: 1, start:2, then: 3
            start.next = then.next # 1->2->4->5
            # now: pre: 1, start:2, then: 3
            then.next = pre.next # 3->2
            # now: pre: 1, start:2, then: 3
            pre.next = then # 1->3
            # now: pre: 1, start:2, then: 3
            then = start.next # 1->3->2->4->5
            # now: pre: 1, start:2, then: 4
        return dummy.next

e1=ListNode(1)
e2=ListNode(2)
e3=ListNode(3)
e4=ListNode(4)
e5=ListNode(5)
e1.next=e2
e2.next=e3
e3.next=e4
e4.next=e5
obj=Solution()
obj.reverseBetween(e1, 2, 4)


# Input: 1->2->3->4->5->NULL, m = 2, n = 4
# Output: 1->4->3->2->5->NULL
