'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# self-made
	# T: O(nlogn), n = len(pairs); S: O(n) for sorting
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        if not pairs: return 0
        pairs.sort(key=lambda x:x[1])
        ct = 1
        prev_end = pairs[0][1]
        for p in pairs[1:]:
            cur_s, cur_e = p[0], p[1]
            if cur_s > prev_end:
                ct += 1
                prev_end = cur_e
            else:
                continue
        return ct

    # official 
    def findLongestChain(self, pairs):
        cur, ans = float('-inf'), 0
        for x, y in sorted(pairs, key = operator.itemgetter(1)):
            if cur < x:
                cur = y
                ans += 1
        return ans
                
