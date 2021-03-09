'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

class Solution:
	# O(N) for S and T
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        res = []
        for row in A:
            res.append(list(map(lambda x: 0 if x == 1 else 1, row[::-1])))
        return res

    # T: O(N), S: O(1)
    def flipAndInvertImage1(self, A: List[List[int]]) -> List[List[int]]:
    	for row in A:
    		for i in range((len(row) + 1) // 2): # keep this range in mind
    		# ~i is equal to len(row)-i-1
    			row[i], row[~i] = ~row[~i], ~row[i]
    	return A

