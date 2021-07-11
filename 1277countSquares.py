""" 
keys: 
Solutions:
Similar: 221
T:
S:
"""


class Solution:
	"""
	https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution
	it is hard to think the dp can mean two things?
	dp[i][j] means the size of biggest square with A[i][j] as bottom-right corner.
	dp[i][j] also means the number of squares with A[i][j] as bottom-right corner.
	clear explanation:
	https://leetcode.com/problems/count-square-submatrices-with-all-ones/discuss/441306/JavaC%2B%2BPython-DP-solution
	"""
    def countSquares(self, matrix: List[List[int]]) -> int:
    	res = 0
    	for r in range(len(matrix)):
    		for c in range(len(matrix[0])):
    			if matrix[r][c] > 0 and r > 0 and c > 0:
    				# only when three previous locations are non-zero, then we increase square length
    				# "+1" means if there is combo, then at least the we have the square w/ length as 1
    				# since "matrix[r][c] > 0"
    				matrix[r][c] = min(matrix[r-1][c-1], matrix[r-1][c], matrix[r][c-1]) + 1
    			res += matrix[r][c]  # the previous larger squares or the small square w/ length as 1
    	return res
