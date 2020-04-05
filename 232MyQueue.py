'''
keys:
Solutions:
Similar:
T:
S:
'''

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.q.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if len(self.q) == 0:
            return None
        poped = self.q[0]
        self.q = self.q[1:]
        return poped


    def peek(self) -> int:
        """
        Get the front element.
        """
        if len(self.q) == 0:
            return None
        return self.q[0]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return (not any(self.q))

obj = MyQueue()
print (obj)
print (obj.push(1))
print (obj.push(2))
print (obj.push(3))
print (obj.pop())
print (obj.pop())
print (obj.pop())
print (obj.empty())

