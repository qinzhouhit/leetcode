'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:

	def solveSudoku(self, board):
		"""
		Do not return anything, modify board in-place instead.
		"""
		if board == None or len(board) < 1 or len(board[0]) < 1:
			return False
		self.solve(board)

	def solve(self, board):
		for row in range(len(board)):
			for col in range(len(board[0])):
				if board[row][col] == ".":
					for i in range(1,10):
						if self.isValid(board, row, col, i):
							board[row][col] = str(i)
							if self.solve(board):
								return True
							else:
								board[row][col] = '.'
					return False # there is empty entry but no suitable i for this entry
		print (board)
		return True

	def isValid(self, board, row, col, i):
		for j in range(0, 9):
			if board[j][col] == str(i):
				return False
			if board[row][j] == str(i):
				return False
			if board[3*(row//3) + j//3][3*(col//3) + j%3] == str(i):
				return False
		return True



test = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
obj = Solution()
obj.solveSudoku(test)


