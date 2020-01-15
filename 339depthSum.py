class Solution:
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
