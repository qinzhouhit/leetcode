'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List



class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        for r in range(len(words)):
        	for c in range(len(words[r])):
        		# notice that the matrix may not be complete
        		if c >= len(words) or r >= len(words[c]) or words[r][c] != words[c][r]:
        			return False
        return True

