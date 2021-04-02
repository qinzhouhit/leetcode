'''
keys:
Solutions:
Similar:
So total space is "rows array + columns array + two diagnals": O(n+n+1+1)==O(n)
For each move, time checking current row, column, and two diagnals takes O(1+1+1+1)==O(1)
'''
# an incremental job
# https://leetcode.com/problems/design-tic-tac-toe/discuss/81908/Python-solution-with-detailed-explanation

class TicTacToe:

    def __init__(self, n: int):
        """
        Initialize your data structure here.
        """
        self.row = [0]*n
        self.col = [0]*n
        self.diag = 0
        self.anti_diag = 0
        self.n = n

    # notice the n marks do not have to be consecutive, i.e., just care about cumulative
    def move(self, row: int, col: int, player: int) -> int:
        """
        Player {player} makes a move at ({row}, {col}).
        @param row The row of the board.
        @param col The column of the board.
        @param player The player, can be either 1 or 2.
        @return The current winning condition, can be either:
                0: No one wins.
                1: Player 1 wins.
                2: Player 2 wins.
        """
        # Record the number of moves for each rows, columns, and two diagonals.
        # For each move, we -1 for each player 1's move and +1 for player 2's move.
        # Then we just need to check whether any of the recored numbers equal to n or -n.
        offset = player * 2 - 3 # -1 for player 1 and 1 for player 2
        self.row[row] += offset
        self.col[col] += offset
        if row == col:
            self.diag += offset
        if row + col == self.n - 1: # anti diagonal
            self.anti_diag += offset
        if self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 2
        if -self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
            return 1
        return 0
        # # last five rows can be, since only the current player can win
        # if offset * self.n in [self.row[row], self.col[col], self.diag, self.anti_diag]:
        #     return player
        # return 0



# Your TicTacToe object will be instantiated and called as such:
# obj = TicTacToe(n)
# param_1 = obj.move(row,col,player)
