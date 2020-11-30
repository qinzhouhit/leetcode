'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List
import bisect

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    	jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # dp[time] = profit means that within the first time duration,
		# we cam make at most profit money.
        dp = [[0, 0]] # [endtime, cur_profit]
        for s, e, p in jobs:
        	# If we do this job, binary search in the dp to find the 
        	# largest profit we can make before start time s.
            i = bisect.bisect(dp, [s + 1]) - 1
            if dp[i][1] + p > dp[-1][1]:
                dp.append([e, dp[i][1] + p])
        return dp[-1][1]
        