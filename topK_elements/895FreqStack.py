'''
keys:
Solutions:
Similar:
T: 
S: 
'''
from typing import List

# official, stack of stack
# T: O(1) for push and pop, S: O(N) for number of elements in FreqStack
class FreqStack:

    def __init__(self):
        self.freq = {}
        self.group = defaultdict(list)
        self.maxFreq = 0

    def push(self, x: int) -> None:
    	f = self.freq.get(x, 0) + 1
    	self.freq[x] = f
    	if f > self.maxFreq:
    		self.maxFreq = f
    	self.group[f].append(x)

    def pop(self) -> int:
    	x = self.group[self.maxFreq].pop() # the latest added number
    	self.freq[x] -= 1
    	if not self.group[self.maxFreq]:
    		self.maxFreq -= 1 # the reason it works is we push 1 element each time
    	return x

        


# educative.io version
class Element:

	def __init__(self, num, freq, idx):
		self.num = num
		self.freq = freq
		self.idx = idx # sequence number

	def __lt__(self, other):
		if self.freq != other.freq:
			return self.freq > other.freq
		return self.idx > other.idx # the number pushed later

class FreqStack:

	def __init__(self):
		self.freqMap = {}
		self.maxHeap = []
		self.seqNum = 0

	def push(self, x):
		self.freqMap[x] = self.freqMap.get(x, 0) + 1
		heappush(self.maxHeap, Element(x, self.freqMap[x], self.seqNum))
		self.seqNum += 1

	def pop(self):
		num = heappop(self.maxHeap).num
		if self.freqMap[num] > 1:
			self.freqMap[num] -= 1
		else:
			del self.freqMap[num]
		return num








