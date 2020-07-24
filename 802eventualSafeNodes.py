'''
keys: https://leetcode.com/problems/find-eventual-safe-states/discuss/119827/20-line-Python-concise-sol-by-removing-0-out-degree-nodes
Solutions:
Similar: 
T:
S:
'''
from typing import List
import collections

class Solution:

    # reverse edges
    # O(N+E) for T and O(N) for S
    def eventualSafeNodes1(self, graph: List[List[int]]) -> List[int]:
        N = len(graph)
        safe = [False] * N

        graph = map(set, graph)
        rgraph = [set() for _ in range(N)]
        q = collections.deque() # for terminate nodes

        for i, js in enumerate(graph):
            if not js:
                q.append(i)
            for j in js:
                rgraph[j].add(i) # recording edges from i to j

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]: # i: nodes into terminate nodes
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]
        
        
    
    # T: O(nlogn), because of the sort
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        '''
        Find nodes with out degree 0, they are terminal nodes, we 
        remove them from graph and they are added to result
        For nodes who are connected terminal nodes, since terminal 
        nodes are removed, we decrease in-nodes' out degree by 1 and 
        if its out degree equals to 0, it become new terminal nodes
        Repeat 2 until no terminal nodes can be found.

        '''
        n = len(graph)
        out_degree = [0]*n
        in_nodes = collections.defaultdict(list)
        queue = []
        for i in range(n):
            out_degree[i] = len(graph[i])
            if out_degree[i] == 0:
                queue.append(i) # terminate nodes
            for j in graph[i]:
                # edges from i (starting) to j (destination)
                in_nodes[j].append(i) 
        for term_node in queue: # terminate_node
            for in_node in in_nodes[term_node]:
                out_degree[in_node] -= 1
                if out_degree[in_node] == 0:
                    queue.append(in_node)
        return sorted(queue)
                
            
        
        
