'''
keys:
Solutions:
Similar:
T: O(n * m * len(word));
O(n^3) in the worst case. Ex. [[A, A], [A, A]] and word='AAAAA'
S: O(1)
'''

class Solution:
    def exist(self, board, word):
        if not board:
            return False
        for i in range(len(board)):
            for j in range(len(board[0])):
                if self.helper(board, i, j, word):
                    return True
        return False

    # check whether can find word, start at (i,j) position
    def helper(self, board, i, j, word):
        if len(word)==0: # all the characters are checked
            return True
        if i<0 or i>=len(board) or j<0 or j>=len(board[0])\
                or word[0]!=board[i][j]:
            return False
        # store the value in tmp: You change the coordinate at (i,j)
        # in the next loop but change it back in the current loop,
        # so definitely there would always be only one vacant symbol,
        # which avoids the danger of 'going back' problem.
        # cases like [['a','a'],[,'a','b']] "baaab"
        tmp=board[i][j] # first character is found, check the remaining part
        board[i][j]="#" # avoid visit again
        # check whether can find "word" along one direction
        # he or statement in posted code returns immediately once either
        # up, down, left, right returns true
        res = self.helper(board, i+1, j, word[1:]) or\
            self.helper(board, i-1, j, word[1:]) or\
            self.helper(board, i, j+1, word[1:]) or\
            self.helper(board, i, j-1, word[1:])
        board[i][j]=tmp
        return res

obj=Solution()
print(obj.exist([["C","A","A"],["A","A","A"],["B","C","D"]],
                "AAB"))


