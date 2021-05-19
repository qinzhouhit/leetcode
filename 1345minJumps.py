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

    	curs = [0] # store current layers, 0 for idx
    	visited = {0}
    	steps = 0

    	# when cur layer exists
    	while curs:
    		nxt = [] # next layer
    		for node in curs: # node is cur idx
    			if node == n - 1:
    				return steps
	    		# check same value
	    		for nei in g[arr[node]]:
	    			if nei not in visited:
	    				visited.add(nei)
	    				nxt.append(nei)
	    		# clear the list to prevent redundant search
	    		# a.clear(): empty the list
	    		g[arr[node]].clear()
	    		# check neighbors, as defined in the question
	    		for nei in [node-1, node+1]:
	    			if 0 <= nei < len(arr) and nei not in visited:
	    				visited.add(nei)
	    				nxt.append(nei)
    		curs = nxt
    		steps += 1

    	return -1

        