'''
keys:
Solutions:
Similar:
T: O(n*26) -> O(n*26^0.5), l = len(word), n = |wordList|
S: O(n + k*L), k = number of paths, L: length of a path
https://leetcode.com/problems/word-ladder-ii/discuss/269012/Python-BFS%2BBacktrack-Greatly-Improved-by-bi-directional-BFS
https://leetcode.com/problems/word-ladder-ii/discuss/40482/Python-simple-BFS-layer-by-layer
'''


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        import string
        import collections
        tree, words, n = collections.defaultdict(set), set(wordList), len(beginWord)
        if endWord not in wordList: return []
        found, q, nq = False, {beginWord}, set()
        while q and not found:
            words -= set(q)
            for x in q:
                for y in [x[:i]+c+x[i+1:] for i in range(n) for c in string.ascii_lowercase]:
                    if y in words:
                        if y == endWord:
                            found = True
                        else:
                            nq.add(y)
                        tree[x].add(y)
            q, nq = nq, set()
        def bt(x):
            return [[x]] if x == endWord else [[x] + rest for y in tree[x] for rest in bt(y)]
        return bt(beginWord)


