'''
keys: t may be part of s
Solutions:
https://www.jiuzhang.com/solution/one-edit-distance/#tag-other-lang-python
Similar:
T:
S:
'''

class Solution:
    # one pass; O(N) for S and T
    def isOneEditDistance(self, s: str, t: str):
        minLen = min(len(s), len(t))

        for i in range(minLen):
            if s[i] != t[i]:
                # get rid of current char, see remaining equal or not
                if len(s) == len(t):
                    return s[i+1:] == t[i+1:]
                # get rid of current char of s or t, see remaining equal or not
                return s[i:] == t[i+1:] or s[i+1:] == t[i:]

        # t is part of s, e.g., Frank and Fran
        diff = abs(len(s) - len(t))
        return diff == 1
