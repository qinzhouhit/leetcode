'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

"""
# Definition for a Node.
Recursion could get a bit cumbersome to grasp, if you try to get into 
every call yourself and try to see what's happening. And why look at 
every call when every call does the same thing with different inputs. 
So, you just worry about ONE such call and let the recursion do the rest.
And of course always handle the base case or the termination condition 
of the recursion. Otherwise how would it end? 
"""

from collections import deque
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    # TODO: BFS
    # T: O(N+M), we process each node (N in total) and each edge (M in total)
    # S: O(N), for hash map of visited, and for recursion queue (O(W))
    def cloneGraph1(self, node: 'Node') -> 'Node':
        if not node:
            return node # it should be node, not []!!!

        # Dictionary to save the visited node, key: node of original graph,
        # value: cloned node of cloned graph. This helps to avoid cycles.
        visited = {}

        # Put the first node in the queue
        queue = deque([node])
        # Clone the node and put it in the visited dictionary.
        visited[node] = Node(node.val, [])

        # Start BFS traversal
        while queue:
            # Pop a node say "n" from the from the front of the queue.
            n = queue.popleft()
            # Iterate through all the neighbors of the node
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    # Clone the neighbor and put in the visited, if not present already
                    visited[neighbor] = Node(neighbor.val, [])
                    # Add the newly encountered node to the queue.
                    queue.append(neighbor)
                # If visited, add the clone of the neighbor to the neighbors 
                # of the clone node "n".
                visited[n].neighbors.append(visited[neighbor])

        # Return the clone of the node from visited.
        return visited[node]

class Solution1:
    # TODO: DFS iterative
    def cloneGraph2(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}
        stack = [node]
        visited[node] = Node(node.val, [])
        while stack:
            n = stack.pop()
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                    stack.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        return visited[node]
    
    # DFS, recursive
    def cloneGraph3(self, node):
        if not node:
            return 
        nodeCopy = Node(node.val, [])
        dic = {node: nodeCopy} # k: original, v: cloned
        self.dfs(node, dic)
        return nodeCopy # i.e., dic[node]

    def dfs(self, node, dic):
        for neighbor in node.neighbors:
            if neighbor not in dic:
                neighborCopy = Node(neighbor.val, [])
                dic[neighbor] = neighborCopy
                dic[node].neighbors.append(neighborCopy)
                self.dfs(neighbor, dic)
            else:
                dic[node].neighbors.append(dic[neighbor])


class Solution2:
    # TODO: DFS recursive
    # T: O(N), we process each node only once
    # S: O(N), for hash map of visited, and for recursion stack (O(H))
    # can also have iterative version of DFS with our own stack
    def __init__(self): # or just use visited = {} outside of def cloneGraph
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        # If the node was already visited before.
        # Return the clone from the visited dictionary.
        if node in self.visited:
            return self.visited[node]

        # If not visited, create a clone for the given node.
        # Note that we don't have cloned neighbors as of now, hence [].
        clone_node = Node(node.val, [])

        # The key is original node and value being the clone node.
        self.visited[node] = clone_node

        # Iterate through the neighbors to generate their clones
        # and prepare a list of cloned neighbors to be added to the cloned node.
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node

