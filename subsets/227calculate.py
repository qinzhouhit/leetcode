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
		num = 0; stack = []; res = 0; sign = "+"
		for i, c in enumerate(s):
			if c.isdigit():
				num = num*10 + int(c)
			if (c != " " or i == len(s) - 1):
				if sign == "-":
					stack.append(-num)
				if sign == "+":
					stack.append(num)
				if sign == "*":
					stack.append(stack.pop()*num)
				if sign == "/":
					stack.append(int(float(stack.pop())/num))
				sign = s[i]
				num = 0
		return sum(stack)

obj = Solution()
print (obj.calculate("42"))
