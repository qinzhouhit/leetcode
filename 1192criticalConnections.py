'''
keys: regex
Solutions:
Similar:
T:
S:
'''

# https://www.youtube.com/watch?v=mKUsbABiwBI&t=661s
import collections
class Solution:
    # T: O(n), S: O(n)
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        # construct the graph
        graph = collections.defaultdict(set)
        for u, v in connections:
            graph[u].add(v)
            graph[v].add(u)

        jump = [-1]*n # the minimum step of each node
        # starting from the current node, explore all the node connecting to this node
        # except for its parents (avoid infinite loop)
        # return the mininum value node (return the value, not the node itself)
        def dfs(cur, parent, level, jump, res, graph):
            '''
            :param cur: current node
            :param parent: parent node
            :param level: current # of steps
            :param jump: minimum step of each node
            :param res: critical connection
            :param graph:
            :return: the minimum # of steps for the cur node
            '''
            jump[cur] = level + 1 # current dfs depth
            for child in graph[cur]:
                if child == parent:
                    continue
                elif jump[child] == -1: # never visited before, so visit
                    # the min step of cur node is the min step of the children nodes
                    jump[cur] = min(jump[cur], dfs(child, cur, level+1, jump, res, graph))
                else: # visited before, no need to visit again
                    jump[cur] = min(jump[cur], jump[child])

            if jump[cur] == level + 1 and cur != 0: # the depth does not change after the exploration
                res.append([parent, cur])
            return jump[cur]

        res = []
        dfs(0, -1, 0, jump, res, graph)
        return res


    # TODO: method2
    # https://leetcode.com/problems/critical-connections-in-a-network/discuss/410345/Python-(98-Time-100-Memory)-clean-solution-with-explanaions-for-confused-people-like-me
    def criticalConnections1(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = [[] for _ in range(n)]  ## vertex i ==> [its neighbors]

        currentRank = 0  ## please note this rank is NOT the num (name) of the vertex itself, it is the order of your DFS level

        lowestRank = [i for i in range(
            n)]  ## here lowestRank[i] represents the lowest order of vertex that can reach this vertex i

        visited = [False for _ in range(n)]  ## common DFS/BFS method to mark whether this node is seen before

        ## build graph:
        for connection in connections:
            ## this step is straightforward, build graph as you would normally do
            graph[connection[0]].append(connection[1])
            graph[connection[1]].append(connection[0])

        res = []
        prevVertex = -1  ## This -1 a dummy. Does not really matter in the beginning.
        ## It will be used in the following DFS because we need to know where the current DFS level comes from.
        ## You do not need to setup this parameter, I setup here ONLY because it is more clear to see what are passed on in the DFS method.

        currentVertex = 0  ## we start the DFS from vertex num 0 (its rank is also 0 of course)
        self._dfs(res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex)
        return res

    def _dfs(self, res, graph, lowestRank, visited, currentRank, prevVertex, currentVertex):

        visited[currentVertex] = True
        lowestRank[currentVertex] = currentRank

        for nextVertex in graph[currentVertex]:
            if nextVertex == prevVertex:
                continue  ## do not include the the incoming path to this vertex since this is the possible ONLY bridge (critical connection) that every vertex needs.

            if not visited[nextVertex]:
                self._dfs(res, graph, lowestRank, visited, currentRank + 1, currentVertex, nextVertex)
            # We avoid visiting visited nodes here instead of doing it at the beginning of DFS -
            # the reason is, even that nextVertex may be visited before, we still need to update my lowestRank using the visited vertex's information.

            lowestRank[currentVertex] = min(lowestRank[currentVertex], lowestRank[nextVertex])
            # take the min of the current vertex's and next vertex's ranking
            if lowestRank[
                nextVertex] >= currentRank + 1:  ####### if all the neighbors lowest rank is higher than mine + 1, then it means I am one connecting critical connection ###
                res.append([currentVertex, nextVertex])



