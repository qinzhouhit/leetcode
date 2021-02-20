'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:

	# similar to next permutation
	# T: O(m), m as number of digits in the number
	def nextGreaterElement(self, n: int) -> int:
		digits = list(str(n))
		i = len(digits) - 1
		while i >= 1 and digits[i-1] >= digits[i]:
			i -= 1
		if i == 0: # all digits decreasing
			return -1
		j = i
		while j < len(digits)-1 and digits[j+1] > digits[i-1]:
			j += 1 # try to find the last ascending number in the decreasing subarrary
		digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1] # reverse the updated decreasing subarray
        ret = int(''.join(digits))
        
        return ret if ret < 1<<31 else -1



	# super naive solution, get all permutations and sort
	# O(n!)
    def nextGreaterElement(self, n: int) -> int:





        