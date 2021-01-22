'''
keys:
Solutions:
Similar: 1209
T:
S:
'''
from typing import List



class Solution:

	# stack
	# T: O(N), S: O(N-D)
	def removeDuplicates1(self, S: str) -> str:
		res = []
		for c in S:
			if res and c == res[-1]:
				res.pop()
			else:
				res.append(c)
		return "".join(res)


	# two pointers
	# O(N) for S and T
    def removeDuplicates(self, S: str) -> str:
        i = 0 # idx of res list
        n = len(S)
        res = list(S)
        for j in range(n): # j: idx of the input list
        	res[i] = res[j]
        	if i > 0 and res[i-1] == res[i]:
        		i -= 2 # backward by 2 steps
        	i += 1 # done with cur idx
        return "".join(res[:i])