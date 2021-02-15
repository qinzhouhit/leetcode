'''
keys:
Solutions:
Similar:
T:
S:
'''
from collections import *

class Solution:
# https://leetcode.com/problems/nested-list-weight-sum-ii/discuss/83643/Python-solution-with-detailed-explanation


	# >>> brilliant idea
	def depthSumInverse3(self, nestedList: List[NestedInteger]) -> int:
		res, level_sum = 0, 0
		while nestedList:
			nxt_level = []
			for item in nestedList:
				if item.isInteger():
					level_sum += item.getInteger()
				else:
					for subitem in item.getList(): # flatten
						nxt_level.append(subitem)
			# level_sum not rest, so the 1st depth vals will be 
			# calculated multiple times
			nestedList = nxt_level
			res += level_sum 
		return res


	# >>> using cache, one pass
	# cache: k: depth, v: total sum of vals at the same depth
	def helper(self, nestedList, depth, cache):
		self.maxDepth = max(self.maxDepth, depth)
		for item in nestedList:
			if item.isInteger():
				cache[depth] += item.getInteger()
			else:
				self.helper(item.getList(), depth+1, cache)
		# return # no need, since it will return when running out of for loop

	def depthSumInverse2(self, nestedList: List[NestedInteger]) -> int:
		cache, self.maxDepth = defaultdict(int), -1
		self.helper(nestedList, 1, cache) # get maxDepth
		res = 0
		for level, val in cache.items():
			res += val * (self.maxDepth - level + 1)
		return res




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


	





