'''
keys: slow/ quick pointers
Solutions: pay attention to the condition
Similar:
T:
S:
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head):
        if not head:
            return False
        fast = head
        low = head
        while fast != None and fast.next != None:
            fast = fast.next.next
            low = low.next
            if fast == low:
                return True
        return False


    # interesting method
    def hasCycle1(self, head):
        try:
            slow = head
            fast = head.next
            while slow is not fast:
                slow = slow.next
                fast = fast.next.next
            return True
        except:
            return False

    # interesting method
    def hasCycle2(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        while head:
            if head.val == None:
                return True
            head.val = None
            head = head.next
        return False


