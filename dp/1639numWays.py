'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# dfs with cache
	# https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/discuss/917694/JavaPython-Top-Down-DP-Clean-and-Concise-O(m*n)
    # S and T: O(m*n), where m is words[i].length and n is target.length
    def numWays(self, words: List[str], target: str) -> int:
        M = 10 ** 9 + 7
        wordsNum, targetLen = len(words[0]), len(target)
        dp = [[0] * wordsNum for _ in range(26)]
        for word in words:
        	for idx, c in enumerate(word):
        		# idx here is the index of word, also index of the 
        		dp[ord(c)-ord("a")][idx] += 1 # frequence of char c at index "idx"

        @lru_cache(maxsize=None)
        def helper(wordIdx, idx):
        	if idx == targetLen:
        		return 1
        	if wordIdx == wordsNum:
        		return 0
        	cur_c = target[idx]
        	res = helper(wordIdx+1, idx) # skip wordIdx-th word
        	if dp[ord(cur_c)-ord("a")][wordIdx] > 0: # 
        		res += helper(wordIdx+1, idx+1) * dp[ord(cur_c)-ord("a")][wordIdx]
        		res %= M
        	return res

        return helper(0, 0) # the 0-th word and 0-th of target


    def numWays(self, words: List[str], target: str) -> int:
    	n, M = len(target), 10**9 + 7
        res = [1] + [0] * n
        for i in range(len(words[0])):
            count = collections.Counter(w[i] for w in words)
            for j in range(n - 1, -1, -1):
                res[j + 1] += res[j] * count[target[j]] % M
        return res[n] % M