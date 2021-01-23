'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83643/Python-solution-with-detailed-explanation


	# >>> using cache, one pass
	def depthSumInverse2(self, nestedList: List[NestedInteger]) -> int:
		



	# >>> get the maxDepth then do the regular weighted sum
	# two pass
	def depth(self, nestedList):
		maxDepth = 1
		for item in nestedList:
			if not item.isInteger():
				maxDepth = max(maxDepth, 1+self.depth(item.getList()))
		return maxDepth

	def helper(self, nestedList, level, maxDepth):
		for item in nestedList:
			if item.isInteger():
				self.res += (maxDepth-level+1) * item.getInteger()
			else:
				self.helper(item.getList, level+1, maxDepth)
		return # one has to return here for the base case

	def depthSumInverse1(self, nestedList: List[NestedInteger]) -> int:
		maxDepth = self.depth(nestedList)
		self.res = 0
		self.helper(nestedList, 1, maxDepth)
		return self.res



		# O(N) for S and T
	def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
		from collections import deque
		queue = deque(nestedList)
		sums = []

		while queue:
			sum_tmp = 0
			for _ in range(len(queue)):
				tmp = queue.popleft()
				if tmp.isInteger():
					sum_tmp += tmp.getInteger()
				else:
					tmp_list = tmp.getList()
					while tmp_list:
						queue.append(tmp_list.pop())
			sums.append(sum_tmp)

		depth = len(sums)

		res = 0
		for ind, val in enumerate(sums):
			dep = depth - ind
			res += dep * val

		return res


	





