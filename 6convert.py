'''
keys:
Solutions:
Similar:
T: O(n)
S: O(n)
'''

class Solution:
    def convert1(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        buffer = ['']*numRows
        row, step = 0, 1
        for c in s:
            buffer[row] += c

            if row == 0: # hit the first row, go down
                step = 1
            elif row == numRows - 1: # hit the bottow row, then go up
                step = -1

            row += step
        return "".join(buffer)


    def convert(self, s: str, numRows: int) -> str:
        len_ = len(s)
        buffer = ['']*numRows

        i = 0
        while i < len_:
            for ind in range(numRows): # vertically down
                if i < len_:
                    buffer[ind] += s[i]
                    i += 1
            for ind in range(numRows-2, 0, -1): # obliquely up
                if i < len_:
                    buffer[ind] += s[i]
                    i += 1

        return ''.join(buffer)

obj = Solution()
print (obj.convert("PAYPALISHIRING", 3))
