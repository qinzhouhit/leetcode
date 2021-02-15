'''keys: use dict to track the idx of the values to enable O(1) removeSolutions:Similar: T:S:'''from typing import Listfrom random import *class RandomizedSet:    def __init__(self):        """        Initialize your data structure here.        """        self.vals = []        self.dict = {} # keep record of idx of values in the list    def insert(self, val: int) -> bool:        """        Inserts a value to the set. Returns true if the set did not already contain the specified element.        """        if val in self.dict:            return False        self.dict[val] = len(self.vals) # the order matters        self.vals.append(val)        return True            # O(1)    def remove(self, val: int) -> bool:        """        Removes a value from the set. Returns true if the set contained the specified element.        """        if val in self.dict:            # move the last element to the place idx of the element to delete            idx = self.dict[val]            last_element = self.vals[-1]            self.vals[idx] = last_element            self.dict[last_element] = idx            # delete the last element, we dont need to swap the val to the list end            # we just pop the last and keep the last_element at idx-th.            self.vals.pop() # O(1)            del self.dict[val] # O(1)            return True        return False            # O(1)    def getRandom(self) -> int:        """        Get a random element from the set.        """        # GetRandom could be implemented in O(1) time with the help of         # standard random.choice in Python         return choice(self.list)        # Your RandomizedSet object will be instantiated and called as such:# obj = RandomizedSet()# param_1 = obj.insert(val)# param_2 = obj.remove(val)# param_3 = obj.getRandom()