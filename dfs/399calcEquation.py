'''keys: Solutions:Similar: T:S:'''from typing import Listfrom collections import defaultdict, dequeimport collectionsclass Solution:        # DFS, huahua, O(e + q*e), q as query, e as edge    # S: O(e)    def calcEquation2(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        def helper(s, e, visited): # O(e*q)            if s == e:                return 1.0            visited.add(s)            for mid_node in graph[s]: # s/mid                if mid_node in visited:                    continue                visited.add(mid_node)                tmp = helper(mid_node, e, visited) # mid/e                if tmp > 0:                    return graph[s][mid_node] * tmp # s/mid * mid/e            return -1.0                graph = collections.defaultdict(dict)        for (s, e), val in zip(equations, values): # O(e)            graph[s][e] = val            graph[e][s] = 1/val        return [helper(s, e, set()) if s in graph and e in graph else -1 for s, e in queries]                            # simply build the graph with given equations,     # and traverse the graph, either DFS or BFS, to find a path    # for a given query, and the result is the product of costs of     # edges on the path.        '''    One optimization, which is not implemented in the code, is to "compress"    paths for past queries, which will make future searches faster. This is     the same idea used in compressing paths in union find set.     So after a query is conducted and a result is found, we add two edges    for this query if these edges are not already in the graph.    Given the number of variables N, and number of equations E, building     the graph takes O(E), each query takes O(N), space for graph takes O(E)    '''    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        graph = {}        def build_graph(equations, values):            def add_edge(f, t, edge):                if f in graph:                    graph[f].append((t, value))                else:                    graph[f] = [(t, value)]                        for vertices, value in zip(equations, values):                x, y = vertices                add_edge(x, y, value)                add_edge(y, x, 1/value)                def find_path(query): # bfs            a, b = query                        if a not in graph or b not in graph:                return -1.0                            q = collections.deque([(a, 1.0)])            visited = set()                        while q:                front, cur_product = q.popleft()                if front == b:                    return cur_product                visited.add(front)                for neighbor, value in graph[front]:                    if neighbor not in visited:                        q.append((neighbor, cur_product*value))            return -1.0                build_graph(equations, values)        return [find_path(q) for q in queries]                        # official    # T: O(M*N), M as number of queries, N as number of input equations    # S: OO(N), O(N) for the graph; for recursion stack; for visited    def calcEquation4(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        graph = defaultdict(defaultdict)        def backtrack_evaluate(curr_node, target_node, acc_product, visited):            visited.add(curr_node)            ret = -1.0            neighbors = graph[curr_node]            if target_node in neighbors:                ret = acc_product * neighbors[target_node]            else:                for neighbor, value in neighbors.items():                    if neighbor in visited:                        continue                    ret = backtrack_evaluate(                        neighbor, target_node, acc_product * value, visited)                    if ret != -1.0:                        break            visited.remove(curr_node)            return ret        # Step 1). build the graph from the equations        for (dividend, divisor), value in zip(equations, values):            # add nodes and two edges into the graph            graph[dividend][divisor] = value            graph[divisor][dividend] = 1 / value        # Step 2). Evaluate each query via backtracking (DFS)        #  by verifying if there exists a path from dividend to divisor        results = []        for dividend, divisor in queries:            if dividend not in graph or divisor not in graph:                # case 1): either node does not exist                ret = -1.0            elif dividend == divisor:                # case 2): origin and destination are the same node                ret = 1.0            else:                visited = set()                ret = backtrack_evaluate(dividend, divisor, 1, visited)            results.append(ret)        return results    # optimized as suggested    # iterative bfs    # https://leetcode.com/problems/evaluate-division/discuss/88275/Python-fast-BFS-solution-with-detailed-explantion    def calcEquation1(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:        graph = defaultdict(dict) # dict of dict        for [x,y],value in zip(equations, values): # O(N)            graph[x][y] = value            graph[y][x] = 1/value                def find_prod(s, e): # bfs # for each equation, may search the whole graph            if s not in graph or e not in graph:                return -1.0            if s == e: return 1.0            q = deque([s, 1.0]) # node, cur_val            visited = set(s)            while q:                node, curr = q.popleft()                for child, val in graph[node].items():                    if child in visited:                        continue                    newVal = curr * val                    if child == e:                        return newVal                    graph[s][child] = newVal                    graph[child][s] = 1/newVal                    visited.add(child)                    q.append((child, newVal))            return -1.0                    return [find_prod(s, e) for s, e in queries] # s/e, start, end                        sol = Solution()print (sol.calcEquation2([ ["a", "b"], ["b", "c"] ], [2.0, 3.0], \      [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ]))