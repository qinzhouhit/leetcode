'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
	# T: O(A^2 + N), N as number of people, A as number of ages
	# S: O(A)
    def numFriendRequests(self, ages: List[int]) -> int:
        count = [0]*121
        for age in ages:
            count[age] += 1
        
        ans = 0
        for a1, ct1 in enumerate(count):
            for a2, ct2 in enumerate(count):
                if a1 * 0.5 + 7 >= a2: continue
                if a1 < a2: continue
                if a1 < 100 < a2: continue
                ans += ct1 * ct2
                if a1 == a2: ans -= ct1
        return ans