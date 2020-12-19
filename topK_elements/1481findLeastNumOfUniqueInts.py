'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/discuss/686335/JavaPython-3-Greedy-Alg.%3A-3-methods-from-O(nlogn)-to-O(n)-w-brief-explanation-and-analysis.
class Solution:
    # T: O(nlogn), S: O(n)
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        distinct_ele_ct = 0
        if len(arr) <= k:
            return distinct_ele_ct
        ct = Counter(arr)
        minHeap = []
        for num, freq in ct.items():
            heappush(minHeap, (freq, num))
        distinct_ele_ct = len(ct.keys())
        while k > 0 and minHeap:
            freq, num = heappop(minHeap)
            k -= freq
            if k >= 0:
                distinct_ele_ct -= 1
                # print (k, distinct_ele_ct)
        if k > 0:
            distinct_ele_ct -= k
        return distinct_ele_ct

    # shorter version of heapq
    def findLeastNumOfUniqueInts1(self, arr: List[int], k: int) -> int:
        hp = [(freq, num) for num, freq in collections.Counter(arr).items()]
        heapq.heapify(hp)
        while k > 0:
            k -= heapq.heappop(hp)[0] # [0] for the freq
        return len(hp) + (k < 0) 
    
    # hashmap
    # O(n) for S and T
    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        c = Counter(arr)
        # cnt: k: freq of number, v: freq of freq, i.e., number of nums with frequence as freq
        cnt, remaining = Counter(c.values()), len(c) 
        # notice that in Counter, unexisting key will return 0
        for key in range(1, len(arr) + 1): # key is the frequence
        # key * cnt[key] is the total number of frequence of all related numbers
        # it's like accelerating the process
            if k >= key * cnt[key]: 
                k -= key * cnt[key]
                remaining -= cnt[key]
            else: # cant aford deleting all high freq numbers
                return remaining - k // key
        return remaining








            