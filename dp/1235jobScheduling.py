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
    '''
    Intial dp[0] = 0, as we make profit = 0 at time = 0.
    If we don't do this job, nothing will be changed.
    If we do this job, use binary search in the dp to find the largest profit we 
    can make before start time s.
    So we also know the maximum cuurent profit that we can make doing this job.

    The trick is that we append [ending, p] in dp, and search for s+1 for the right
    position for new task.
    '''
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
    	jobs = sorted(zip(startTime, endTime, profit), key=lambda v: v[1])
        # dp[time] = profit means that within the first time duration,
		# we cam make at most profit money.
        # we need endtime for the binary search
        dp = [[0, 0]] # [endtime, cur_profit]
        for s, e, p in jobs:
        	# If we do this job, binary search in the dp to find the 
        	# largest profit we can make before start time s.
            # s+1 since we store the ENDING time in dps.
            # idx-1 since we are accesing the previous location
            # e.g., bisect.bisect([[1], [2], [4], [10], [5]) = 3
            i = bisect.bisect(dp, [s + 1]) - 1 # use bracket on s+1 since vals in dp are []s
            if dp[i][1] + p > dp[-1][1]: # compare with last element in dp
                dp.append([e, dp[i][1] + p]) # more money, then worth doing, add the pair
        return dp[-1][1]
        