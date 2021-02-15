'''
keys: two pointers
Solutions:
Similar:
T:
S:
'''
from typing import List


class Solution:
    # O(M+N) for S and T; M, N as the length of A and B
    # S: O(1)
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i = j = 0

        while i < len(A) and j < len(B):
            lo = max(A[i][0], B[j][0])
            hi = min(A[i][1], B[j][1])
            if lo <= hi: # notice that overlapping at one idx, e.g., [5,5], also legit
                res.append([lo, hi])

            # remove the interval with the smallest endpoint
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1

        return res

    # educative.io version
    def intervalIntersection1(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        res = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            # whenever the two intervals overlap, one of the interval’s start time 
            # lies within the other interval. 
            a_overlaps_b = B[j][0] <= A[i][0] <= B[j][1]
            b_overlaps_a = A[i][0] <= B[j][0] <= A[i][1]
            if a_overlaps_b or b_overlaps_a:
                res.append([max(A[i][0], B[j][0]), min(A[i][1], B[j][1])])
            # move next from the interval which is finishing first
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res
