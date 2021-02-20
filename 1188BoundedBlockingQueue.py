'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

from collections import deque
from threading import Lock

# deque
# https://leetcode.com/problems/design-bounded-blocking-queue/discuss/442797/Python3-concise-28ms-100-using-Lock-36-ms-using-Condition

class BoundedBlockingQueue(object):

    def __init__(self, capacity: int):
        self.en, self.de = Lock(), Lock()
        self.q = deque()
        self.capacity = capacity
        self.de.acquire()

    def enqueue(self, element: int) -> None:
        self.en.acquire()
        self.q.append(element)
        if len(self.q) < self.capacity:
            self.en.release()
        if self.de.locked():
            self.de.release()

    def dequeue(self) -> int:
        self.de.acquire()
        val = self.q.popleft()
        if len(self.q):
            self.de.release()
        if val and self.en.locked():
            self.en.release()
        return val
        
    def size(self) -> int:
        return len(self.q)