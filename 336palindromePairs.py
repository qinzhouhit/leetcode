'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

# edge case: empty string

class Solution:
	# check prefix and suffix
	# T: O(n * w^2), n as length of list and w as average word length
	# https://leetcode.com/problems/palindrome-pairs/discuss/79209/Accepted-Python-Solution-With-Explanation
	def palindromePairs2(self, words: List[str]) -> List[List[int]]:
		hashmap = {word: idx for idx, word in enumerate(words)}
		res = []
		for word, idx in hashmap.items():
			n = len(word)
			for j in range(n+1): # idx to split the word
				prefix = word[:j]
				suffix = word[j:]
				if self.isPal(prefix): # then check the suffix
					revSuffix = suffix[::-1]
					# if revSuffix == word then the word itself is a palindrome.
					# We want to skip this case because we know the list of words are unique,
					# otherwise we would double count the number palindrome pairs, e.g., [3, 3] for "s "
					if revSuffix != word and revSuffix in hashmap:
						res.append([hashmap[revSuffix], idx]) # revSuffix + prefix + suffix -> revSuffix + word
				if j != len(word) and self.isPal(suffix): # j == len(word) is the same case as j == 0
					revPrefix = prefix[::-1]
					# # dont need revPrefix != word since j != len(word)
					if revPrefix != word and revPrefix in hashmap: 
						res.append([idx, hashmap[revPrefix]]) # prefix + suffix + revPrefix -> word + revPrefix
		return res





	# brute force, T: O(n^2 * k), n as number of words, k as length of longest word
	# S: O(n^2 + k), worst case n*(n-1) owrds in the output
	# reversed copy of the combined words: 2*k * 2 -> O(k)
    def palindromePairs1(self, words: List[str]) -> List[List[int]]:
    	pairs = []
    	for i, word1 in enumerate(words):
    		for j, word2 in enumerate(words):
    			if i == j:
    				continue
    			combined = word1 + word2
    			if combined == combined[::-1]:
    				pairs.append([i, j])
    	return pairs



    # my version, TLE
   	def palindromePairs(self, words: List[str]) -> List[List[int]]:
        if not words:
            return []
        n = len(words)
        memo = {}
        res = []
        for i in range(n):
            for j in range(i+1, n):
                word1 = words[i]+words[j]
                word2 = words[j]+words[i]
                if word1 not in memo:
                    if self.isPal(word1):
                        memo[word1] = True
                        res.append([i, j])
                    else:
                        memo[word1] = False
                else:
                    if memo[word1] and [i, j] not in res:
                        res.append([i, j])
                        
                if word2 not in memo:
                    if self.isPal(word2):
                        memo[word2] = True
                        res.append([j, i])
                    else:
                        memo[word2] = False
                else:
                    if memo[word2] and [j, i] not in res:
                        res.append([j, i])
        return res
        
    def isPal(self, s1):
        return s1 == s1[::-1]
    
sol = Solution()
print (sol.palindromePairs2(["abcd","dcba"]))