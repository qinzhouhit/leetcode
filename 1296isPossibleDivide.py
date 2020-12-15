'''
keys: 
Solutions:
Similar: 846
T:
S:
'''
from typing import List

# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/discuss/470238/JavaC%2B%2BPython-Exactly-Same-as-846.-Hand-of-Straights

class Solution:
	# Time O(MlogM + MK), where M is the number of different cards.
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(A)
        for i in sorted(c):
            if c[i] > 0:
                for j in range(k)[::-1]:
                    c[i + j] -= c[i]
                    if c[i + j] < 0:
                        return False
        return True
        

    # O(N+MlogM), where M is the number of different cards.
	# Because I count and sort cards.
    def isPossibleDivide1(self, nums: List[int], k: int) -> bool:
        c = collections.Counter(A)
        start = collections.deque()
        last_checked, opened = -1, 0
        for i in sorted(c):
            if opened > c[i] or opened > 0 and i > last_checked + 1: return False
            start.append(c[i] - opened)
            last_checked, opened = i, c[i]
            if len(start) == k: opened -= start.popleft()
        return opened == 0