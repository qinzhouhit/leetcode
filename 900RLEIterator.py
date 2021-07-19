""" 
keys: 
Solutions:
Similar:
T:
S:
"""

# T: O(N)
# S: O(1)
class RLEIterator:

    def __init__(self, encoding: List[int]):
        self.encoding = encoding
        self.idx = 0  # current/ moving idx

    def next(self, n: int) -> int:
    	while self.idx < len(self.encoding):  # all elements exhausted?
    		if n <= self.encoding[self.idx]:  # find the corresponding value.
    			self.encoding[self.idx] = -n  # deduct n from count of value in A[index].
    			return self.encoding[self.idx + 1]  # A[index + 1] is the n-th value.
    		else:  # also works wo/ "else"
	    		n -= self.encoding[self.idx]  # not find the value yet, deduct A[index] from n.
	    		self.idx += 2  # next group of same values
    	return -1  # not enough values remaining.
        


# Your RLEIterator object will be instantiated and called as such:
# obj = RLEIterator(encoding)
# param_1 = obj.next(n)