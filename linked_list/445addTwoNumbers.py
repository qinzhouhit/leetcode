'''keys: Solutions:Similar: T:S:'''from typing import List# Definition for singly-linked list.class ListNode:    def __init__(self, val=0, next=None):        self.val = val        self.next = next        class Solution:    # self-made    # T and S: O(N1+N2)    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        stack1 = []        while l1:            stack1.append(l1.val)            l1 = l1.next                stack2 = []        while l2:            stack2.append(l2.val)            l2 = l2.next                dummy = head = ListNode(0)        carry = 0        while stack1 or stack2 or carry:            sum_ = 0            if stack1:                sum_ += stack1.pop()            if stack2:                sum_ += stack2.pop()            carry, val = divmod(sum_+carry, 10)            newNode = ListNode(val) # just insert the newNode between head and head.next            nxt = head.next # original nxt            head.next = newNode            newNode.next = nxt        return dummy.next    # use two stacks    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        stack1 = []; stack2 = []                while l1:            stack1.append(l1.val) # [7, 2, 4, 3]            l1 = l1.next                while l2:            stack2.append(l2.val) # [5, 6, 4]            l2 = l2.next                sum_ = 0        curr = ListNode(0)        while stack1 or stack2:            if stack1: # starting from the bottom                sum_ += stack1.pop()            if stack2:                sum_ += stack2.pop()            carry, remainder = divmod(sum_, 10)            curr.val = remainder # cur node: remainder            prev = ListNode(carry) # prev: carry node            prev.next = curr # prev -> curr            curr = prev # move ptr to prev            sum_ = carry # update the sum_                return curr if curr.val else curr.next        # >>> official    # T: O(N1 + N2), N1 as number of nodes in l1    # S: O(1) but O(max(N1, N2)) for the output    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        # find the length of both lists        n1 = n2 = 0        curr1, curr2 = l1, l2        while curr1:            curr1 = curr1.next             n1 += 1        while curr2:            curr2 = curr2.next             n2 += 1        # parse both lists and sum the corresponding positions         # without taking carry into account        # 3->3->3 + 7->7 --> 3->10->10 --> 10->10->3        curr1, curr2 = l1, l2        head = None        while n1 > 0 and n2 > 0:            val = 0            if n1 >= n2:                val += curr1.val                 curr1 = curr1.next                 n1 -= 1            if n1 < n2:                val += curr2.val                 curr2 = curr2.next                n2 -= 1                            # update the result: add to front            curr = ListNode(val)            curr.next = head            head = curr # head works as the ptr        # take the carry into account to have all elements to be less than 10        # 10->10->3 --> 0->1->4 --> 4->1->0        curr1, head = head, None        carry = 0        while curr1:            # current sum and carry            val = (curr1.val + carry) % 10            carry = (curr1.val + carry) // 10                        # update the result: add to front            curr = ListNode(val)            curr.next = head            head = curr            # move to the next elements in the list            curr1 = curr1.next                # add the last carry        if carry:            curr = ListNode(carry)            curr.next = head            head = curr        return head    # >>> dummy reverse it    def reverse(self, node):        if not node:            return node        prev = dummy = None        while node:            nxt = node.next            node.next = prev            prev = node            node = nxt            # print (node, prev)        return prev        def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:        l1 = self.reverse(l1)        l2 = self.reverse(l2)        # print (l1)        # print (l2)                carry = 0        root = n = ListNode(0)        while l1 or l2 or carry:            v1 = v2 = 0            if l1:                v1 = l1.val                l1 = l1.next            if l2:                v2 = l2.val                l2 = l2.next            # v1+v2+carry, this carry is from last round            carry, val = divmod(v1+v2+carry, 10)            n.next = ListNode(val)            n = n.next        return self.reverse(root.next)        # >>> advanced    # O(1) for S    def addTwoNumbers1(self, l1, l2):        x1, x2 = 0, 0        while l1: # 7243            x1 = x1*10+l1.val            l1 = l1.next        while l2: # 564            x2 = x2*10+l2.val            l2 = l2.next        x = x1 + x2 # 7807                head = ListNode(0)        if x == 0: return head        while x: # 7->8->0->7            v, x = divmod(x, 10)            # # one liner for inserting newNode between head and head.next            # head.next, head.next.next = ListNode(v), head.next            # assign the current computed number to temp            temp = head.next            # add new significant digit after head            head.next = ListNode(v)             # reattach rest of the computed number to new sig digit            head.next.next = temp # newNode.next = tmp                    return head.next