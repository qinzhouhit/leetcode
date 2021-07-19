""" 
keys: 
Solutions:
Similar:
T:
S:
"""


from collections import Counter


# https://leetcode.com/problems/my-calendar-iii/discuss/109556/JavaC%2B%2B-Clean-Code
# T: O(N^2), N as number of events booked
# S: O(N)
class MyCalendarThree:

    def __init__(self):
    	self.delta = Counter()
        

    def book(self, start: int, end: int) -> int:
        self.delta[start] += 1  # each start add a new ongoing event at that time
        self.delta[end] -= 1  # each end terminate an ongoing event.

        # scan the timeline to figure out the maximum number of ongoing
        # event at any time.
        active = res = 0
        for x in sorted(self.delta):  
        	active += self.delta[x]  # the active will increase until it hits terminations
        	if active > res:
        		res = active
        return res 


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book(start,end)