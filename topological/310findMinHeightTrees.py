'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List
from collections import deque

'''
the leaf nodes can not be MHT because its adjacent non-leaf nodes 
will always give an MHT with a smaller height. Suppose node M as root
 gives us a tree with height 5, then adjacent leaf node P as root has height 6.
Since P only connects to the subtree (leaf node), obviously its adjacent
M has height 5.
The height of a tree can be defined as the max distance between the root and all its leaf nodes.
=> Finding out the nodes that are overall close to all other nodes, especially the leaf nodes.
Assertion: For the tree-alike graph, the number of centroids is no more than 2.
=> find the centroid nodes in the graph
'''

class Solution:
	# T and S: O(V+E), V as the total nodes and E as the total number of edges
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 0:
        	return []
        # its in-degrees will be 0 # we need 1
        if n == 1:
        	return [0]

        inDegree = {i: 0 for i in range(n)}
        graph = {i:[] for i in range(n)}

        for node1, node2 in edges:
        	# this is undirected graph
        	graph[node1].append(node2)
        	graph[node2].append(node1)
        	inDegree[node1] += 1
        	inDegree[node2] += 1
        # find all leaves, i.e., in-degree as 1
        leaves = deque()
        for node, ct in inDegree.items():
        	if ct == 1:
        		leaves.append(node)
        # remove leaves level by level to approach the centroids
		# repeat until we have 1 or 2 nodes, i.e., answers
		# any node that already been a leaf can not be root of MHT
		# since its adjacent non-leaf node will always be better
		totalNodes = n
		while totalNodes > 2:
			leavesSize = len(leaves)
			totalNodes -= leavesSize
			for _ in range(leavesSize):
				vertex = leaves.popleft()
				# get the child to change inDegree
				for child in graph[vertex]:
					inDegree[child] -= 1
					if inDegree[child] == 1:
						leaves.append(child)
		return list(leaves)

