""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	# https://leetcode.com/problems/where-will-the-ball-fall/discuss/988576/JavaC%2B%2BPython-Solution-with-Explanation
	# O(rows * cols) time, because for every column we iterate at most all rows (top to bottom).
	# O(1) additional space. O(grid[0].length) space to store the result.
    def findBall(self, grid: List[List[int]]) -> List[int]:
    	if not grid or len(grid[0]) == 0:
    		return []

    	rows, cols = len(grid), len(grid[0])
    	res = [0] * cols  
    	# each loop computes the result for when dropping a ball in column i.
    	for i in range(cols):
    		curRow = 0; curCol = i
    		while curRow < rows:
    			# We go to the right if the current value and the value 
    			# to the right are both equal to 1.
    			if grid[curRow][curCol] == 1 and curCol + 1 < cols \
    					and grid[curRow][curCol+1] == 1:
    				curRow += 1
    				curCol += 1
    			# We go to the left if the current value and the value to
    			# the left are both equal to -1.
    			elif grid[curRow][curCol] == -1 and curCol >= 1 and \
    					grid[curRow][curCol-1] == -1:
    				curRow += 1
    				curCol -= 1
    			# If we can't move to the left, and we can't move to the right, 
    			# then the ball is stuck because there is no other way to move.
    			else:
    				break
    		res[i] = curCol if curRow == rows else -1  # Store -1 if the ball got stuck.
    	return res

