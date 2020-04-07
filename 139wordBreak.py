'''
keys:
Solutions:
Similar: word break II
T: O(n^2) for both DP and BFS
S: O(n)
'''

import collections

class Solution:
    # d is an array that contains booleans
    # d[i] is True if there is a word in the dictionary that
    # ends at ith index of s AND d is also True at the beginning of the word

    def wordBreak1(self, s, wordDict):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                if w == s[i-len(w)+1:i+1] and (d[i-len(w)] or (i == (len(w)-1))):
                    d[i] = True
        return d[-1]

    # "nightmare", there are two ways to break it,
    # "night mare" and "nightmare". The graph would be
    # 0-->5-->9
    def wordBreak(self, s, wordDict):
        # Modeled as a graph problem - every index is a vertex and every edge is a completed word
        # The problem thus boils down to if a path exists.
        from collections import deque
        queue = deque()
        visited = []
        queue.appendleft(0)
        visited.append(0)
        while queue:
            cur = queue.pop()
            for i in range(cur, len(s)+1):
                if i in visited:
                    continue
                if s[cur: i] in wordDict:
                    if i == len(s):
                        return True
                    queue.appendleft(i)
                    visited.append(i)
        return False

obj = Solution()
print (obj.wordBreak1("catsandog",
["cats","dog","sand","and","cat"]))
