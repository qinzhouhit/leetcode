'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	'''
	the matrix is symmetrical across its diagonal
	T: O(N*26^L), N = len(words), L = len(word[0])
	the upper bound of the operations would be the total number of 
	nodes in a full-blossom n-ary tree.
	S: O(N*L): O(N*L) for values in prefixHashTable, O(N*L/2) for keys

	'''
    def wordSquares(self, words: List[str]) -> List[List[str]]:

        self.words = words
        self.N = len(words[0]) # length of each word
        self.buildPrefixHashTable(self.words)

        results = []
        word_squares = []
        for word in words:
            word_squares = [word] # try to build new squares with each word
            self.backtracking(1, word_squares, results)
        return results

    def backtracking(self, step, word_squares, results):
        if step == self.N:
            results.append(word_squares[:]) # one solution
            return

        prefix = ''.join([word[step] for word in word_squares])
        candidates = self.prefixHashTable.get(prefix, set([]))
        for candidate in candidates:
            word_squares.append(candidate)
            self.backtracking(step+1, word_squares, results)
            word_squares.pop()

    def buildPrefixHashTable(self, words):
    	# or one can use 
    	# self.prefixHashTable = collections.defaultdict(lambda: set([])), then 
    	# self.prefixHashTable[prefix].add(word)
        self.prefixHashTable = {}
        for word in words:
        	prefixWords = [word[:i] for i in range(1, len(word))]
            for prefix in prefixWords:
            	# k: prefix, v: the original word
                self.prefixHashTable.get(prefix, set([])).add(word) # make the value a dynamic set


# shortened
class Solution:
	def wordSquares(self, words: List[str]) -> List[List[str]]:
        self.N = len(words[0])
        res = []
        self.prefix2words = {}
        for word in words:
            for i in range(1, len(word)):
                prefix = word[:i]
                self.prefix2words.setdefault(prefix, set([])).add(word)
        # print (self.prefix2words)
        
        for word in words:
            squares = [word]
            self.helper(1, squares, res)
        return res
    
    def helper(self, step, squares, res):
        if step == self.N:
            res.append(squares[:])
            return 
        
        prefix = "".join([word[step] for word in squares])
        candidates = self.prefix2words.get(prefix, set())
        for candidate in candidates:
            squares.append(candidate)
            self.helper(step+1, squares, res)
            squares.pop()
        
        
        
        



