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
    # https://leetcode.com/problems/one-edit-distance/solution/481970
    # concise version
    def isOneEditDistance(self, s: str, t: str):
        minLen = min(len(s), len(t))

        for i in range(minLen):
            if s[i] != t[i]:
                # same length, can replace to make current pair the same
                if len(s) == len(t): # since they are of the same length, cant insert or delete
                    return s[i+1:] == t[i+1:] 
                # different length, can only delete or insert
                return s[i:] == t[i+1:] or s[i+1:] == t[i:]

        # t is part of s, e.g., Frank and Fran
        # or cases like "a" and ""
        return abs(len(s) - len(t))  == 1 # we can do delete


    # >>> readable version
    def isOneEditDistance1(self, s, t):
        if s == t:
            return False
        l1, l2 = len(s), len(t)
        if l1 > l2: # force s no longer than t
            return self.isOneEditDistance(t, s)
        if l2 - l1 > 1: # make s the short and t the longer
            return False
        for i in range(len(s)): # s is the shorter one
            if s[i] != t[i]:
                if l1 == l2:
                    s = s[:i]+t[i]+s[i+1:]  # replacement
                else:
                    s = s[:i]+t[i]+s[i:]  # insertion
                break # we one make one round revision
        return s == t or s == t[:-1]

sol = Solution()
print (sol.isOneEditDistance1("ab", "ba"))
