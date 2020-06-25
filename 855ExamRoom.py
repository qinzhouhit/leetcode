'''
keys: bisect.insort
This module provides support for maintaining a list in sorted order without
 having to sort the list after each insertion.
Solutions:
Similar:
T:
S:
'''
from typing import List
import bisect

class ExamRoom1:
    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        '''
        1. find the biggest distance at the start, at the end, and in the middle.
        2. insert index of seat
        3. return index
        :return:
        '''
        N, L = self.N, self.L
        if not L:
            res = 0
        else:
            d, res = L[0], 0 # starting from the leftmost
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d:
                res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        self.L.remove(p)


# offficial
class ExamRoom:

    def __init__(self, N: int):
        self.N = N
        self.students = [] # record the index of seats where people sit.

    def seat(self) -> int:
        # Let's determine student, the position of the next
        # student to sit down.
        if not self.students:
            idx = 0
        else:
            # Tenatively, dist is the distance to the closest student,
            # which is achieved by sitting in the position 'idx'.
            # We start by considering the left-most seat.
            dist, idx = self.students[0], 0
            for i, s in enumerate(self.students):
                if i:
                    prev = self.students[i-1]
                    # For each pair of adjacent students in positions (prev, s),
                    # d is the distance to the closest student;
                    # achieved at position prev + d.
                    d = (s - prev) // 2
                    if d > dist:
                        dist, idx = d, prev + d
            # Considering the right-most seat.
            d = self.N - 1 - self.students[-1]
            if d > dist:
                idx = self.N - 1
        # Add the student to our sorted list of positions.
        bisect.insort(self.students, idx)
        print (idx)
        return idx



    def leave(self, p: int) -> None:
        self.students.remove(p)


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(N)
# param_1 = obj.seat()
# obj.leave(p)



sol = ExamRoom(10)
sol.seat()
sol.seat()
sol.seat()
sol.seat()
sol.leave(4)
sol.seat()

