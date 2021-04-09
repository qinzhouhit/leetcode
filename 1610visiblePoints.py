'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/maximum-number-of-visible-points/discuss/877822/Python-clean-sliding-window-solution-with-explanation
	# T: O(nlogn)
	# S: O(n)
    def visiblePoints(self, points: List[List[int]], angle: int, location: List[int]) -> int:
        arr, extra = [], 0
        xx, yy = location 
        
        for x, y in points:
            if x == xx and y == yy:
                extra += 1 # overlapped
                continue
            # inverse of the tangent
            # It returns a value that lies between –pi and pi. This represents 
            # the angle between the positive x-axis and the coordinates (x,y).
            arr.append(math.atan2(y - yy, x - xx)) # radian angle
        
        arr.sort() # sort by angle
        # Note that we need to go around the circle, so we duplicate
        # the array and offset the second half by 2*pi.
        arr = arr + [x + 2.0 * math.pi for x in arr] 
        angle = math.pi * angle / 180 # to radian
        
        l = ans = 0 # two pointers
        for r in range(len(arr)):
            while arr[r] - arr[l] > angle: 
                l += 1
            ans = max(ans, r - l + 1)
            
        return ans + extra



