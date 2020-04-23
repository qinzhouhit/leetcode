'''
keys:
Solutions:
Similar:
T:
S:
'''

# Hashmap + DoubleLinkedList
# T: O(1) for put and get
# S: O(capacity) for hashmap and double linked list with
# at most capacity + 1 elements
class DLinkedNode():
    def __init__(self):
        self.key = 0
        self.val = 0
        self.prev = None
        self.next = None


class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.size = 0
        self.capacity = capacity
        self.head, self.tail = DLinkedNode(), DLinkedNode
        self.head.next = self.tail # pseudo head and tail
        self.tail.prev = self.head


    def _add_node(self, node):
        '''
        add the new node right after head
        head <-> new node <-> (previous) node after head
        '''
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def _remove_node(self, node):
        prev = node.prev
        tmp = node.next # prev <-> tmp <-> next

        prev.next = tmp
        tmp.prev = prev

    def _

    def get(self, key: int) -> int:
        node = self.cache.get(key, None) # return cache[key] if exists, or None
        if not node:
            return -1

        self._move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:




# ordered dictionary
# T: O(1) for put and get
# S(capacity) the space is used only for an ordered dictionary with at most capacity + 1 elements
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.size = capacity
        self.cache = OrderedDict()

    def get(self, key: int) -> int:
        if key not in self.cache: return -1
        val = self.cache[key]
        self.cache.move_to_end(key)
        return val

    def put(self, key: int, value: int) -> None:
        # The del keyword is used to delete objects. In Python everything is an object
        if key in self.cache: del self.cache[key]
        self.cache[key] = value
        if len(self.cache) > self.size():
            # popitem() method returns and removes a (key, value) pair
            # The pairs are returned in LIFO order if last is true or FIFO order if false.
            self.cache.popitem(last = False)









