'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# O(N) for T and O(1) for S since there are only 26 letters
    def firstUniqChar(self, s: str) -> int:
        ct = Counter(s)
        vals = set([c for c, v in ct.items() if v == 1])
        # print (vals)
        for idx, c in enumerate(s):
            if c in vals:
                return idx
        return -1
                
    # official
    def firstUniqChar(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        # build hash map : character and how often it appears
        count = collections.Counter(s)
        
        # find the index
        for idx, ch in enumerate(s):
            if count[ch] == 1:
                return idx     
        return -1

