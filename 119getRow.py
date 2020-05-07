'''
keys:
Solutions:
Similar:
T:
S:
'''

import collections
class Solution:
    # TODO: ultimate DP
    # same ST as below
    def getRow3(self, rowIndex: int): #-> List[int]:
        res = [1]*(rowIndex+1)
        for i in range(1, rowIndex):
            for j in range(i, 0, -1):
                res[j] = res[j] + res[j-1]
        return res


    # TODO: improved DP
    # T: O(k^2), caculating all the previous rows
    # S: O(k), for the lastest generated row
    def getRow2(self, rowIndex: int): #-> List[int]:
        curr, prev = [1], [1]
        for i in range(1, rowIndex+1):
            curr = [1]*(i+1)

            for j in range(1, i):
                curr[j] = prev[j-1] + prev[j]
            prev = curr
        return prev



    # TODO: DP
    cache = collections.defaultdict(int)
    def getRow1(self, rowIndex: int): #-> List[int]:
        res = []
        for i in range(0, rowIndex+1):
            res.append(self.getNum1(rowIndex, i))
        return res

    def getNum1(self, row, col):
        # global cache
        global cache
        if (row, col) in self.cache:
            return self.cache[(row, col)]

        if row == 0 or col == 0 or row == col:
            self.cache[(row, col)] = 1
            return self.cache[(row, col)]

        self.cache[(row, col)] = self.getNum1(row-1, col-1) + self.getNum1(row-1,col)
        return self.cache[(row, col)]


    # TODO: brutal force, TLE
    # T: O(2^k), two branches for recursion
    # S: 2*O(k)->O(k), O(k) for output and O(k) for recursion stack
    def getRow(self, rowIndex: int): #-> List[int]:
        res = []
        for i in range(0, rowIndex+1):
            res.append(self.getNum(rowIndex, i))
        return res

    def getNum(self, row, col):
        if row == 0 or col == 0 or row == col:
            return 1
        return self.getNum(row-1, col-1) + self.getNum(row-1, col)


sol = Solution()
print (sol.getRow2(3))
