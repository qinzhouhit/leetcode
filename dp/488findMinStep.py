'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/zuma-game/discuss/221386/Python-DFS-16-lines-very-easy-to-understand/805714
    def findMinStep(self, board: str, hand: str) -> int:
    	
    	def remove(s):
            i = 0
            for j in range(len(s)+1): # len(s) included since we can insert at rightmost pos
                if j == len(s) or s[j] != s[i]:
                    if j - i >= 3:
                        return remove(s[:i]+s[j:]) # notice that it could be removable again...
                    i = j
            return s
        
        @lru_cache(None)
        def dfs(b, h):
            b = remove(b)
            if b and not h: return float('inf')
            if not b: return 0
            
            res = float('inf')
            for i in range(len(b)+1): # same reason, we can insert at rightmost pos
                for j in range(len(h)):
                	# insert h[j] in board and delete h[j] from hand
                    res = min(res, 1 + dfs(b[:i] + h[j] + b[i:], h[:j] + h[j+1:]))
            return res
        
        # # we only need to consider chars appeared in board
        # hand = ''.join(filter(lambda x: x in board, hand))
        res = dfs(board, hand)
        return res if res != float('inf') else -1