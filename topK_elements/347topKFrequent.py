'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import defaultdict
from collections import Counter, heapq
import random

class Solution:
    # O(N) for S and T, quickselect
    def topKFrequent3(self, nums: List[int], k: int) -> List[int]:
        
        def partition(left, right, pivot_index) -> int:
            pivot_frequency = count[unique[pivot_index]]
            # 1. move pivot to end
            unique[pivot_index], unique[right] = unique[right], unique[pivot_index]  
            # 2. move all less frequent elements to the left
            store_index = left
            for i in range(left, right):
                if count[unique[i]] < pivot_frequency:
                    unique[store_index], unique[i] = unique[i], unique[store_index]
                    store_index += 1
            # 3. move pivot to its final place
            unique[right], unique[store_index] = unique[store_index], unique[right]  
            return store_index
        
        def quickselect(left, right, k_smallest) -> None:
            """
            Sort a list within left..right till kth less frequent element
            takes its place. 
            """
            # base case: the list contains only one element
            if left == right: 
                return
            # select a random pivot_index
            pivot_index = random.randint(left, right)     
            # find the pivot position in a sorted list   
            pivot_index = partition(left, right, pivot_index)
            # if the pivot is in its final sorted position
            if k_smallest == pivot_index:
                 return 
            # go left
            elif k_smallest < pivot_index:
                quickselect(left, pivot_index - 1, k_smallest)
            # go right
            else:
                quickselect(pivot_index + 1, right, k_smallest)

        count = Counter(nums)
        unique = list(count.keys())
        n = len(unique) 
        # kth top frequent element is (n - k)th less frequent.
        # Do a partial sort: from less frequent to the most frequent, till
        # (n - k)th less frequent element takes its place (n - k) in a sorted array. 
        # All element on the left are less frequent.
        # All the elements on the right are more frequent.  
        quickselect(0, n - 1, n - k)
        # Return top k frequent elements
        return unique[n - k:]
    
    # educative.io heap
    # T: O(N+N*logK); S: O(N)
    def topKFrequent4(self, nums: List[int], k: int) -> List[int]:
        ct = Counter(nums)
        h = []
        for num, freq in ct.items():
            heappush(h, (freq, num))
            if len(h) > k:
                heappop(h)
        res = []
        while h:
            res.append(heappop(h)[1])
        return res

    
    # T: O(Nlogk)
    # https://leetcode.com/problems/top-k-frequent-elements/solution/
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]: 
        # O(1) time 
        if k == len(nums):
            return nums
        
        # 1. build hash map : character and how often it appears
        # O(N) time
        count = Counter(nums)   
        # 2-3. build heap of top k frequent elements and
        # convert it into an output array
        # O(N log k) time; iterable = keys, key = values, i.e., count.get
        return heapq.nlargest(k, count.keys(), key=count.get) 
    
    # self-made
    def topKFrequent21(self, nums: List[int], k: int) -> List[int]: 
   		tmp = {}
   		for num in nums:
   			if num not in tmp:
   				tmp[num] = 1
   			else:
   				tmp[num] += 1
   		freq = {}
   		for key, v in tmp.items():
   			if v not in freq:
   				freq[v] = [key]
   			else:
   				freq[v].append(key) # k: frequency, v: list of nums
   
   		arr = []
   		for i in range(len(nums), 0, -1):
   			if i in freq:
   				for j in freq[i]:
   					arr.append(j)
   
   		return [arr[x] for x in range(0,k)]


	# another version
    def topKFrequent(self, nums, k):
        frq = defaultdict(list)
        for key, cnt in Counter(nums).items():
            frq[cnt].append(key)

        res = []
        for times in reversed(range(len(nums) + 1)):
            res.extend(frq[times])
            if len(res) >= k: return res[:k]

        return res[:k]

obj = Solution()
print (obj.topKFrequent([1,1,4,6,8,2,2,3], 3))
