class Solution:
	def depthSumInverse(self, nestedList):
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
			res += dep*val

		return res


