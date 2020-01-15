"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def canAttendMeetings(self, intervals):
        # Write your code here
        intervals = sorted(intervals, key = lambda x: x.start)
        for ind, interval in enumerate(intervals):
            if ind == 0:
                continue
            if interval.start < intervals[ind - 1].end:
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
