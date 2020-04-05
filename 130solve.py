'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
	def solve(self, board):
		if not any(board):
			return None

		row = len(board); col = len(board[0])

		# check the edges of the board, if "O"(s), mark them as "*"
		for i in range(row):
			self.check(board, i, 0, row, col)
			if col > 1:
				self.check(board, i, col-1, row, col)
		for j in range(col):
			self.check(board, 0, j, row, col)
			if row > 1:
				self.check(board, row-1, j, row, col)

		for i in range(row):
			for j in range(col):
				if board[i][j] == "O":
					board[i][j] = "X"
				if board[i][j] == "1":
					board[i][j] = "O"
		# for j in range(row):
		# 	for j in range(col):
		# 		if board[i][j] == "1":
		# 			board[i][j] = "O"
		print (board)


	def check(self, board, i, j, row, col):
		if board[i][j] == "O":
			board[i][j] = "1"
			if i >= 1:
				self.check(board, i-1, j, row, col)
			if j >= 1:
				self.check(board, i, j-1, row, col)
			if i < row - 1:
				self.check(board, i+1, j, row, col)
			if j < col - 1:
				self.check(board, i, j+1, row, col)

obj = Solution()
obj.solve([["O","O"],["O","O"]])
