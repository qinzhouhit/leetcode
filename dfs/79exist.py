'''
keys: backtracking
Solutions:
Similar:
T: O(n * m * len(word));
O(n^3) in the worst case. Ex. [[A, A], [A, A]] and word='AAAAA'
S: O(1)
'''
from typing import List


class Solution:
    # T: O(N*3^L), N the number of cells in the board and L the length of word
    def exist(self, board, word):
        if not board:
            return False
        for r in range(len(board)): # O(N) for the two for loops here
            for c in range(len(board[0])):
                if self.helper(board, word, r, c):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def helper(self, board, word, r, c):
        if len(word) == 0: # all the characters are checked
            return True
        if not (0 <= r < len(board) and 0 <= c < len(board[0]) and word[0] == board[r][c]):
            return False
        # store the value in tmp: You change the coordinate at (i,j)
        # in the next loop but change it back in the current loop,
        # so definitely there would always be only one vacant symbol,
        # which avoids the danger of 'going back' problem.
        # cases like [['a','a'],[,'a','b']] "baaab"
        tmp = board[r][c] # first character is found, check the remaining part
        board[r][c] = "#" # avoid visit again, we need it since each char can be used once
        # check whether can find "word" along one direction
        # he or statement in posted code returns immediately once either
        # up, down, left, right returns true
        res =  self.helper(board, word[1:], r+1, c) or \
            self.helper(board, word[1:], r, c+1) or \
            self.helper(board, word[1:], r-1, c) or \
            self.helper(board, word[1:], r, c-1)
        board[r][c] = tmp
        return res
    
    ######
    # 
    def exist(self, board, word):
        self.ROWS = len(board)
        self.COLS = len(board[0])
        self.board = board

        for row in range(self.ROWS):
            for col in range(self.COLS):
                if self.backtrack(row, col, word):
                    return True
        # no match found after all exploration
        return False


    def backtrack(self, row, col, suffix):
        # bottom case: we find match for each letter in the word
        if len(suffix) == 0:
            return True
        # Check the current status, before jumping into backtracking
        if row < 0 or row == self.ROWS or col < 0 or col == self.COLS \
                or self.board[row][col] != suffix[0]:
            return False
        # mark the choice before exploring further.
        self.board[row][col] = '#'
        # explore the 4 neighbor directions
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            if self.backtrack(row + rowOffset, col + colOffset, suffix[1:]):
                return True
        # revert the change
        self.board[row][col] = suffix[0]
        # Tried all directions, and did not find any match
        return False



obj=Solution()
print(obj.exist([["C","A","A"],["A","A","A"],["B","C","D"]],
                "AAB"))


