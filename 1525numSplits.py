""" 
keys: 
Solutions:
Similar:
T:
S:
"""

from collections import Counter


class Solution:
    def numSplits(self, s: str) -> int:
        l_counter = Counter()
        r_counter = Counter(s)

        res = 0
        for c in s:
        	l_counter[c] += 1
        	r_counter[c] -= 1
        	if r_counter[c] == 0:
        		del r_counter[c]
        	if len(l_counter) == len(r_counter):  # same #distinct letters
        		res += 1
        return res