'''
keys:
Solutions: a summary of four calculator questions
https://leetcode.com/problems/basic-calculator-iii/discuss/113592/Development-of-a-generic-solution-for-the-series-of-the-calculator-problems
Similar:
T:
S:
'''
from typing import List
from collections import deque

# with parenthesis and +/-/*//

class Solution:
	# https://leetcode.com/problems/basic-calculator-iii/discuss/127881/Python-O(n)-Solution-using-recursion
	def calculate2(self, s: str) -> int:
		s = s + "@" # placeholder
        def helper(stack, i):
            num = 0
            sign = '+'
            while i < len(s):
                c = s[i]
                if c == " ":
                    i += 1
                    continue
                if c.isdigit():
                    num = 10 * num + int(c)
                    i += 1
                elif c == '(':
                    num, i = helper([], i+1)
                else:
                    if sign == '+':
                        stack.append(num)
                    if sign == '-':
                        stack.append(-num)
                    if sign == '*':
                        stack.append(stack.pop() * num)
                    if sign == '/':
                        stack.append(int(stack.pop() / num))
                    num = 0
                    i += 1
                    if c == ')':
                        return sum(stack), i
                    sign = c 
            return sum(stack)
        
        return helper([], 0)



    # not working
	# T: O(n^2); S: O(n)
    def calculate(self, s: str) -> int:
        res1, operator1 = 0, 1 # level 1 result and operator (+)
        res2, operator2 = 1, 1 # level 1 result and operator (*)
        for i, c in enumerate(s):
        	if c.isdigit():
        		num = int(c)
        		while i + 1 < len(s) and s[i+1].isdigit():
        			num = num * 10 + int(s[i+1])
        			i += 1
        		res2 = res2 * num if operator2 == 1 else res2 // num
        	elif c == "(":
        		j = i
        		ct = 0
        		while i < len(s):
        			if s[i] == "(": ct += 1
        			if s[i] == ")": ct -= 1
        			if ct == 0: break
        			i += 1
        		num = self.calculate(s[j+1:i])
        		res2 = res2 * num if operator2 == 1 else res2 // num
        	elif c == "*" or c == "/":
        		operator2 = 1 if c == "*" else -1
        	elif c == "+" or c == "-":
        		res1 = res1 + operator1 * res2
        		operator1 = 1 if c == "+" else -1
        		res2 = 1; operator2 = 1
        return res1 + operator1 * res2

    # iterative, O(n) for S and T
    def calculate1(self, s: str) -> int:
    	res1, operator1 = 0, 1 # level 1 result and operator (+)
        res2, operator2 = 1, 1 # level 1 result and operator (*)
        stack = []
        for i, c in enumerate(s):
        	if c.isdigit():
        		num = int(c)
        		while i + 1 < len(s) and s[i+1].isdigit():
        			num = num * 10 + int(s[i+1])
        			i += 1
        		res2 = res2 * num if operator2 == 1 else res2 // num
        	elif c == "(":
        		stack.append(res1); stack.append(operator1)
        		stack.append(res2); stack.append(operator2)
        		res1, operator1 = 0, 1 # level 1 result and operator (+)
        		res2, operator2 = 1, 1 # level 1 result and operator (*)
        	elif c == ")":
        		num = res1 + operator1 * res2
        		operator2 = stack.pop(); res2 = stack.pop()
        		operator1 = stack.pop(); res1 = stack.pop()
        		res2 = res2 * num if operator2 == 1 else res2 // num
        	elif c == "*" or c == "/":
        		operator2 = 1 if c == "*" else -1
        	elif c == "+" or c == "-":
        		res1 = res1 + operator1 * res2
        		operator1 = 1 if c == "+" else -1
        		res2 = 1; operator2 = 1
        return res1 + operator1 * res2











