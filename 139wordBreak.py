'''
keys:
Solutions:
Similar: word break II
T: O(n^2) for both DP and BFS
S: O(n)
'''
from typing import List
import collections

class Solution:
    # d is an array that contains booleans
    # d[i] is True if there is a word in the dictionary that
    # ends at ith index of s AND d is also True at the beginning of the word
    # "leetcode", ["leet", "code"]
    # > d[3] is True because there is "leet" in the dictionary that ends at 
    # 3rd index of "leetcode"
    # > d[7] is True because there is "code" in the dictionary that ends at 
    # the 7th index of "leetcode" AND d[3] is True
    # T: O(l*N), l as len(s) and N as number of words in wordDict
    # https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways
    def wordBreak1(self, s, wordDict):
        d = [False] * len(s)
        for i in range(len(s)):
            for w in wordDict:
                # the trick is that if i+1-len(w)<0, the substring is empty
                if w == s[i+1-len(w):i+1] and (d[i-len(w)] \
                        or (i == (len(w)-1))): # i == len(w)-1: first word
                    d[i] = True
        return d[-1]

    # "nightmare", there are two ways to break it,
    # "night mare" and "nightmare". The graph would be
    # node represents the index of 1st char of the word
    # each edge represents a word
    # 0-->5-->9; graph + BFS, check if path from 0 to 9
    # T: O(N^2), S: O(N)
    # https://leetcode.com/problems/word-break/discuss/43797/A-solution-using-BFS
    def wordBreak(self, s, wordDict):
        # Modeled as a graph problem - every index is a vertex and every edge 
        # is a completed word
        # The problem thus boils down to if a path exists.
        from collections import deque
        queue = deque() # for index 
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
