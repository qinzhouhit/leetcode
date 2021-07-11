'''
keys: put the min value in stack as element of (x, min)
Solutions:
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
    # official brute force
    # T: O(N*M), S: O(1),
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        
        while headA: # for each node in A
            ptrB = headB # cur node in B
            while ptrB: # check if intersect for each node in B
                if headA == ptrB:
                    return headA
                ptrB = ptrB.next
            headA = headA.next
        return None


    # official hashset. T: O(N+M), S: O(M) or O(N)
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        nodesB = set()

        while headB:
            nodesB.add(headB)
            headB = headB.next

        while headA:
            if headA in nodesB:
                return headA
            headA = headA.next
        return None

    # official two pointers, T: O(M+N), S: O(1)
    # the idea is if you switch head, the possible difference between
    # length would be countered.
    # On the second traversal, they either hit or miss.
    # if they meet, pa or pb would be the node we are looking for,
    # if they didn't meet, they will hit the end at the same iteration,
    # pa == pb == None, return either one of them is the same, None
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None

        pa = headA # 2 pointers
        pb = headB

        while pa is not pb:
            # if either pointer hits the end, switch head
            # and continue the second traversal,
            # if not hit the end, just move on to next
            pa = headB if pa is None else pa.next
            pb = headA if pb is None else pb.next

        return pa # only 2 ways to get out of the loop,
        # they meet or the both hit the end=None




    # calculate the length of linked lists
    # calculate the d=|l1-l2|
    # move the pointer of longer list by d
    # move the pointer of both lists until p = q
    def getIntersectionNode1(self, headA, headB):
        if headA is None or headB is None:
            return None

        l1 = 0; curA = headA
        while curA:
            l1 += 1
            curA = curA.next

        l2 = 0; curB = headB
        while curB:
            l2 += 1
            curB = curB.next

        d = abs(l1 - l2)

        if l1 > l2:
            p = headA; q = headB
        else:
            q = headA; p = headB

        while d:
            p = p.next
            d -= 1
        while p:
            if p == q:
                return p
            else:
                p = p.next
                q = q.next


    


    # Concatenate list A and list B, if there's an intersection,
    # there's a loop,
    # so we need to find the start of the loop if there's any:
    def getIntersectionNode2(self, A, B):
        if not A or not B: return None

        # Concatenate A and B
        last = A
        while last.next: last = last.next
        last.next = B

        # Find the start of the loop
        fast = slow = A
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                fast = A
                while fast != slow:
                    slow, fast = slow.next, fast.next
                last.next = None
                return slow

        # No loop found
        last.next = None
        return None
