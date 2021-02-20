'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# https://leetcode.com/problems/design-hit-counter/discuss/83511/Python-solution-with-detailed-explanation
# dictionary version
# scalable version: self.hits = [[0, i+1] for i in range(300)], x0: frequency, x1: timestamp
from collections import defaultdict
class HitCounter(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.counter = defaultdict(int)

    # def get(self, timestamp):
    #     return self.prune(timestamp)       

    def hit(self, timestamp):
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: void
        """
        self.counter[timestamp] += 1

    def getHits(self, timestamp):
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        :type timestamp: int
        :rtype: int
        """
        cnt = 0
        vals = self.counter.keys()
        for k in list(vals): # dict size changes, use deep copy here
            if timestamp - k >= 300:
                del self.counter[k]
            else:
                cnt += self.counter[k] 
        return cnt



class HitCounter:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hits = deque()
        
    # O(1)
    def hit(self, timestamp: int) -> None:
        """
        Record a hit.
        @param timestamp - The current timestamp (in seconds granularity).
        """

        self.hits.append(timestamp)
        
    # O(1)
    def getHits(self, timestamp: int) -> int:
        """
        Return the number of hits in the past 5 minutes.
        @param timestamp - The current timestamp (in seconds granularity).
        """
        while self.hits and timestamp - self.hits[0] >= 300:
            self.hits.popleft()
        return len(self.hits)
        


# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)