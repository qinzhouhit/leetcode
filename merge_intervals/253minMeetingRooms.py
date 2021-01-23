'''
keys: heapq
Solutions: 
Similar: 
1) Given a list of intervals, find the point where the maximum number of intervals overlap.
2) 
T:
S:
'''
from typing import List

# keep track of the mutual exclusiveness of the overlapping meetings.
import heapq
class Solution:
    # heapq, T:O(nlogn), S:O(n)
    # keep track of the ending time of all the meetings currently happening
    def minMeetingRooms2(self, intervals):
        # sorting for O(nlogn)
        intervals.sort(key = lambda x: x[0]) # since we allocate for the earlier meetings
        heap = [] # stores the end time of active and overlapping meetings

        # O(nlogn), O(n) for n collided meetings, each operation take O(logn)
        for start, end in intervals: # heap[0]: earliest meeting ending time
            if heap and start >= heap[0]: # using the same room
                heapq.heapreplace(heap, end) # pop the min, and push new end time
            else: # create a new room, track ending time
                heapq.heappush(heap, end)
        return len(heap)
    
    
    # short version of minMeetingRooms1
    # draw the intervals to better understand
    def minMeetingRooms(self, intervals):
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        e = res = 0 # Think about e as an index to the first available room
        # 1st, how may meetings start (start list) before the first meeting to end (end[0]).
        # 2nd, how many meetings start before the second meeting to end (end[1]) and so on.
        for s in range(len(starts)):
            if starts[s] < ends[e]: # next conf starts and last conf doesn't end
                res += 1
            else: # last meeting ends
                e += 1 # then next meeting
        return res

    # https://leetcode.com/problems/meeting-rooms-ii/discuss/67860/My-Python-Solution-With-Explanation
    def minMeetingRooms1(self, intervals):
        starts = sorted(i[0] for i in intervals)
        ends = sorted(i[1] for i in intervals)

        s = e = 0
        avail = 0; numRoom = 0
        while s < len(starts):
            if starts[s] < ends[e]: # next conf starts and last conf doesn't end
                if avail == 0:
                    numRoom += 1
                else:
                    avail -= 1
                s += 1
            else: # if last conf ends, then avail += 1
                avail += 1
                e += 1
        return numRoom


    


obj = Solution()
print (obj.minMeetingRooms([[0, 30],[5, 15],[10, 20]]))
