'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List

'''
Topological Sort of a directed graph (a graph with unidirectional edges) 
is a linear ordering of its vertices such that for every directed edge 
(U, V) from vertex U to vertex V, U comes before V in the ordering.

basic concepts:
Source: Any node that has no incoming edge and has only outgoing edges is called a source.
Sink: Any node that has only incoming edges and no outgoing edge is called a sink.
A topological ordering starts with one of the sources and ends at one of the sinks.
A topological ordering is possible only when the graph has no directed cycles,
i.e., a Directed Acyclic Graph (DAG).
We can traverse the graph in a Breadth First Search (BFS) way.
Process: save all sources to a sorted list. We will then remove all sources and 
their edges from the graph. After the removal of the edges, we will have new sources,
 so we will repeat the above process until all vertices are visited.
'''

from collections import deque
# vertices is the number of nodes, edges are a list of [2,1]
# Vertices=7, Edges=[6, 4], [6, 2], [5, 3], [5, 4], [3, 0], [3, 1], [3, 2], [4, 1]

# S and T: O(V+E), ‘V’ is the total number of vertices and 
# ‘E’ is the total number of edges in the graph.
def topological_sort(vertices, edges):
	sortedOrder = []
	if vertices <= 0:
		return sortedOrder

	# initialize the graph
	inDegree = {i: 0 for i in range(vertices)} # count of incoming edges
	graph = {i: [] for i in range(vertices)} # adjacency list graph

	# build the graph
	for edge in edges:
		parent, child = edge[0], edge[1] # 0 -> 1
		graph[parent].append(child)
		inDegree[child] += 1

	# find all source nodes, i.e., 0 inDegree
	sources = deque()
	for k, v in inDegree.items():
		if v == 0:
			sources.append(k)

	# For each source, add it to the sortedOrder and subtract one from all 
	# of its children's in-degrees
  	# if a child's in-degree becomes zero, add it to the sources queue
  	while sources:
  		vertex = sources.popleft()
  		sortedOrder.append(vertex)
  		for child in graph[vertex]:
  			inDegree[child] -= 1
  			if inDegree[child] == 0:
  				sources.append(child)

  	#  If we can’t determine the topological ordering of all the vertices of a
  	#  directed graph, the graph has a cycle in it. 
  	if len(sortedOrder) != vertices: # cycle exists
  		return [] 

  	return sortedOrder











