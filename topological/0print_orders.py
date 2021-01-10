'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


'''
similar to 207 and 210, but need to print all orders.
There are ‘N’ tasks, labeled from ‘0’ to ‘N-1’. Each task can have 
some prerequisite tasks which need to be completed before it can be
 scheduled. Given the number of tasks and a list of prerequisite pairs,
  write a method to print all possible ordering of tasks meeting all prerequisites.

Input: Tasks=4, Prerequisites=[3, 2], [3, 0], [2, 0], [2, 1]
Output: 
1) [3, 2, 0, 1]
2) [3, 2, 1, 0]
Explanation: There are two possible orderings of the tasks meeting all prerequisites.

Essentially this is to print all orders in topological sort
'''

from collections import deque

# here can be N!N! combinations for ‘N’ numbers, S and T: O(V! * E)
# V as the total number of tasks, E as the number of prerequisites

class Solution:

	res = []
	def print_orders(self, tasks, prerequisites):
		sortedOrder = []
		if tasks <= 0:
			return False

		graph = {i: [] for i in range(tasks)}
		inDegree = {i: 0 for i in range(tasks)}

		for parent, child in prerequisites:
			graph[parent].append(child)
			inDegree[child] += 1

		sources = deque()
		for vertex, ct in inDegree.items():
			if ct == 0:
				sources.append(ct)

		self.helper(graph, inDegree, sources, sortedOrder)
		print (self.res)


	def helper(self, graph, inDegree, sources, sortedOrder):
		if sources:
			for vertex in sources:
				sortedOrder.append(vertex)
				sourcesForNextCall = deque(sources) # a copy of sources
				# only remove the current source, all other sources should remain 
				# in the queue for the next call
				sourcesForNextCall.remove(vertex)
				# process child
				for child in graph[vertex]:
					inDegree[child] -= 1
					if inDegree[child] == 0:
						sourcesForNextCall.append(child)
				# recursive call to print other orderings from the remaining (and new) sources
				self.helper(graph, inDegree, sourcesForNextCall, sortedOrder)
				# backtrack, remove the vertex from the sorted order and put all of its 
				# children back to consider
				# the next source instead of the current vertex
				sortedOrder.remove(vertex)
				for child in graph[vertex]:
					inDegree[child] += 1

		if len(sortedOrder) == len(inDegree):
			print (sortedOrder)
			self.res.append(sortedOrder[:]) # notice that sortedOrder changes

sol = Solution()
sol.print_orders(3, [[0, 1], [1, 2]])
# sol.print_orders(4, [[3, 2], [3, 0], [2, 0], [2, 1]])
# sol.print_orders(6, [[2, 5], [0, 5], [0, 4], [1, 4], [3, 2], [1, 3]])

























