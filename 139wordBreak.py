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
    # >>> dfs
    # T: O(n^3)
    # S: O(n)
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        @lru_cache # we dont need word_dict/ s as parameter here
        def wordBreakMemo(s: str, word_dict: FrozenSet[str], start: int):
            if start == len(s):
                return True
            for end in range(start + 1, len(s) + 1): # +1 since it is ending idx
                if s[start:end] in word_dict and wordBreakMemo(s, word_dict, end):
                    return True
            return False
        # you can not use set in lru_cache, then it uses frozenset
        return wordBreakMemo(s, frozenset(wordDict), 0)

    # self-made
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        @lru_cache(None)
        def helper(idx):
            if idx == len(s):
                return True
            for end in range(idx+1, len(s)+1):
                if s[idx:end] in wordDict and helper(end):
                    return True
            return False
        wordDict = frozenset(wordDict)
        return helper(0)


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
    # T: O(N^3), S: O(N)
    # https://leetcode.com/problems/word-break/discuss/43797/A-solution-using-BFS
    def wordBreak(self, s, wordDict):
        # Modeled as a graph problem - every index is a vertex and every edge 
        # is a completed word
        # The problem thus boils down to if a path exists.
        from collections import deque
        wordSet = set(wordDict)
        q = deque([0]) # for starting index 
        visited = set()
        while q:
            start = q.popleft() # idx
            if start in visited:
                continue
            for end in range(start+1, len(s)+1):
                if s[start: end] in wordSet:
                    q.append(end)
                    if end == len(s):
                        return True
                    visited.add(start)
        return False


obj = Solution()
print (obj.wordBreak1("catsandog",
["cats","dog","sand","and","cat"]))
