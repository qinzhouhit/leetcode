'''
keys:
Solutions:
Similar:
T:
S:
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    # official recursive
    def reverseLinkedList(self, head, k):
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains
        # at least k nodes.
        new_head, ptr = None, head # does not matter what is initialized in new_head
        while k:
            # Keep track of the next node to process in the
            # original list
            next_node = ptr.next

            # Insert the node pointed to by "ptr"
            # at the beginning of the reversed list
            ptr.next = new_head
            new_head = ptr

            # Move on to the next node
            ptr = next_node

            # Decrement the count of nodes to be reversed by 1
            k -= 1

        # Return the head of the reversed list
        return new_head

    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        count = 0
        ptr = head
        # First, see if there are atleast k nodes
        # left in the linked list.
        while count < k and ptr:
            ptr = ptr.next
            count += 1

        # If we have k nodes, then we reverse them
        if count == k:
            # Reverse the first k nodes of the list and
            # get the reversed list's head.
            reversedHead = self.reverseLinkedList(head, k)

            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            # head: original head of the linked list
            # head.next should be the return node (its head node) of reverseKGroup
            head.next = self.reverseKGroup2(ptr, k)
            return reversedHead
        return head # if less than k node



    # recursive
    # recursion length is n/k, hence you need O(n/k) memory to store implicit stack.
    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
        # 1. test weather we have more then k node left,
        # if less then k node left we just return head
        node = head
        count = 0
        while count < k:
            if node == None: return head
            node = node.next
            count += 1

        # 2.reverse k node at current level
        # pre is the "head" of the remaining linked list
        # e.g., 1->2->3->4->5, k=2, then first pre is node 5
        pre = self.reverseKGroup1(node, k)
        while count > 0:
            tmp = head.next # store head.next
            # making sure that the original head.next connects to the pre
            # i.e., the original head essential becomes the new tail in the reversed linked list
            # e.g., 1->2->3->4->5, 3 is head and 5 is pre; in the reversed
            # it should be 3->5, so head.next = pre (3.next = 5)
            head.next = pre
            # pre becomes the original head, e.g., 3 is pre (head of the "finished" linked list)
            # e.g., 4 (will be new head) 3->5 (3 and 5 are finished, don't have to touch it)
            pre = head
            head = tmp # move head to the next node
            count -= 1
        return pre


    # non-recursivem T: O(N), S: O(1), constant
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        len_ = 0
        tmp = head
        # have the length of the linked list
        while tmp:
            len_ += 1
            tmp = tmp.next

        dummy = ListNode(0)
        dummy.next = head
        prev = dummy; tail = head
        while len_ >= k:
            for i in range(1, k):
                # next = ListNode()
                tmp = tail.next.next
                tail.next.next = prev.next
                prev.next = tail.next
                tail.next = tmp

            prev = tail
            tail = tail.next

            len_ -= k
        return dummy.next

node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
node7 = ListNode(7)
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
obj = Solution()
print (obj.reverseKGroup1(node1, 3))



