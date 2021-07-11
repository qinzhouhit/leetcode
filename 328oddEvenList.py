'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for singly-linked list.class ListNode:    def __init__(self, val=0, next=None):        self.val = val        self.next = next        class Solution:    # official, concise, faster    # T: O(n), S: O(1)    def oddEvenList1(self, head):        dummy1 = odd = ListNode(0)        dummy2 = even = ListNode(0)        while head:            odd.next = head # odd/evne still acting as dummy            even.next = head.next            odd = odd.next # advance odd/even            even = even.next            # even is actually head.next            head = head.next.next if even else None        odd.next = dummy2.next # connect odd and even sublists        return dummy1.next            def oddEvenList(self, head: ListNode) -> ListNode:        odd = ListNode(0)        even = ListNode(0)        oddHead = odd        evenHead = even        isOdd = True        # think of each iteration of the loop as a toggle between odd and even.        while head:            if isOdd:                odd.next = head                odd = odd.next # this does not affect, since in the next if loop,                # the odd will be pointing to the head            else:                even.next = head                even = even.next            isOdd = not isOdd            head = head.next        even.next = None        odd.next = evenHead.next        return oddHead.next                            