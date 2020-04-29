'''
keys:
Solutions:
Similar:
T:
S:
'''


import heapq
class Solution:
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


    # heapq, T:O(nlogn), S:O(n)
    def minMeetingRooms2(self, intervals):
        intervals.sort(key = lambda x: x[0])
        heap = [] # stores the end time of intervals, i.e., # of rooms

        for pair in intervals:
            if heap and pair[0] >= heap[0]: # using the same room
                heapq.heapreplace(heap, pair[1]) # pop the min, and push new end time
            else: # create a new room
                heapq.heappush(heap, pair[1])
        return len(heap)


obj = Solution()
print (obj.minMeetingRooms([[0, 30],[5, 15],[10, 20]]))
