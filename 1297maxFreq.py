'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/maximum-number-of-occurrences-of-a-substring/discuss/457577/C%2B%2B-Greedy-approach-%2B-Sliding-window-O(n).
	# two pointers
	# O(26n) for S and T
    def maxFreq(self, s: str, maxLetters: int, minSize: int, maxSize: int) -> int:
        l = 0; res = 0
        freqc = defaultdict(int)
        freqsub = defaultdict(int)
        for r, c in enumerate(s):
            freqc[c] += 1
            if r-l+1 > minSize:
                freqc[s[l]] -= 1
                if freqc[s[l]] == 0:
                    del freqc[s[l]]
                l += 1
            if r-l+1 == minSize and len(freqc) <= maxLetters:
                freqsub[s[l:r+1]] += 1
                res = max(res, freqsub[s[l:r+1]])
        return res