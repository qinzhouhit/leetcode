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
'''from typing import List

from heapq import heappush, heappop, heapreplace, heapify

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# priorityqueue method
from Queue import PriorityQueue
class Solution:
    # divide and conquer
    # T: O(Nlogk); S: O(1)
    def mergeKLists2(self, lists: List[ListNode]) -> ListNode:
        if not lists:
            return 
        if len(lists) == 1:
            return lists[0]
        mid = len(lists)//2
        l = self.mergeKLists2(lists[:mid])
        r = self.mergeKLists2(lists[mid:])
        return self.merge(l, r)

    def merge(self, l, r):
        # merge two lists, l: first, r: second
        dummy = cur = ListNode(0)
        while l and r:
            if l.val < r.val:
                cur.next = l
                l = l.next
            else:
                cur.next = r
                r = r.next
            cur = cur.next
        cur.next = l or r # for the rest remained node
        return dummy.next
        

    # heapq method, not optimal
    # T: O(Nlogk), O(N) as the number of nodes for the while loop
    # O(logk) for the heap pop since there may be k elements in heap
    # https://leetcode.com/problems/merge-k-sorted-lists/discuss/10513/108ms-python-solution-with-heapq-and-avoid-changing-heap-size
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ## If two elements have the same val,
        # the next tuple items will be compared:
        ## "i" in the below code, which is guaranteed to be unique.
        heap = [(head.val, i, head) for i, head in enumerate(lists) if head]
        # the smallest element gets pushed to the index position 0,
        # But rest of the data elements are not necessarily sorted.
        heapify(heap)
        curr = dummy = ListNode(0)
        while heap:
            val, i, node = heappop(heap) # returns the smallest data element from the heap.
            if node.next:
                # recycling tie-breaker i guarantees uniqueness
                #  replaces the smallest data element with a new value supplied in the function.
                heappush(heap, (node.next.val, i, node.next)) 
            curr.next = node
            curr = curr.next
        return dummy.next

    # heap, seems illegal to change ListNode class
    # could use a wrapper here
    # T: O(Nlogk), S: O(k), k is the number of lists
    def mergeKLists3(self, lists: List[ListNode]) -> ListNode:  
        class Wrapper():
            def __init__(self, node):
                self.node = node
            def __lt__(self, other):
                return self.node.val < other.node.val
  
        minHeap = []
        for root in lists:
            if root:
                heappush(minHeap, Wrapper(root))
        head, dummy = None, None # head is the pointer here
        while minHeap:
            node = heappop(minHeap).node
            if not head:
                dummy = head = node
            else:
                head.next = node
                head = head.next # insert the node ahead of tail
            if node.next:
                heappush(minHeap, Wrapper(node.next))
        return dummy    


    # naive method: append the nodes vals in the list and sort, then 
    # construct a new link list
    # T: O(NlogN); S: O(N)
    def mergeKLists0(self, lists: List[ListNode]) -> ListNode:     
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next


    # T: O(Nlogk), k as the number of linked lists, O(logk) for comparison,
    # i.e., pop and insertion to priority queue
    # S: O(n) for new linked list
    def mergeKLists1(self, lists: List[ListNode]) -> ListNode:            
        dummy = ListNode(None)
        cur = dummy
        q = PriorityQueue() # heap is not working
        for node in lists:
            if node:
                q.put((node.val, node))
        while q.qsize() > 0:
            cur.next = q.get()[1]
            cur = cur.next
            if cur.next:
                q.put((cur.next.val, cur.next))
        return dummy.next

        
    




