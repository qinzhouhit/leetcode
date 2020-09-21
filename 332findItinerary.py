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
        # heapq (priotirty queue -> smallest lexcial order)
        for flight in tickets:
            origin, destination = flight[0], flight[1]
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
            path.append(origin)
                
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

    # iterative
    def findItinerary1(self, tickets: List[List[str]]) -> List[str]:
        targets = collections.defaultdict(list)
        for a, b in sorted(tickets)[::-1]:
            targets[a] += b,
        route, stack = [], ['JFK']
        while stack:
            while targets[stack[-1]]:
                stack += targets[stack[-1]].pop(),
            route += stack.pop(),
        return route[::-1]


    
    