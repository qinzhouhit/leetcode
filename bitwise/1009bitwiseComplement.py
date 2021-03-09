'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# flip bitwise
	# O(1) for S and T
    def bitwiseComplement(self, N: int) -> int:
    	if N == 0:
    		return 1
    	todo, bit = N, 1
    	while todo:
    		# flip current bit
    		N = N ^ bit # xor
    		# prepare for the next round
    		bit = bit << 1
    		todo = todo >> 1
    	return N

    # compute bit length and construct 1-bits bitmask
    from math import log2
    def bitwiseComplement1(self, N: int) -> int:
    	if N == 0: return 1
    	l = floor(log2(N)) + 1
    	bitmask = (1 << l) - 1 # -1 is smart af...
    	# bitmask will be all bits of N as 1, e.g., 1111111...1111
    	return bitmask ^ N
