'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List





class Solution:
	# find if there is a single line L parallel to y-axis
	# O(N) for S and T
	# https://leetcode.com/problems/line-reflection/discuss/202760/Bad-problem-description-come-and-read-what-it-really-means.
    def isReflected(self, points: List[List[int]]) -> bool:
        if not points: # very weird...
        	return True 
        points = set([ tuple(p) for p in points]) # there may be repeated points
        all_x = [x for x, y in points]
        mid_x = (min(all_x) + max(all_x))/2
        
        for x, y in points:
            mirror_x = mid_x + (mid_x - x) # (x + mirror_x)/2 = mid_x
            if (mirror_x, y) not in points: 
            	return False
        
        return True