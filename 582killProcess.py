'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:


	# self-made
	# O(n) for S and T, n as the number of nodes
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        g = collections.defaultdict(list) # parent to child
        for child, parent in zip(pid, ppid):
        	g[parent].append(child)

        stack = [kill] # should use deque since bfs for the n-ary tree level order traversal
        res = []
        while stack:
        	node = stack.pop()
        	res.append(node)
        	for child in g[node]:
        		stack.append(child)

        return res
