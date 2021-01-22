'''
keys:
Solutions:
Similar: 84, 85
T:
S:
'''
from typing import List

# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020708/Python-9-lines-or-Easy-to-understand-explanation-with-pictures-or-Faster-than-100
# https://leetcode.com/problems/largest-submatrix-with-rearrangements/discuss/1020710/C%2B%2B-Clean-and-Clear-With-Intuitive-Pictures-O(m-*-n-*-logn)

class Solution:
	# T: O(m*n*logn), m and n as number of rows and cols
	# S: O(m) or O(1)
	def largestSubmatrix1(self, matrix: List[List[int]]) -> int:
        ans = 0
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if matrix[row][col] != 0 and row > 0:
                    matrix[row][col] += matrix[row - 1][col]

            curr = sorted(matrix[row], reverse=True) 
            print (curr)
            for i in range(len(matrix[0])):
                ans = max(ans, curr[i] * (i + 1))
        
        return ans


	# 
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
    	if not matrix:
    		return 0
    	m, n = len(matrix), len(matrix[0])

    	res = 0
    	heights = [0] * n # n cols
    	for r in range(m):
    		for c in range(n):
    			if matrix[r][c] == 0:
    				heights[c] = 0 # has to reset it due to discontinuity
    			else:
    				heights[c] += 1
    		# sort the pillars
    		tmp = sorted(heights, reverse=True)
    		# calculate max area
    		for c in range(n):
    			res = max(res, (c+1) * tmp[c])
    	return res



        


