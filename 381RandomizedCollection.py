'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


# S: O(N), N as number of operations
class RandomizedCollection:

	def __init__(self):
        """
        Initialize your data structure here.
        """
        self.vals = []
        self.idx = defaultdict(set)
        
    # O(1)
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        """
        self.idx[val].add(len(self.vals)) # k: num, v: idx
        self.vals.append(val)
        return len(self.idx[val]) == 1
        
    # O(1)
    def remove(self, val: int) -> bool:
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        """
        if not self.idx[val]:
            return False
        # set has .pop(), pop a random one in set
        toRemoveIdx, lastVal = self.idx[val].pop(), self.vals[-1]
        self.vals[toRemoveIdx] = lastVal # move lastVal to toRemoveIdx
        self.idx[lastVal].add(toRemoveIdx) # add the corresponding idx
        self.idx[lastVal].discard(len(self.vals)-1) # discard the prev idx
        
        self.vals.pop() # pop the last one
        return True
        
    # O(1)
    def getRandom(self) -> int:
        """
        Get a random element from the collection.
        """
        return random.choice(self.vals) # since all vals are recorded sequentially


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()


