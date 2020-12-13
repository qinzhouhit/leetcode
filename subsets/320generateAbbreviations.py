'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# backtrack, official
	# T: O(n*2^n)
	# keep: concatenating the letter
	# abbreviate: concatenating empty string and keep track of ct of empty string numbers
    def generateAbbreviations(self, word: str) -> List[str]:
    	# no need to pass word into helper
    	def helper(word, pos, cur, ct):
    		if pos == len(word):
    			# Once we reach the end, append current to the result
    			res.append(cur + str(ct) if ct > 0 else cur)
    			return # no need
    		else:
    			# abbreviate current position, and increment count
    			helper(word, pos+1, cur, ct+1)
    			# keep current position/letter, and zero-out count
    			helper(word, pos+1, cur + (str(ct) if ct > 0 else "") + word[pos], 0)

    	res = []
    	helper(word, 0, "", 0)
    	return res
