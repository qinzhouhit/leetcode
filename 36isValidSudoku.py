class Solution:
    def isValidSudoku(self, board):
        return (self.isRowValid(board) and
                self.isColValid(board) and
                self.isSquareValid(board))

    def isRowValid(self, board):
        for row in board:
            if not self.isUnitValid(row):
                return False
        return True

    def isColValid(self, board):
        for col in zip(*board):
            if not self.isUnitValid(col):
                return False
        return True

    def isSquareValid(self, board):
        for i in [0,3,6]:
            for j in [0,3,6]:
                square=[board[x][y] for x in range(i,i+3) for y in range(j, j+3)]
                if not self.isUnitValid(square):
                    return False
        return True

    def isUnitValid(self,unit):
        unit=[i for i in unit if i!="."]
        return len(set(unit))==len(unit)

