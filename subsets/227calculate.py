'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List
# https://leetcode.com/problems/basic-calculator-ii/discuss/63076/Python-short-solution-with-stack.
# no parenthesis but with +/-/*//

class Solution:
	# O(n) for S and T
	def calculate(self, s: str) -> int:
		if s is None: return 0
		num = 0; stack = []; res = 0; prev_sign = "+"
		for i, cur in enumerate(s):
			if cur.isdigit():
				num = num*10 + int(cur) # consecutive digits
			if (cur in "+-*/" or i == len(s) - 1): # i == len(s)-1, e.g., "42"
				if prev_sign == "-":
					stack.append(-num)
				elif prev_sign == "+":
					stack.append(num)
				elif prev_sign == "*":
					stack.append(stack.pop()*num)
				elif prev_sign == "/":
					stack.append(int(float(stack.pop())/num))
				prev_sign = cur
				num = 0
		return sum(stack)

obj = Solution()
print (obj.calculate("42"))
