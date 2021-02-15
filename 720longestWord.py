'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# https://leetcode.com/problems/longest-word-in-dictionary/discuss/113916/Python%3A-Trie-%2B-BFS
class TrieNode(object):
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.isEnd = False
        self.word = ''
        
class Trie(object):
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
        node.isEnd = True
        node.word = word
    
    def bfs(self): # more like the find function
        q = collections.deque([self.root])
        res = ''
        while q:
            cur = q.popleft()
            for node in cur.children.values():
                if node.isEnd:
                    q.append(node)
                    # length and lexical
                    if len(node.word) > len(res) or node.word < res:
                        res = node.word
        return res 
    
class Solution(object):
    def longestWord(self, words):
        trie = Trie()
        for w in words: 
        	trie.insert(w)
        return trie.bfs()



class Solution:
	# T: O(sum of w_i^2), w_i is the length of words[i]
	# S: same as T for substring creation
	# notice that all prefix must exist
    def longestWord(self, words: List[str]) -> str:
        wordset = set(words)
        words.sort(key = lambda c: (-len(c), c)) # increasing length, lexicographical order
        for word in words:
            if all(word[:k] in wordset for k in range(1, len(word))):
                return word

        return ""


    # >>> official
    # T: O(sum of w_i), w_i is the length of words[i]
    # for build the trie and search it
    # S: O(sum of w_i) for the trie
    def longestWord(self, words: List[str]) -> str:
    	Trie = lambda: collections.defaultdict(Trie)
        trie = Trie()
        END = True

        for i, word in enumerate(words): # this so fancy...
            reduce(dict.__getitem__, word, trie)[END] = i

        stack = trie.values()
        ans = ""
        while stack:
            cur = stack.pop()
            if END in cur:
                word = words[cur[END]]
                if len(word) > len(ans) or len(word) == len(ans) and word < ans:
                    ans = word
                stack.extend([cur[letter] for letter in cur if letter != END])

        return ans