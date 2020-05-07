'''
keys:
Solutions:
Similar:
T:
S:
'''

class Solution:
    # TODO: DP
    # T: O(numRows^2)
    # S: O(numRows^2)
    def generate(self, numRows: int) -> List[List[int]]:
        res = []

        # The first and last row elements are always 1.
        for row in range(numRows):
            row = [None]*(row+1)
            row[0], row[-1] = 1, 1

            # Each triangle element is equal to the sum of the elements
            # above-and-to-the-left and above-and-to-the-right.
            for i in range(1, len(row)-1):
                row[i] = res[numRows-1][i-1] + res[numRows-1][i]
            res.append(row)
        return res

