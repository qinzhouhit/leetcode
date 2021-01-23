'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# sortedDict(), similar to treemap
class Leaderboard:

    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:

        # The scores dictionary simply contains the mapping from the
        # playerId to their score. The sortedScores contain a BST with 
        # key as the score and value as the number of players that have
        # that score.     
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            preScore = self.scores[playerId]
            val = self.sortedScores.get(-preScore)
            if val == 1:
                del self.sortedScores[-preScore]
            else:
                self.sortedScores[-preScore] = val - 1    
            
            newScore = preScore + score;
            self.scores[playerId] = newScore
            self.sortedScores[-newScore] = self.sortedScores.get(-newScore, 0) + 1
        
    def top(self, K: int) -> int:
        count, total = 0, 0;

        for key, value in self.sortedScores.items():
            times = self.sortedScores.get(key)
            for _ in range(times): 
                total += -key;
                count += 1;
                
                # Found top-K scores, break.
                if count == K:
                    break;
                
            # Found top-K scores, break.
            if count == K:
                break;
        
        return total;

    def reset(self, playerId: int) -> None:
        preScore = self.scores[playerId]
        if self.sortedScores[-preScore] == 1:
            del self.sortedScores[-preScore]
        else:
            self.sortedScores[-preScore] -= 1
        del self.scores[playerId];




# heap for top function
# S: O(N+K), N for dict and K for heap
class Leaderboard1:

    def __init__(self):
        self.scores = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = 0 
        self.scores[playerId] += score
    # O(K)+O(NlogK) = O(NlogK). It takes O(K) to construct the initial heap and then 
    # for the rest of the N−K elements, we perform the extractMin and 
    # add operations on the heap each of which take
    def top(self, K: int) -> int:
        # This is a min-heap by default in Python.
        heap = []
        for x in self.scores.values():
            heapq.heappush(heap, x)
            if len(heap) > K:
                heapq.heappop(heap)
        res = 0
        while heap:
            res += heapq.heappop(heap)
        return res

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0



# naive. S: O(N) by the score dict
class Leaderboard:

    def __init__(self):
        self.scores = {}

    # T: O(1)
    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
        else:
            self.scores[playerId] += score
    # T: O(NlogN), N represents the total number of players
    def top(self, K: int) -> int:
    	# key=itemgetter(1) <=> key=lambda x:x[1] # notice that x[0] is the key
        tmp = sorted(self.scores.items(), key=itemgetter(1), reverse=True)
        # this only returns the scores instead of tuples
        # tmp = [v for _, v in sorted(self.scores.items(), key=lambda item: item[1], reverse=True)]
        res = 0
        for player, score in tmp:
            if K:
                res += score
                K -= 1
        return res
    # T: O(1)
    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0

        


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)