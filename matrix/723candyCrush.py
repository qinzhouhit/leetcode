'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/candy-crush/discuss/191252/Short-Python
	# T: O((R*C)^2), R and C as number of rows and cols, O(R*C) for the scan
	# and repeat
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        if not board:
            return []
        rows, cols = len(board), len(board[0])
        
        while True: # repeat the whole process until nothing in crush set
	        crush = set() # record crushed positions, in the for loop! Empty the crush set each loop
	        for r in range(rows):
	            for c in range(cols):
	                if c > 1 and board[r][c] == board[r][c-1] == board[r][c-2] != 0: # a row
	                    crush |= {(r, c), (r, c-1), (r, c-2)} # union operation of set
	                if r > 1 and board[r][c] == board[r-1][c] == board[r-2][c] != 0:
	                	crush |= {(r, c), (r-1, c), (r-2, c)}

	        # crush, set to 0
	        if not crush: 
	        	break # nothing to crush
	        for r, c in crush:
	        	board[r][c] = 0

	        # drop, drop vals above 0, update the board
	        for c in range(cols):
	        	idx = rows - 1
	        	for r in range(rows-1, -1, -1): # check from the bottom row
	        		if board[r][c]: 
	        			board[idx][c] = board[r][c] # drop and overwrite from the bottom row
	        			idx -= 1
	        	for r in range(idx+1): # for the rest ones above (droppign zeros)
	        		board[r][c] = 0

	    return board



	# >>> 1d candy crush
	# https://leetcode.com/discuss/interview-question/380650/Bloomberg-or-Phone-Screen-or-Candy-Crush-1D
	'''
	Input: "aaabbbacd"
	Output: "acd"
	Explanation:
	1. Remove 3 'a': "aaabbbacd" => "bbbacd"
	2. Remove 3 'b': "bbbacd" => "acd"
	'''
	def candyCrush(self, s: str) -> str:
		if not s:
			return s

		stack = [[s[0], 1]]
		for i in range(1, len(s)):
			if s[i] != s[i-1]:
				if stack[-1][1] >= 3: # k 
					stack.pop()
				if stack and stack[-1][0] == s[i]:
					stack[-1][1] += 1
				else:
					stack.append([s[i], 1])
			else:
				stack[-1][1] += 1
		if stack[-1][1] >= 3:
			stack.pop()

		return "".join(a*b for a, b in stack)









                

