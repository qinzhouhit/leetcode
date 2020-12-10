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

    # educative.io version2, reverse the sublist for alternating k nodes
    # i.e., skip every k nodes
    def reverseKGroup3(self, head: ListNode, k: int) -> ListNode:
        while k <= 1 or not head:
            return head
        prev = None; cur = head
        while True:
            last_node_prev_part = prev
            last_node_cur_sublist = cur
            # reverse k nodes
            ptr = 0
            while cur and ptr < k:
                nxt = cur.next
                cur.next = prev
                prev = cur # prev is the current head of sublist
                cur = nxt
                ptr += 1
            # connect three parts
            if last_node_prev_part:
                last_node_prev_part.next = prev
            else:
                head = prev 
            last_node_cur_sublist.next = cur # cur is the head of the rest nodes
            # skip k nodes
            ptr = 0
            while cur and ptr < k:
                prev = cur
                cur = cur.next
                ptr += 1
            if not cur:
                break
            prev = last_node_cur_sublist
        return head

    # educative.io version, reverse the sublist with less than k nodes
    def reverseKGroup2(self, head: ListNode, k: int) -> ListNode:
        while k <= 1 or not head:
            return head
        
        prev = None
        cur = head
        while True:
            last_node_prev_part = prev
            last_node_cur_sublist = cur
            ptr = 0
            while cur and ptr < k:
                nxt = cur.next
                cur.next = prev
                prev = cur # prev is the head of cur sublist
                cur = nxt # cur will be the head of next sublist
                ptr += 1
            # connect the prev part with cur sublist
            if last_node_prev_part:
                last_node_prev_part.next = prev
            else:
                head = prev
            # connect the cur sublist with the rest linked list nodes
            last_node_cur_sublist.next = cur
            
            if not cur: # no more nodes left to reverse
                break 
            # connect the cur sublist to the next one
            prev = last_node_cur_sublist
        return head


    # educative.io, required the same as this question
    def reverseKGroup3(self, head: ListNode, k: int) -> ListNode:
        while k <= 1 or not head:
            return head
        
        # have the length of the linked list
        len_ = 0; tmp = head
        while tmp:
            len_ += 1
            tmp = tmp.next
        
        prev = None
        cur = head
        while len_ >= k:
            last_node_prev_part = prev
            last_node_cur_sublist = cur
            ptr = 0
            while cur and ptr < k:
                nxt = cur.next
                cur.next = prev
                prev = cur # prev is the head of cur sublist
                cur = nxt # cur will be the head of next sublist
                ptr += 1
            # connect the prev part with cur sublist
            if last_node_prev_part:
                last_node_prev_part.next = prev
            else:
                head = prev
            # connect the cur sublist with the rest linked list nodes
            last_node_cur_sublist.next = cur
            len_ -= k

            if not cur: # no more nodes left to reverse
                break 
            # connect the cur sublist to the next one
            prev = last_node_cur_sublist
        return head
            



    ######
    # official recursive
    # T: O(N); S: O(N/k) for recursion stack
    def reverseLinkedList1(self, head, k):
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

    def reverseKGroup1(self, head: ListNode, k: int) -> ListNode:
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
            reversedHead = self.reverseLinkedList1(head, k)
            # Now recurse on the remaining linked list. Since
            # our recursion returns the head of the overall processed
            # list, we use that and the "original" head of the "k" nodes
            # to re-wire the connections.
            # head: original head of the linked list
            # head.next should be the return node (its head node) of reverseKGroup
            head.next = self.reverseKGroup1(ptr, k)
            return reversedHead
        return head # if less than k node
    
    
    ###### recursive
    # recursion length is n/k, hence you need O(n/k) memory to store implicit stack.
    def reverseKGroup3(self, head: ListNode, k: int) -> ListNode:
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
        pre = self.reverseKGroup3(node, k)
        while count:
            nxt = head.next # store head.next
            # making sure that the original head.next connects to the pre
            # i.e., the original head essential becomes the new tail in the reversed linked list
            # e.g., 1->2->3->4->5, 3 is head and 5 is pre; in the reversed
            # it should be 3->5, so head.next = pre (3.next = 5)
            # i.e., 5 is the newHead in the 1st recursion sol.
            head.next = pre
            # pre becomes the original head, e.g., 3 is pre (head of the "finished" linked list)
            # e.g., 4 (will be new head) 3->5 (3 and 5 are finished, don't have to touch it)
            pre = head
            head = nxt # move head to the next node
            count -= 1
        return pre


    ######
    # iterative T: O(N), S: O(1), constant
    def reverseKGroup4(self, head: ListNode, k: int) -> ListNode:
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
    

    ######
    # S: O(1), iterative 
    def reverseLinkedList2(self, head, k):
        
        # Reverse k nodes of the given linked list.
        # This function assumes that the list contains 
        # atleast k nodes.
        new_head, ptr = None, head
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
        
        ptr = head
        ktail = None
        # Head of the final, moified linked list
        new_head = None
        # Keep going until there are nodes in the list
        while ptr:
            count = 0
            # Start counting nodes from the head
            ptr = head
            # Find the head of the next k nodes
            while count < k and ptr:
                ptr = ptr.next
                count += 1
            # If we counted k nodes, reverse them        
            if count == k:
                # Reverse k nodes and get the new head
                revHead = self.reverseLinkedList2(head, k)
                # new_head is the head of the final linked list
                if not new_head:
                    new_head = revHead
                # ktail is the tail of the previous block of 
                # reversed k nodes
                if ktail:
                    ktail.next = revHead  
                ktail = head 
                head = ptr
        
        # attach the final, possibly un-reversed portion
        if ktail:
            ktail.next = head
        return new_head if new_head else head


    
    
    


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



