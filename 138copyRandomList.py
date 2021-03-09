'''
keys:
Solutions:
Similar:
T:
S:
'''

"""
# Definition for a Node.
"""
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    # T: O(N); S: O(1)
    '''
    https://leetcode.com/problems/copy-list-with-random-pointer/discuss/43491/A-solution-with-constant-space-complexity-O(1)-and-linear-time-complexity-O(N)
    The idea is to associate the original node with its copy node in a single
    linked list. In this way, we don't need extra space to keep track of the 
    new nodes.
    '''
    def copyRandomList1(self, head: 'Node') -> 'Node':
        # Insert each node's copy right after it, already copy .label
        node = head
        while node:
            copy = Node(node.val)
            copy.next = node.next
            node.next = copy
            node = copy.next # move to the original next
    
        # Set each copy's .random
        node = head
        while node:
            # node.next is the copy of the node
            if node.random: 
                node.next.random = node.random.next # connecting the random with the copy of the random
            node = node.next.next # go to the original next
    
        # Separate the copied list from the original, (re)setting every .next
        node = head
        dummy = Node(0)
        copy, copy_iter = dummy, dummy
        while node:
            nxt = node.next.next # original next
            # extract the copy
            copy = node.next
            copy_iter.next = copy
            copy_iter = copy
            # restore the original lsit
            node.next = nxt
            node = nxt
        return dummy.next
    

    # T: O(N); S: O(N)
    # two pass
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur, dic = head, {}
        while cur: # get a copy of single Nodes
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head # cur works as ptr
        while cur: # add the random and next pointer info
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head] 

    # official recursion
    def __init__(self):
        # Dictionary which holds old nodes as keys and new nodes as its values.
        self.visitedHash = {}

    def copyRandomList(self, head):

        if head == None:
            return None

        # If we have already processed the current node, then we simply return the cloned version of it.
        if head in self.visitedHash:
            return self.visitedHash[head]

        # create a new node
        # with the value same as old node.
        node = Node(head.val, None, None)

        # Save this value in the hash map. This is needed since there might be
        # loops during traversal due to randomness of random pointers and this would help us avoid them.
        self.visitedHash[head] = node

        # Recursively copy the remaining linked list starting once from the next pointer and then from the random pointer.
        # Thus we have two independent recursive calls.
        # Finally we update the next and random pointers for the new node created.
        node.next = self.copyRandomList(head.next)
        node.random = self.copyRandomList(head.random)

        return node




