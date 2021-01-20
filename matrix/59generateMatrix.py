'''
keys:
Solutions:
Similar: 54
T:
S:
'''


# T: O(n^2)
# S: O(1)
class Solution:
	# https://leetcode.com/problems/spiral-matrix-ii/discuss/22290/Python-easy-to-follow-solution.
	# from outside to inside
	def generateMatrix1(self, n: int) -> List[List[int]]:
		m = [[None]*n for _ in range(n)]
		l, r, top, down = 0, n-1, 0, n-1
		nums = iter([v for v in range(1, n**2 + 1)])
		while l <= r and top <= down:
			for col in range(l, r+1):
				m[top][col] = next(nums)
			top += 1

			for row in range(top, down+1):
				m[row][r] = next(nums)
			r -= 1

			for col in range(r, l-1, -1):
				m[down][col] = next(nums)
			down -= 1

			for row in range(down, top-1, -1):
				m[row][l] = next(nums)
			l += 1
		return m



	# https://leetcode.com/problems/spiral-matrix-ii/discuss/22282/4-9-lines-Python-solutions
    def generateMatrix(self, n):
        A, lo = [], n*n+1
        while lo > 1:
            lo, hi = lo - len(A), lo
            A = [list(range(lo, hi))] + \
                [list(i) for i in zip(*A[::-1])]
        return A

obj=Solution()
print (obj.generateMatrix(3))