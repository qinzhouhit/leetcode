'''
keys: lambda two keys, or heapq
Solutions:
Similar:
T:
S:
'''

import collections
import heapq


# https://leetcode.com/problems/top-k-frequent-words/discuss/108348/Python-3-solution-with-O(nlogk)-and-O(n)

class Word:
    def __init__(self, freq, word):
        self.freq = freq
        self.word = word

    # override its __lt__ and __eq__ functions
    # since sort will only use __lt__
    def __lt__(self, other): # less than
        if self.freq == other.freq:
            # reversed alphabetical order, so larger letters will be popped out
            return self.word > other.word 
        return self.freq < other.freq

    # def __eq__(self, other): # default eq
    #     return self.count == other.count and self.word == other.word


class Solution:
    # real O(nlogk)
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ct = collections.Counter(nums)
        heap = []
        for word, freq in ct.items():
            heapq.heappush(heap, Word(freq, word))
            if len(heap) > k: # without Wrapper class Word, then the highest freq will be popped
                heapq.heappop(heap)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(heap).word)
        return res[::-1] # since minheap


########
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

    # T: O(n + nlogn), n as length of words,
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
