'''
keys:
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    # T: O(nlog), S: O(1)
    def canAttendMeetings(self, intervals):
        intervals = sorted(intervals, key = lambda x: x[0])
        for idx, interval in enumerate(intervals):
            if idx == 0:
                continue
            if interval[0] < intervals[idx - 1][1]:
                return False
        return True


    def canAttendMeetings1(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key = lambda x: x.start)

        end = intervals[0].end
        for i in range(1, len(intervals)):
            if end > intervals[i].start:
                return False
            end = intervals[i].end
        return True
