'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/allocate-mailboxes/discuss/685620/JavaC%2B%2BPython-Top-down-DP-Prove-median-mailbox-O(n3)
	# https://www.youtube.com/watch?v=oAwtxihciCc
	# T: O(n^3)
	# costs[i][j] is the cost to put a mailbox among houses[i:j], 
	# the best way is put the mail box at median position among houses[i:j]
    def minDistance(self, houses: List[int], k: int) -> int:
        n = len(houses)
        houses = sorted(houses)
        costs = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(i, n):
                median = houses[(i + j) // 2]
                for t in range(i, j + 1): 
                    costs[i][j] += abs(median - houses[t])

        @lru_cache(None) 
        def dp(k, i): # k: remaining mailbox to assign, i: cur idx
            if k == 0 and i == n: # used out all mailboxes and covered all houses
            	return 0 # find one solution
            if k == 0 or i == n: # no solution found if two conditions are not met at the same time
            	return math.inf
            ans = math.inf
            for j in range(i, n):
                cost = costs[i][j]  # Try to put a mailbox among house[i:j]
                ans = min(ans, cost + dp(k - 1, j + 1)) # then cover [j+1:n]
            return ans

        return dp(k, 0)


