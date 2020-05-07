'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # TODO: bottom up
    def minimumTotal3(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        for r in range(len(triangle)-2, -1, -1):
            for c in range(len(triangle[r])):
                triangle[r][c] += min(triangle[r+1][c], triangle[r+1][c+1])
        return triangle[0][0]


    # TODO: improved DP, make in-place modification
    # O(1) space; triangle[i][j] += min(tri[i-1][j-1], tri[i-1][j])
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    triangle[r][c] += triangle[r-1][c]
                elif c == len(triangle[r])-1:
                    triangle[r][c] += triangle[r-1][c-1]
                else: # for element in row r, the sum comes from the last row r-1
                    # since you can only move right or move down
                    # from the aspect of elements in row c, it's from the element
                    # above it and the element to the upper left.
                    # adjacent: means adjacent in the triangle
                    triangle[r][c] += min(triangle[r-1][c-1], triangle[r-1][c])
        print (triangle)
        return min(triangle[-1])



    # TODO: improved DP, we only have to keep two rows (curr and prev)
    # O(N) space
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        # row 0 for prev calculation, row 1 for current calculation
        res = [[0]*len(triangle) for _ in range(2)]
        res[0][0] = triangle[0][0]
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    res[1][c] = res[0][c] + triangle[r][c]
                elif c == len(triangle[r])-1:
                    res[1][c] = res[0][c-1] + triangle[r][c]
                else: # for element in row r, the sum comes from the last row r-1
                    # since you can only move right or move down
                    # from the aspect of elements in row c, it's from the element
                    # above it and the element to the upper left.
                    # adjacent: means adjacent in the triangle
                    res[1][c] = min(res[0][c-1], res[0][c]) + triangle[r][c]
            tmp = res[0][:] # swap two rows to make the current to the prev row
            res[0][:] = res[1][:]
            res[1][:] = tmp
        print (res)
        return min(res[0])


    # TODO: brutal DP, O(n^2/2) space; T: O(n^2)
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if not triangle:
            return
        res = [[0 for _ in range(len(row))] for row in triangle]
        res[0][0] = triangle[0][0]
        # res[r][c] -> minTotalOfElement(r,c)
        for r in range(1, len(triangle)):
            for c in range(len(triangle[r])):
                if c == 0:
                    res[r][c] = res[r-1][c] + triangle[r][c]
                elif c == len(triangle[r])-1:
                    res[r][c] = res[r-1][c-1] + triangle[r][c]
                else: # for element in row r, the sum comes from the last row r-1
                    # since you can only move right or move down
                    # from the aspect of elements in row c, it's from the element
                    # above it and the element to the upper left.
                    # adjacent: means adjacent in the triangle
                    res[r][c] = min(res[r-1][c-1], res[r-1][c]) + triangle[r][c]
        print (res)
        return min(res[-1])



sol = Solution()
print(sol.minimumTotal2([
    [2],
    [4,3],
    [6,7,5],
    [4,1,8,3]
]))
