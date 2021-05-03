'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:
	# O(N) for T and O(1) for S
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        # pick one index as the target and rotate

        def check(x):
        	'''
        	Return min number of swaps 
            if one could make all elements in A or B equal to x.
            Else return -1.
        	'''
	        rotate_a = rotate_b = 0
	        for i in range(n):
	        	if A[i] != x and B[i] != x:
	        		return -1 # impossible
	        	elif A[i] != x: # and B[i] == x
	        		rotate_a += 1
	        	elif B[i] != x:
	        		rotate_b += 1
	        # rotate_a: number of rotations needed to make A with equal values
	        return min(rotate_a, rotate_b)


	    # we only need to check A[0] and B[0], if not successful,
	    # then it is impossible to do it
	    n = len(A)
	    rotations = check(A[0]) 
	    # If one could make all elements in A or B equal to A[0]
	    if rotations != -1 or A[0] == B[0]:
	    	return rotations
	    else: # If one could make all elements in A or B equal to B[0]
	    	return check(B[0])
