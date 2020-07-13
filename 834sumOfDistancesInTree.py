'''keys: graphSolutions:Similar: T:S:'''from typing import Listimport collectionsclass Solution:    # subtree sum and count    # O(N) for S and T, N as nodes number    def sumOfDistancesInTree(self, N: int, edges: List[List[int]]) -> List[int]:        graph = collections.defaultdict(set)        for u, v in edges:            graph[u] = v            graph[v] = u                count = [1] * N        ans = [0] * N                def dfs(node = 0, parent = None):            for child in graph[node]:                if child != parent:                    dfs(child, node)                    count[node] += count[child]                    ans[node] += ans[child] + count[child]                            def dfs2(node = 0, parent = None):            for child in graph[node]:                if child != parent:                    ans[child] = ans[node] - count[child] + N - count[child]                    dfs2(child, node)                dfs()        dfs2()        return ans