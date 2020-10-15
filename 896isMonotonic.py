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
	def isMonotonic2(self, A: List[int]) -> bool:
		increasing = decreasing = True

        for i in range(len(A) - 1):
            if A[i] > A[i+1]:
                increasing = False
            if A[i] < A[i+1]:
                decreasing = False
        
        return increasing or decreasing

	# O(N) for T and O(1) for S
	# with the array [1, 2, 2, 3, 0], 
	# we will see the stream (-1, 0, -1, 1)
	def isMonotonic1(self, A: List[int]) -> bool:
		store = 0
		for i in range(len(A)-1):
			c = (A[i] > A[i+1]) - (A[i] < A[i+1])
			if c: # A[i] > A[i+1]
				if c != store != 0:
					return False
				store = c
		return True

	# O(N) for T and O(1) for S
    def isMonotonic(self, A: List[int]) -> bool:
        return all(A[i]>=A[i+1] for i in range(len(A)-1)) or all(A[i]<=A[i+1] for i in range(len(A)-1))