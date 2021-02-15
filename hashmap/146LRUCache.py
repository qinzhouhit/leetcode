'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



# ordered dictionary
# Time complexity: O(1) both for put and get since all operations with 
# ordered dictionary : get/in/set/move_to_end/popitem 
# (get/containsKey/put/remove) are done in a constant time.
# Space complexity: O(capacity) since the space is used only for an ordered dictionary 
# with at most capacity + 1 elements. 

# self-made, with no heritance version
class LRUCache2:

    def __init__(self, capacity: int):
        self.capacity  = capacity
        self.h = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.h:
            return -1
        # move the key to the end of key list
        # move to the font: h.move_to_end(key, last=False)
        self.h.move_to_end(key) # quite important!!!
        return self.h[key]
        

    def put(self, key: int, value: int) -> None:
        if key in self.h:
            self.h.move_to_end(key)
        self.h[key] = value
        if len(self.h) > self.capacity:
            self.h.popitem(last = False) # FIFO, pop the font one


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
from collections import OrderedDict
class LRUCache1(OrderedDict):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self:
            return - 1
        
        self.move_to_end(key)
        return self[key]

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key in self:
            self.move_to_end(key)
        self[key] = value
        if len(self) > self.capacity:
            # The pairs are returned in LIFO order if last is true or 
            # FIFO order if false.
            self.popitem(last = False)


# Hashmap + DoubleLinkedList
# T: O(1) for put and get
# S: O(capacity) for hashmap and double linked list with
# at most capacity + 1 elements
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.value = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {} # k: key, v: node object, node values as key and value
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode() # two dummy node
        self.head.next = self.tail # pseudo head and tail
        self.tail.prev = self.head

    def _add_node(self, node):
        '''
        always add the new node right after head
        head <=> node <=> (previous) node after head: 2nd
        '''
        # conenct the node to head and head.next
        node.prev = self.head # head <- node
        node.next = self.head.next # node -> 2nd (originally the node after head)
        # connect the head related pointers
        self.head.next.prev = node # node <- 2nd, this step first since we need the .prev
        self.head.next = node # head -> node

    def _remove_node(self, node):
        prev = node.prev
        nxt = node.next # prev <=> node <=> new
        prev.next = nxt
        nxt.prev = prev 

    def _move_to_head(self, node):
        '''
         move certain node in between to the head
        '''
        self._remove_node(node)
        self._add_node(node) # always add after dummy head

    def _pop_tail(self):
        res = self.tail.prev # tail is dummy
        self._remove_node(res)
        return res

    def get(self, key: int) -> int:
        node = self.cache.get(key, None) # return cache[key] if exists, or None
        if not node:
            return -1

        self._move_to_head(node) # move it the front (most frequently visited)
        return node.value

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if not node: # no key in the cache
            newNode = DLinkedNode()
            newNode.key = key
            newNode.value = value

            self.cache[key] = newNode
            self._add_node(newNode)

            self.size += 1
            if self.size > self.capacity:
                tail = self._pop_tail()
                del self.cache[tail.key]
                self.size -= 1

        else:
            # update the value
            node.value = value
            self._move_to_head(node)



obj = LRUCache(2)
print (obj.put(1,1))
print (obj.put(2,2))
print (obj.get(1))
print (obj.put(3,3))
print (obj.get(2))


# # ordered dictionary
# # T: O(1) for put and get
# # S(capacity) the space is used only for an ordered dictionary with at most capacity + 1 elements
# from collections import OrderedDict
# class LRUCache:
#     def __init__(self, capacity: int):
#         self.size = capacity
#         self.cache = OrderedDict()
#
#     def get(self, key: int) -> int:
#         if key not in self.cache: return -1
#         val = self.cache[key]
#         self.cache.move_to_end(key)
#         return val
#
#     def put(self, key: int, value: int) -> None:
#         # The del keyword is used to delete objects. In Python everything is an object
#         if key in self.cache: del self.cache[key]
#         self.cache[key] = value
#         if len(self.cache) > self.size():
#             # popitem() method returns and removes a (key, value) pair
#             # The pairs are returned in LIFO order if last is true or FIFO order if false.
#             self.cache.popitem(last = False)









