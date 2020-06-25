'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for singly-linked list.class ListNode:    def __init__(self, val=0, next=None):        self.val = val        self.next = next                class Solution:    def insertionSortList1(self, head: ListNode) -> ListNode:        dummy = ListNode(0)        prev = dummy                while (head != None):            temp = head.next                        # Before insert, the prev is at the last node of the sorted list.            # Only the last node's value is larger than the current inserting             # node should we move the temp back to the head            if prev.val >= head.val:                prev = dummy            # find the right place to insert            while prev.next != None and prev.next.val < head.val:                prev = prev.next            # insert between prev and prev.next            # 1 (pre), 3(pre.next), 2(head), 8(head.next/ temp)            head.next = prev.next # 2->3            prev.next = head # 1-> 2            head = temp # 8 now the head                    return dummy.next                def insertionSortList(self, head: ListNode) -> ListNode:        if not head:            return head                helper = ListNode(0)        curr = head # //the node will be inserted        pre = helper # //insert node between pre and pre.next        next_ = None # //the next node will be inserted        # not the end of linklist        while curr != None:            next_ = curr.next            # find the right place to insert            while pre.next != None and pre.next.val < curr.val:                pre = pre.next                        # insert between pre and pre.next            # 1, 3(pre), 2(cur), 8, 5            curr.next = pre.next            pre.next = curr            pre = helper            curr = next_        return helper.next                    