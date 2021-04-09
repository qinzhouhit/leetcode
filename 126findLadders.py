'''
keys:
Solutions:
Similar: 127, 126 returns all solutions, 127 only returns path length
T: O(n*26) -> O(n*26^0.5), l = len(word), n = |wordList|
S: O(n + k*L), k = number of paths, L: length of a path
https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS
https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
'''
from typing import List
import collections
import string

class Solution:
    # bidirection BFS
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) \
                          for c in string.ascii_lowercase]:
                    if y in words:
                        if y == endWord:
                            found = True
                        else:
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        def bt(x):
            return [[x]] if x == endWord else [[x] + rest \
                            for y in tree[x] for rest in bt(y)]
        return bt(beginWord)

    # simple BFS
    def findLadders1(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        if endWord not in wordList:
            return []
    
        wordSet = set(wordList) # faster checks against dictionary
        layer = {}
        # stores current word and all possible sequences how we got to it
        layer[beginWord] = [[beginWord]] # k: destination, v: sequence of transformations

        while layer:
            # returns [] on missing keys, just to simplify code
            newlayer = collections.defaultdict(list) 
            for word in layer:
                if word == endWord: 
                    return layer[word] # return all found sequences
                # change every possible letter and check if it's in dictionary
                for i in range(len(word)): 
                    for c in string.ascii_lowercase:
                        newWord =  word[:i] + c + word[i+1:]
                        if newWord in wordSet:
                        # add new word to all sequences and form new layer element
                            newlayer[newWord] += [j + [newWord] for j in layer[word]] 
            wordSet -= set(newlayer.keys()) # remove from dictionary to prevent loops
            layer = newlayer # move down to new layer, update layer

        return []

sol = Solution()
print (sol.findLadders1("hit", "cog", ["hot","dot","dog","lot","log","cog"]))



