'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows = len(board)
        if not rows:
        	return 0
        cols = len(board[0])

        ct = 0
        for r in range(rows):
        	for c in range(cols):
        		if board[r][c] == '.': 
        			continue 
        		if r > 0 and board[r-1][c] == 'X':
        			continue
        		if c > 0 and board[r][c-1] == 'X':
        			continue
        		ct += 1
        return ct
