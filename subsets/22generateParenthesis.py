'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:


	# official
	def generateParenthesis1(self, n: int) -> List[str]:

		def backtrack(s = "", left = 0, right = 0):
			if len(s) == 2 * N:
				res.append(s)
				return
			if left < N:
				backtrack(s+"(", left+1, righ)
			if right < left:
				backtrack(s+")", left, right+1)
		res = []
		backtrack()
		return res


	# backtracking
	# T: O(4^n/sqrt(n))??? 2^n combinations and n for concatenating each one
	# S: O(n*2^n), for the output space, 2^n combinations and n for each one
    def generateParenthesis(self, n: int) -> List[str]:
        def generate(p, left, right, parens=[]):
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    parens += p, # comma for concatenating the whole string
            return parens
        return generate('', n, n)

obj=Solution()
print (obj.generateParenthesis(3))
