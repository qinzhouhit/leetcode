'''
keys: put the min value in stack as element of (x, min)
Solutions:
Similar:
T:
S:
'''

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.q = []

    def push(self, x: int) -> None:
        curMin = self.getMin()
        if len(self.q) == 0 or x < curMin:
            curMin = x
        self.q.append((x, curMin))


    def pop(self) -> None:
        self.q.pop()


    def top(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][0]


    def getMin(self) -> int:
        if len(self.q) == 0:
            return None
        else:
            return self.q[-1][1]
