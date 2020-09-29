'''
keys: implement it as an iterator to flatten
Solutions:
Similar:
T:
S:
'''
from typing import List




# stack; S: O(N+L)
class NestedIterator:
    # O(N+L), N as total number of integers in the nestedList
    # L as total number of lists in the nestedList
    def __init__(self, nestedList):
        # reverse it for popping the 1st element
        self.stack = nestedList[::-1]

    # O(1) or O(L/N), i.e., O((N+L)/N)
    def next(self) -> int:
        self.make_stack_top_an_integer()
        return self.stack.pop().getInteger()
    
    # O(1) or O(L/N)
    def hasNext(self) -> bool:
        self.make_stack_top_an_integer()
        return len(self.stack) > 0
        
    # O(1) or O(L/N)
    def make_stack_top_an_integer(self):
        # While the stack contains a nested list at the top...
        while self.stack and not self.stack[-1].isInteger():
            # Unpack the list at the top by putting its items onto
            # the stack in reverse order.
            self.stack.extend(self.stack.pop().getList()[::-1])






