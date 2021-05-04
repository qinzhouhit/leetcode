'''
keys: 
Solutions:
Similar: 55
T:
S:
'''
from typing import List


class Solution:
	# BFS, O(N) for S and T
	# return the minimal number of steps to 
    def minJumps(self, arr: List[int]) -> int:
    	n = len(arr)
    	if n <= 1:
    		return 0

    	# construct the graph
    	g = {} # graph
    	for i, val in enumerate(arr):
    		if val in g:
    			g[val].append(i)
    		else:
    			g[val] = [i]

    	# 
        