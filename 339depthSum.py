'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # T: O(N), N as the total number of nested elements in the input list.
    # S: O(D), D as the maximum level of nesting in the input.
	def depthSum(self, nestedList):
		if len(nestedList) == 0:
			return 0

		stack = []
		res = 0
		for item in nestedList:
			stack.append([item, 1])
		while stack:
			next, d = stack.pop()
			if next.isInteger():
				res += d*next.getInteger()
			else:
				for i in next.getList():
					stack.append((i, d+1))
		return res
