'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List

'''
Given 2 segment (left1, right1), (left2, right2), how can we check whether they overlap?
If these two intervals overlap, it should exist an number x,

left1 < x < right1 && left2 < x < right2

left1 < x < right2 && left2 < x < right1

left1 < right2 && left2 < right1

This is the sufficient and necessary condition for two segments overlap.
'''

class Solution:
	# passed all cases
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    	lx1, by1, rx1, ty1 = rec1
        lx2, by2, rx2, ty2 = rec2
        # width overlap: horizontal distance between lesser of the right edges 
        # and greater of the left edges
        width = min(rx1, rx2) - max(lx1, lx2)
        height = min(ty1, ty2) - max(by1, by2)
        return width > 0 and height > 0


        
	# O(1) for S and T
	# fails for this case:
	# [-1,0,1,1]
	# [0,-1,0,1]
	def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
    	# lx2 >= rx1 or lx1 >= rx2 or ly1 >= ry2 or ly2 >= ry1
    	# lx2: left bottom x-val of rec2
     	return not (rec1[0] >=rec2[2] or rec2[0]>=rec1[2] or rec1[1]>=rec2[3] or rec2[1]>=rec1[3])


    


