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
	# T: O(4^n / sqrt(n)), each valid sequence has at most n steps during the 
	# backtracking procedure
	def generateParenthesis1(self, n: int) -> List[str]:

		def backtrack(s = "", left = 0, right = 0):
			if len(s) == 2 * N:
				res.append(s)
				return
			if left < N:
				backtrack(s+"(", left+1, right)
			if right < left:
				backtrack(s+")", left, right+1)
		res = []
		backtrack()
		return res

	### explicit
	def helper(path, l, r):
            if len(path) == n * 2:
                res.append("".join(path))
                return
            if l < n:
                path.append("(")
                helper(path, l+1, r)
                path.pop()
            if l > r:
                path.append(")")
                helper(path, l, r+1)
                path.pop()
        
        res = []
        helper([], 0, 0)
        return res



	# backtracking
	# T: O(4^n/sqrt(n))??? 2^n combinations and n for concatenating each one
	# S: O(n*2^n), for the output space, 2^n combinations and n for each one
    def generateParenthesis(self, n: int) -> List[str]:

        def generate(p, left, right, parens=[]):
            if left:         
            	generate(p + '(', left-1, right)
            if right > left: 
            	generate(p + ')', left, right-1)
            if not right:    
            	parens += p, # comma for concatenating the whole string
            return parens
        return generate('', n, n)

obj=Solution()
print (obj.generateParenthesis(3))
