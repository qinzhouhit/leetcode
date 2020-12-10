'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	def __init__(self):
        self.small = []; self.large = []
        
    # T: O(N*K), ‘N’ is the total number of elements in the input array and 
    # ‘K’ is the size of the sliding window
    # Inserting/removing numbers from heaps of size ‘K’. This will take O(logK)O(logK)
    # Removing the element going out of the sliding window. This will take O(K)O(K) as 
    # we will be searching this element in an array of size ‘K’ (i.e., a heap).
    # S: O(K), storing all the numbers within the sliding window.
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        if not nums or k > len(nums):
            return []
        n = len(nums)
        res = [0 for _ in range(n - (k - 1))]
        
        for i, num in enumerate(nums):
            if not self.small or num < -self.small[0]:
                heappush(self.small, -num) # small has one more element than large
            else:
                heappush(self.large, num)
            # rebalance
            self.rebalance()
            # find median
            if i+1 >= k: # accumulating enough k elements in window
                if len(self.small) == len(self.large):
                    res[i+1-k] = (self.large[0] - self.small[0])/2
                else: # we can directly return -self.small[0] since small has more element
                    res[i+1-k] = self.large[0] if len(self.small) < len(self.large) else -self.small[0]
                # remove element
                ele2remove = nums[i+1-k]
                if ele2remove <= -self.small[0]:
                    # print ("small", self.small, -ele2remove)
                    self.remove(self.small, -ele2remove)
                else:
                    # print ("large", self.large, ele2remove) 
                    self.remove(self.large, ele2remove)
                # rebalance
                self.rebalance()
            
        return res
                    
    def remove(self, heap, val):
        ind = heap.index(val)
        heap[ind] = heap[-1] # move last one val to ind
        del heap[-1]
        heapify(heap)
        
    def rebalance(self): # we make self.small with one extra element
        if len(self.small) > len(self.large) + 1: # small has two more nums than large
            heappush(self.large, -heappop(self.small))
        elif len(self.small) < len(self.large): 
            heappush(self.small, -heappop(self.large))

        
        
        
            
