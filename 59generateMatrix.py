class Solution:
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + \
                [list(i) for i in zip(*A[::-1])]
        return A

obj=Solution()
print (obj.generateMatrix(3))
