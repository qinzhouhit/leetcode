'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# https://leetcode.com/problems/minimum-area-rectangle/discuss/192021/Python-O(N1.5)-80ms
	# T: O(N^2), S: O(N)
    def minAreaRect(self, points: List[List[int]]) -> int:
    	seen = set()
    	res = float("inf")
    	for x1, y1 in points:
    		for x2, y2 in seen:
    			if (x1, y2) in seen and (x2, y1) in seen:
    				area = abs(x1 - x2) * abs(y1 - y2)
    				if area and area < res:
    					res = area
    		seen.add((x1, y1))
    	return res if res < float("inf") else 0
        

    # T: O(N^1.5)
    def minAreaRect1(self, points: List[List[int]]) -> int:
        n = len(points)
        nx = len(set(x for x, y in points))
        ny = len(set(y for x, y in points))
        if nx == n or ny == n:
            return 0

        p = collections.defaultdict(list)
        if nx > ny:
            for x, y in points:
                p[x].append(y)
        else:
            for x, y in points:
                p[y].append(x)

        lastx = {}
        res = float('inf')
        for x in sorted(p):
            p[x].sort()
            for i in range(len(p[x])):
                for j in range(i):
                    y1, y2 = p[x][j], p[x][i]
                    if (y1, y2) in lastx:
                        res = min(res, (x - lastx[y1, y2]) * abs(y2 - y1))
                    lastx[y1, y2] = x
        return res if res < float('inf') else 0



        