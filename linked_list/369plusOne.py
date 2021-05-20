'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
	# iterative version, O(n) for T and O(1) for S
    def plusOne(self, head: ListNode) -> ListNode:

    	# sentinel head, use for overflow by the carry, e.g., [9] -> [1, 0]
        dummy = ListNode(0)
        dummy.next = head
        not_nine = dummy

        # find the rightmost not-nine digit
        while head:
            if head.val != 9:
                not_nine = head
            head = head.next

        # increase this rightmost not-nine digit by 1
        not_nine.val += 1
        nine = not_nine.next # now not_line.val == 9

        # set all the following nines to zeros
        while nine:
            nine.val = 0
            nine = nine.next
        # if all nines, then not_nine is dummy at line 33
        return dummy if dummy.val else dummy.next



   	# recursion
   	# https://leetcode.com/problems/plus-one-linked-list/discuss/1218977/Python-or-Recursive-Soln.-or-Beats-95
    def plusOne(self, head: ListNode) -> ListNode:

    	def addOne(node: ListNode) -> int:
    		if node:
    			carry = addOne(node.next)
    			div, mod = divmod(node.val + carry, 10)
    			node.val = mod
    			return div
    		return 1 # add one for the last node

    	addOne(head)
    	if head.val is 0: # e.g., [9] -> [0]
    		head = ListNode(1, head)
    	return head



