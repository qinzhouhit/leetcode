'''
keys:
Solutions:
Similar:
T:
S:
'''
import collections

class Solution:
    # O(n) < T(n) < O(n^2)
    '''
    The tricky part is computing the number of recursions you need for it to 
    converge. There are only 26 allowed characters in total, so the recursion
    tree must have a height less than or equal to 26. So wouldn't that make 
    it O(n) work over O(1) recursions for a total runtime complexity of O(n)
    '''
    def longestSubstring3(self, s: str, k: int) -> int:
        if not s: return 0
        if k == 0: return len(s)
        
        ct = collections.defaultdict(int)
        for c in s:
            ct[c] += 1
        
        # check where 
        idx = 0
        while idx < len(s) and ct[s[idx]] >= k:
            idx += 1
        if idx == len(s):
            return len(s)
        # use all the infrequent elements as splits, since any of these 
        # infrequent elements couldn't be any part of the substring we want.
        left = self.longestSubstring3(s[0:idx], k)
        while idx < len(s) and ct[s[idx]] < k: # skip infrequent ones
            idx += 1
        # if idx == len(s)-1: return left # doesn't matter too much
        right = self.longestSubstring3(s[idx:], k)
        return max(left, right)
        
            
        
    
    # O(n) < T(n) < O(n^2)
    def longestSubstring2(self, s: str, k: int) -> int:
        for c in set(s):
            if s.count(c) < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)


    def longestSubstring1(self, s: str, k: int) -> int:
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring(t, k) for t in s.split(c))