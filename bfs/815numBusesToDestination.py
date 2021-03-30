'''keys: Solutions:Similar: T:S:'''from typing import Listimport collectionsclass Solution:    # T: O(sum((N - i)*bi) + N^2), N as number of buses,    # bi as the numebr of stops on i-th bus. route map construct + bfs    # O(sum((N - i)*bi)) for the graph construction, O(N^2) for the bfs    # S: O(N^2 + sum(bi))    # https://leetcode.com/problems/bus-routes/discuss/122771/C%2B%2BJavaPython-BFS-Solution    def numBusesToDestination(self, routes: List[List[int]], S: int, T: int) -> int:        # using defaultdict(list) is also fine        graph = collections.defaultdict(list)        for idx, route in enumerate(routes):            for station in route:                graph[station].append(idx) #                         queue = [(S, 0)] # 0 for the ct        seen = set([S]) # no need to check one stop twice        for stop, ct in queue:            if stop == T:                return ct            for route_idx in graph[stop]:                for station in routes[route_idx]:                    if station not in seen:                        seen.add(station)                        queue.append((station, ct+1))                routes[route_idx] = []# this line is important to reduce time                # it eliminates seen route, since no need to switch back to this line        return -1    # official    def numBusesToDestination1(self, routes, S, T):        if S == T: return 0        routes = map(set, routes)        graph = collections.defaultdict(set)        for i, r1 in enumerate(routes):            for j in range(i+1, len(routes)):                r2 = routes[j]                if any(r in r2 for r in r1):                    graph[i].add(j)                    graph[j].add(i)        seen, targets = set(), set()        for node, route in enumerate(routes):            if S in route: seen.add(node)            if T in route: targets.add(node)        queue = [(node, 1) for node in seen]        for node, depth in queue:            if node in targets: return depth            for nei in graph[node]:                if nei not in seen:                    seen.add(nei)                    queue.append((nei, depth+1))        return -1            