""" 
keys: 
Solutions:
Similar:
T:
S:
"""


class Solution:
	# https://leetcode.com/problems/valid-square/solution/395688
	# a square can only have 2 different lengths between two points
	# the length of the diagonal, the length of the edge
	# O(1) for S and T
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
    	
    	def dist(pt1, pt2):
    		return (pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2

    	def isSame(pt1, pt2):
    		return pt1[0] == pt2[0] and pt1[1] == pt2[1]

    	if isSame(p1, p2) or isSame(p1, p3) or isSame(p1, p4) or isSame(p2, p3) or \
            isSame(p2, p4) or isSame(p3, p4):
    		return False

    	dists = {dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3), dist(p2, p4), \
    			 dist(p3, p4)}
    	if len(dists) == 2:
    		return True
    	else:
    		return False


   	# https://leetcode.com/problems/valid-square/discuss/103448/Simple-python-solution-by-comparing-distance
   	def validSquare(self, p1, p2, p3, p4):
        if p1 == p2 == p3 == p4: return False
        def dist(x,y):
            return (x[0] - y[0])**2 + (x[1] - y[1])**2
        ls = [dist(p1, p2), dist(p1, p3), dist(p1, p4), dist(p2, p3),\
        		dist(p2, p4), dist(p3, p4)]
        ls.sort()
        if ls[0] == ls[1] == ls[2] == ls[3]:
            if ls[4] == ls[5]:
                return True
        return False