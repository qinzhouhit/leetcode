'''
keys: 
Solutions:
Similar: 
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/discuss/661673/JavaPython-3-Find-the-max-width-and-height./813125
	
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        h = sorted([0] + horizontalCuts + [h])
        w = sorted([0] + verticalCuts + [w])
        x = max(b - a for a, b in zip(h, h[1:]))  # find the max height
        y = max(b - a for a, b in zip(w, w[1:]))  # find the max width
        return x * y % int(1e9+7)