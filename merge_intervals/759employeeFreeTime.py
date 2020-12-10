'''
keys: 
Solutions:
Similar:
T:
S:
'''
from typing import List
from collections import heapq
"""
# Definition for an Interval.
"""
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end


class Solution:
	# maintain the heap
	# T: O(clogN), N as number of employees, C the number of all intervals
	def employeeFreeTime3(self, schedule: '[[Interval]]') -> '[Interval]':
		ans = []
		# 0 means start and 1 means end
        pq = [(emp[0].start, empID, 0) for empID, emp in enumerate(schedule)]
        heapq.heapify(pq)
        # anchor: minimal start time for all employee
        prev_end = pq[0][0]
        while pq: # e_id: employee id; e_jx: current job ID
            start_time, e_id, e_jx = heapq.heappop(pq)
            # no overlap
            if prev_end < start_time:
                ans.append(Interval(anchor, start_time))
            # overlap, update prev_end
            prev_end = max(prev_end, schedule[e_id][e_jx].end)
           	# # if there are more intervals available for the same employee, add their next interval
            if e_jx + 1 < len(schedule[e_id]): # push next job into it
                heapq.heappush(pq, (schedule[e_id][e_jx+1].start, e_id, e_jx+1))

        return ans



	# minheap, still not optimal since all intervals in heap
	# T: O(clogc), N as number of employees, C the number of all intervals
	# S: O(N)
	def employeeFreeTime2(self, schedule: '[[Interval]]') -> '[Interval]':
		res = []
        intervals = [(i.start, i.end) for emp in schedule for i in emp]
        heapify(intervals)

        start, end = heappop(intervals)
        prev_end = end
        while intervals:
            cur_start, cur_end = heappop(intervals)
            if cur_start > prev_end:
                res.append(Interval(prev_end, cur_start))
                prev_end = cur_end
            else:
                prev_end = max(cur_end, prev_end)
        return res



	# T: O(clogc), n as number of all intervals, not optimal
	def employeeFreeTime1(self, schedule: '[[Interval]]') -> '[Interval]':
		intervals = sorted([i for emp in schedule for i in emp], \
			key=lambda x: x.start)
	    res, pre = [], intervals[0]
	    for cur_interval in intervals[1:]:
	    	# overlap, extend/update the prev_end
	        if cur_interval.start <= pre.end and cur_interval.end > pre.end:
	            pre.end = cur_interval.end
	        # no overlap
	        elif cur_interval.start > pre.end:
	            res.append(Interval(pre.end, cur_interval.start))
	            pre = cur_interval
	    return res



	# T: O(clogc), c as number of intervals for all employees
	# S: O(C)
    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
    	OPEN, CLOSE = 0, 1
        events = []
        for emp in schedule:
            for inter in emp:
                events.append((inter.start, OPEN))
                events.append((inter.end, CLOSE))
        events.sort() # sort by keys, one by one
        
        res = []
        balance = 0
        prev = None
        for time, status in events:
            if balance == 0 and prev:
                res.append(Interval(prev, time))
            balance += 1 if status == OPEN else -1
            prev = time
        return res
            