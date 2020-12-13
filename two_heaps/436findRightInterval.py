'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
	# T: O(NlogN), ‘N’ is the total number of intervals.
	# S: O(N)
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        maxStart, maxEnd = [], []
        n = len(intervals)
        res = [0] * n
        for idx in range(n):
        	heappush(maxStart, (-intervals[idx][0], idx))
        	heappush(maxEnd, (-intervals[idx][1], idx))

        for _ in range(n):
        	topEnd, endIdx = heappop(maxEnd)
        	res[endIdx] = -1 # since no right interval for the max end
        	# if the max start larger then topEnd, then it's candidates as right interval
        	if -maxStart[0][0] >= -topEnd: 
        		topStart, startIdx = heappop(maxStart)
        		# there may be more candidates, then keep poping
        		# until condition breaks, then topStart is the closest right interval
        		while maxStart and -maxStart[0][0] >= -topEnd:
        			topStart, startIdx = heappop(maxStart)
        		res[endIdx] = startIdx
        		# put the interval back as it could be the next interval of other intervals
      			heappush(maxStart, (topStart, startIdx))
        return res

    # https://leetcode.com/problems/find-right-interval/discuss/814463/Python-Binary-search-explained
    # sort intervals by starts
	def findRightInterval1(self, intervals: List[List[int]]) -> List[int]:
		ints = sorted([[start, end, idx] for idx, [start, end] in enumerate(intervals))
        starts = [i for i, _, _ in ints]
        res = [-1] * len(starts)
        for i, j, k in ints:
            t = bisect.bisect_left(starts, j)
            if t < len(starts):
                res[k] = ints[t][2]
        return res

