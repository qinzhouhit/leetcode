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
            node = copy.next
    
        # Set each copy's .random
        node = head
        while node:
            node.next.random = node.random and node.random.next
            node = node.next.next
    
        # Separate the copied list from the original, (re)setting every .next
        node = head
        copy = head_copy = head and head.next
        while node:
            node.next = node = copy.next
            copy.next = copy = node and node.next
    
        return head_copy
    
    # T: O(N); S: O(N)
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return
        cur, dic = head, {}
        while cur: # get a copy of single Nodes
            dic[cur] = Node(cur.val)
            cur = cur.next
        cur = head
        while cur: # add the random and next pointer info
            if cur.random:
                dic[cur].random = dic[cur.random]
            if cur.next:
                dic[cur].next = dic[cur.next]
            cur = cur.next
        return dic[head]
