'''
keys: reverse the first half and compare it to the remaining half
Solutions:
Similar:
T: O(n)
S: O(1)
'''


class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        rev = None
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
            # rev = slow # this is wrong since rev is assigned to the slow that will modify the slow value.
            # rev.next = rev
            # slow = slow.next
        if fast: # fast is at the end, move slow one step further for comparison(cross middle one)
            slow = slow.next
        while rev and slow.val == rev.val:
            rev = rev.next
            slow = slow.next
        return not rev

