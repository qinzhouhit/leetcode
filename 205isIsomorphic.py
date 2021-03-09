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
	# O(N) for S and T
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        m1 = defaultdict(int)
        m2 = defaultdict(int)
        for i in range(len(s)):
            if m1[s[i]] != m2[t[i]]:
                return False
            m1[s[i]] = i + 1 # mapping the letters to number or whatever
            m2[t[i]] = i + 1
        return True
            

    # some other versions
    def isIsomorphic(self, s, t):
        s2t, t2s = {}, {}
        for i in range(len(s)):
            if s[i] in s2t and s2t[s[i]] != t[i]:
                return False
            if t[i] in t2s and t2s[t[i]] != s[i]:
                return False
            s2t[s[i]] = t[i]
            t2s[t[i]] = s[i]
        return True
    
    def isIsomorphic1(self, s, t):
        d1, d2 = {}, {}
        for i, val in enumerate(s):
            d1[val] = d1.get(val, []) + [i]
        for i, val in enumerate(t):
            d2[val] = d2.get(val, []) + [i]
        return sorted(d1.values()) == sorted(d2.values())
        
    def isIsomorphic2(self, s, t):
        d1, d2 = [[] for _ in range(256)], [[] for _ in range(256)]
        for i, val in enumerate(s):
            d1[ord(val)].append(i)
        for i, val in enumerate(t):
            d2[ord(val)].append(i)
        return sorted(d1) == sorted(d2)
    
    def isIsomorphic3(self, s, t):
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))
    
    def isIsomorphic4(self, s, t): 
        return [s.find(i) for i in s] == [t.find(j) for j in t]
    
    def isIsomorphic5(self, s, t):
        return map(s.find, s) == map(t.find, t)

    def isIsomorphic6(self, s, t):
        d1, d2 = [0 for _ in range(256)], [0 for _ in range(256)]
        for i in range(len(s)):
            if d1[ord(s[i])] != d2[ord(t[i])]:
                return False
            d1[ord(s[i])] = i+1
            d2[ord(t[i])] = i+1
        return True

