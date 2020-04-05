'''
keys:
Solutions:
Similar:
T:
S:
'''

# bad problem, can not run by youself

class NestedIterator:
    def __init__(self, nestedList):
        self.stack = nestedList[::-1]

    def next(self) -> int:
        return self.stack.pop().getInteger()

    def hasNext(self) -> bool:
        while self.stack:
            top = self.stack[-1]
            if top.isInteger():
                return True
            self.stack = self.stack[:-1] + top.getList()[::-1] # why reverse it...
        return False

obj, v = NestedIterator([1,[4,[6]]]), []
while obj.hasNext():
    v.append(obj.next())
print (v)
