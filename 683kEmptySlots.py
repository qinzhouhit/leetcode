'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List
import bisect

class Solution:


	'''
    bucket based methods, make each bucket as k+1 long, b[0]: 1 ~ k+1,
    b[1]: k+2 ~ 2*k+2, ... Then track the min/max of each bucket
    For each flower at pos x, p = x/(k+1).
    if x == min(b[p]): # if not the min, then so need to check since there 
    # will always be some flower on the left with dist shorter than k (some min)
        check max(b[p-1]) == x-k-1
    if x == max(b[p]):
        check min(b[p+1]) == x+k+1
    T: O(n), S: O(n//(k+1))
    '''
    def kEmptySlots(self, flowers: List[int], k: int) -> int:
    	n = len(flowers)
        if n == 0 or k >= n:
            return -1 
        k = k + 1 # so we dont type k+1 each time
        buckets = (n + k + 1) // k # number of buckets 
        lows = [float("inf")] * buckets
        highs = [float("-inf")] * buckets
        for i, flower in enumerate(flowers):
            p = flower // k # bucket index of current flower
            if flower < lows[p]:
                lows[p] = flower # keep track of min in this bucket
                if p > 0 and highs[p - 1] == flower - k:
                    return i + 1
            if flower > highs[p]:
                highs[p] = flower
                if p < buckets - 1 and lows[p + 1] == flower + k:
                    return i + 1
        return -1




    '''
    BST: next(x) == x+k+1, since there are k empty slots between
    current x and the next flower
    prev(x) == x-k-1: previous 
    T: O(nlong), O(logn) for each step; S: O(n)
    http://zxi.mytechroad.com/blog/simulation/leetcode-683-k-empty-slots/
    '''
    def kEmptySlots(self, bulbs: List[int], k: int) -> int:
        pass


    '''
    brute force: for each new flower, check whether there are k empty
    slots, but the k + 1 slot is another flower. T: O(2nk), n as 
    number of flowers. S: O(n)
    '''
    def kEmptySlots(self, flowers: List[int], k: int) -> int:

        def isValid(x, k, n, f):
            f[x] = 1 # flower bloom for flower x
            # check the right side the current flower: x
            if x + k + 1 <= n and f[x + k + 1] == 1:
                valid = True
                for i in range(k): # check the places between x and x+k+1
                    if f[x + i + 1] == 1:
                        valid = False
                        break
                if valid:
                    return True
            # check the left side
            if x - k - 1 > 0 and f[x - k - 1] == 1:
                for i in range(k):
                    if f[x - i - 1] == 1:
                        return False
                return True
            return False


        n = len(flowers)
        f = [0] * (n+1) # the status of all flowers

        day_idx = 0
        for x in flowers:
            day_idx += 1
            if isValid(x, k, n, f):
                return day_idx
        return -1









