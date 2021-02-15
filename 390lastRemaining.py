'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List




# https://leetcode.com/problems/elimination-game/discuss/87119/JAVA%3A-Easiest-solution-O(logN)-with-explanation
# S: O(1), T: O(logn)
class Solution:
    def lastRemaining(self, n: int) -> int:
        remaining = n
        startLeft = True
        step = 1
        head = 1
        while remaining > 1:
            if startLeft or remaining % 2:
                head += step
            remaining //= 2
            step *= 2
            startLeft = not startLeft # start from right
        return head

