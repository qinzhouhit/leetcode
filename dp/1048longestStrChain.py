""" 
keys: 
Solutions:
Similar:
T:
S:
"""

from collections import defaultdict

class Solution:
	"""
	Start from a word and delete one character at a time.
	Continue this chain until we come across a word that is not 
	present in the list or is one letter long.
	T: O(N*L^2), N as number of words, L as word length
	S: O(N) for recursion stack
	"""
    def longestStrChain(self, words: List[str]) -> int:

    	def dfs(memo, currentWord):
    		# consider the currentWord as the last word in the word sequence.
    		if currentWord in memo:
    			return memo[currentWord]

    		maxLen = 1
    		# taking one char out of currentWord
    		for i in range(len(currentWord)):  # O(L) here
    			newWord = currentWord[:i] + currentWord[i+1:]  # O(L)
    			if newWord in wordsPresent:
    				curLen = 1 + dfs(memo, newWord)
    				maxLen = max(curLen, maxLen)
    		memo[currentWord] = maxLen
    		return maxLen

    	# store the length of the longest possible word sequence where
    	# the key is the last word in the sequence.
        memo = defaultdict(int)
        wordsPresent = set(words)
        res = 0
        for word in words:  # O(N) here
        	res = max(res, dfs(memo, word))
        return res



    # bottom up
    # T: O(N * logN + N * L^2)
    # S: O(N)
    def longestStrChain1(self, words: List[str]) -> int:
    	dp = dict()
    	words.sort(key=lambda x: len(x))  # O(N * logN)
    	 
    	maxLen = 1

    	for word in words:  # O(N)
    		curLen = 1
    		for i in range(len(word)):  # O(L)
    			predecessor = word[:i] + word[i+1:]  # O(L)
    			prevLen = dp.get(predecessor, 0)
    			curLen = max(curLen, prevLen + 1)
    		dp[word] = curLen
    		maxLen = max(maxLen, curLen)
    	return maxLen











