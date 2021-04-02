'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


# """
# This is Sea's API interface.
# You should not implement it, or speculate about its implementation
# """
#class Sea(object):
#    def hasShips(self, topRight: 'Point', bottomLeft: 'Point') -> bool:
#
#class Point(object):
#	def __init__(self, x: int, y: int):
#		self.x = x
#		self.y = y

class Solution(object):
    # O(10logMN)
    '''
    Time complexity: O(n) where n is total number of points inside the rectangle
    T(n) = 4xT(n/4) + O(1)
    Apply master theorem: n^(log(4)4) = n is O(O(1)). So T(n) = O(n)
        '''
	# https://leetcode.com/problems/number-of-ships-in-a-rectangle/discuss/440773/python-divide-and-conquer-with-picture-explanation
	# In order to have no overlap for these four parts, we need to add a center point by 1
	def countShips1(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        def helper(bottom, top):
            if bottom.x > top.x or bottom.y > top.y:
            	return 0
            if (top.x, top.y)  == (bottom.x, bottom.y):     
                return sea.hasShips(top, bottom) # will return 1/0 for True/False
            else:
                if not sea.hasShips(top, bottom):
                	return 0
                x0, y0 = bottom.x, bottom.y
                x1, y1 = top.x, top.y
                center_x, center_y = (x0+x1)//2, (y0+y1)//2
                # lower left, upper right, upper left, lower right
                return helper(bottom, Point(center_x, center_y)) + \
                	helper(Point(center_x+1, center_y+1), top) + \
                	helper(Point(x0, center_y+1), Point(center_x, y1)) + \
                	helper(Point(center_x+1, y0), Point(x1, center_y))
        return helper(bottomLeft, topRight)           


    def countShips(self, sea: 'Sea', topRight: 'Point', bottomLeft: 'Point') -> int:
        res = 0
        if topRight.x > bottomLeft.x and topRight.y > bottomLeft.y and sea.hasShips(topRight, bottomLeft):
        	if topRight.x == bottomLeft.x and topRight.y == bottomLeft.y: # base case
        		return int(sea.hasShips(top, bottom)) 
        	newx = (topRight.x + bottomLeft.x) // 2
        	newy = (topRight.y + bottomLeft.y) // 2
        	res += self.countShips(sea, topRight, Point(newx+1, newy+1)) # upper right
        	res += self.countShips(sea, Point(topRight.x, newy), Point(newx+1, bottomLeft.y)) # lower right
        	res += self.countShips(sea, Point(newx, topRight.y), Point(bottomLeft.x, newy+1)) # upper left
        	res += self.countShips(sea, Point(newx, newy), bottomLeft) # lower left
        return res

