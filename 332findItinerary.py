'''
keys: graph traversal
Solutions:
Similar:
T:
S:
'''
from typing import List
from heapq import *


class Solution:
    # backtracking + greedy
    # backtracking: exploring all possible combination
    # greedy: with smallest lexical order would have its trial first
    # use priority queue, just like postorder dfs
    # T: (|E|log(|E|/|V|)), O(|E|) for DFS
    # S: O(|V|+|E)
    def findItinerary3(self, tickets: List[List[str]]) -> List[str]:
        
        flights = {}
        # heapq ( -> smallest lexcial order)
        for origin, destination in tickets:
            if origin not in flights:
                flights[origin] = [destination]
            else:
                heappush(flights[origin], destination)
            
            if destination not in flights:
                flights[destination] = []
                
        def dfs(origin):
            destinations = flights[origin]
            while destinations:
                dfs(heappop(destinations)) # the smallest one
            path.append(origin) # append backward from the last one due to recursion
                
        path = []
        dfs("JFK")
        return path[::-1]
    
    # recursive
    # So, the algorithm is to find the end node first and delete the path to
    # this node(backtrack), meanwhile using PriorityQueue to guarantee lexical 
    # order.
    '''
    1. The nodes which have odd degrees (int and out) are the entrance or exit.
    In your example it's JFK and A.
    2. If there are no nodes have odd degrees, we could follow any path without
    stuck until hit the last exit node
    3. The reason we got stuck is because that we hit the exit
    '''
    # https://leetcode.com/problems/reconstruct-itinerary/discuss/78768/Short-Ruby-Python-Java-C%2B%2B
    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route = []
        
        def visit(airport):
            while targets[airport]:
                visit(targets[airport].pop())
            route.append(airport)
            
        visit('JFK')
        return route[::-1]

    # iterative; O(ElogE), E as number of edges
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        # reversed lexical order, so smaller lexical ones will poped out first
        for a, b in sorted(tickets, reverse=True): 
            targets[a].append(b)
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                nxt_stop = targets[stack[-1]].pop() # pop since can be used once and once only
                stack.append(nxt_stop)
            route.append(stack.pop())
        return route[::-1]


    
    