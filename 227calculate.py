'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
	def calculate(self, s: str) -> int:
		if s is None: return 0
		num = 0; stack = []; res = 0; sign = "+"
		for i in range(len(s)):
			if s[i].isdigit():
				num = num*10 + int(s[i])
			if (s[i] != " " or i == len(s) - 1):
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
