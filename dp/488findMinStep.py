'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/zuma-game/discuss/97010/%22short%22-java-solution-beats-98

    # https://leetcode.com/problems/zuma-game/discuss/254300/Right-answer-for-this-questions/805715
    def findMinStep(self, board: str, hand: str) -> int:
    	
    	def remove(s):
            i = 0
            for j in range(len(s)+1): # len(s) included since we can insert at rightmost pos
                if j == len(s) or s[j] != s[i]:
                    if j - i >= 3:
                        return remove(s[:i] + s[j:]) # notice that it could be removable again...
                    i = j
            return s
        
        @lru_cache(None)
        def dfs(b, h):
            b = remove(b)
            if b and not h: 
                return float('inf')
            if not b: 
                return 0
            
            res = float('inf')
            for i in range(len(b)+1): # same reason, we can insert at rightmost pos
                for j in range(len(h)): # choose which ball in hand 
                	# insert h[j] in board and delete h[j] from hand
                    # 1 + dfs: 1 is the added ball?
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res
        
        # # we only need to consider chars appeared in board
        # hand = ''.join(filter(lambda x: x in board, hand))
        res = dfs(board, hand)
        return res if res != float('inf') else -1


    # similar one
    # # https://leetcode.com/problems/zuma-game/discuss/254300/Right-answer-for-this-questions/574796
    
    def findMinStep(self, board: str, hand: str) -> int:
        INF = float('inf')
        def de_dup(board):
            prev_en = 0
            for i, c in enumerate(board):
                if c != board[prev_en]:
                    if i - prev_en >= 3:
                        return de_dup(board[:prev_en] + board[i:])
                    prev_en = i
            return board

        @lru_cache(None)
        def dfs(board, hand):
            board = de_dup(board)
            if board == "#":
                return 0
            board_set = set(board)
            hand = "".join(h for h in hand if h in board_set)
            if not hand:
                return INF 
            ans = INF 
            for i in range(len(board)):
                for h_id, h in enumerate(hand):
                    new_hand = hand[:h_id] + hand[h_id+1:]
                    new_board = board[:i] + h + board[i:]
                    ans = min(ans, 1 + dfs(new_board, new_hand))
            return ans

        ans = dfs(board + "#", hand)
        return ans if ans < INF else -1




