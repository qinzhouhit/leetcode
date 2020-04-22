'''
keys:
Solutions:
Similar:
T:considering k lists and n being the maximum list size,
there are total number of n.k nodes
at each point of time we are only storing maximum of k nodes in the queue.
 After storing k nodes in the queue, now to insert a new node in the queue,
  time complexity is O( log(k) ) --> comes from time complexity of inserting
   node in priority queue. And since we are doing this for total of n.k nodes,
    it gives total time complexity = n.k.log(k)

Time complexity: O( n.k.log(k) )
Space complexity: O(k), only k nodes are stored at a time
or O(k)+O(n) if the space for returning result is considered
'''


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# priorityqueue method
from queue import PriorityQueue
class Solution:
    def mergeKLists(self, lists):
        dummy = ListNode(None)
        cur = dummy
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next

# heapq method
def mergeKLists(self, lists):
    ## If two elements have the same val,
    # the next tuple items will be compared:
    ## "i" in the below code, which is guaranteed to be unique.
    from heapq import heappush, heappop, heapreplace, heapify
    heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
    # the smallest element gets pushed to the index position 0,
    # But rest of the data elements are not necessarily sorted.
    heapify(heap)
    dummy = ListNode(None)
    curr = dummy
    while heap != []:
        val, i, node = heap[0] # the smallest node
        if not node.next: # exhausted one linked-list
            heappop(heap) # returns the smallest data element from the heap.
        else:
            # recycling tie-breaker i guarantees uniqueness
            #  replaces the smallest data element with a new value supplied in the function.
            heapreplace(heap, (node.next.val, i, node.next))
        curr.next = node
        curr = curr.next
        return dummy.next









