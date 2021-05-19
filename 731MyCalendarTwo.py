'''
keys: segment tree
Solutions:
Similar:
T:
S:
'''
from typing import List


class MyCalendarTwo:

    def __init__(self):
        

    def book(self, start: int, end: int) -> bool:
        

# brute force
# T: O(N^2), S: O(N), N as size of calendar
'''
Evidently, two events [s1, e1) and [s2, e2) do not conflict if and 
only if one of them starts after the other one ends: either 
e1 <= s2 OR e2 <= s1. By De Morgan's laws, this means the events conflict
 when s1 < e2 AND s2 < e1
'''
class MyCalendarTwo:

    def __init__(self):
        self.calendar = [] # records original intervals
        self.overlaps = [] # records overlapping intersections

    def book(self, start, end):
        for s, e in self.overlaps:
            if start < e and end > s:
                return False
        for s, e in self.calendar:
            if start < e and end > s:
                self.overlaps.append((max(start, s), min(end, e)))
        self.calendar.append((start, end)) 
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)