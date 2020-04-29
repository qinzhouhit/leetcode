'''
keys: lambda two keys, or heapq
Solutions:
Similar:
T:
S:
'''

import collections
import heapq
class Solution:
    # T: O(nlogn), n as length of words
    # S: O(n) for candidates
    def topKFrequent(self, words, k):
        if not words:
            return []

        count = collections.Counter(words)
        candidates = count.keys()
        res = sorted(candidates, key = lambda w: (-count[w], w))
        return res[:k]

    # T: O(n + klogn), n as length of words,
    # heapify: O(n), each of k heappop: O(logN)
    # S: O(N), for count
    def topKFrequent1(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for _ in range(k)]


obj = Solution()
print (obj.topKFrequent(["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"],
4))
